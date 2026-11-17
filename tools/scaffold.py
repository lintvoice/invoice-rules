"""Write the facts of a rule page (meta.yaml) from the official rule files and the invoice-examples manifest:
the rule set, severity, the ids validators report, where the rule looks in CII and UBL, the official message and
the example files. The words (title, brief, search terms, when, topic, related) stay to be written; an existing
meta.yaml is never overwritten.

    uv run python tools/scaffold.py RULES_CACHE EXAMPLES_MANIFEST PAGE_ID [PAGE_ID ...]
    uv run python tools/scaffold.py RULES_CACHE EXAMPLES_MANIFEST --facts PAGE_ID   # print the raw facts
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
# the attributes may hold ">" inside quotes (a test like "a >= b"): match quoted values whole
ASSERT = re.compile(r"<(?:\w+:)?assert\b((?:[^>\"]|\"[^\"]*\")*)>(.*?)</(?:\w+:)?assert>", re.S)
RULE = re.compile(r"<(?:\w+:)?rule\b([^>]*)>(.*?)</(?:\w+:)?rule>", re.S)
ATTR = re.compile(r'(\w+)="([^"]*)"')
EN16931_TAG = "validation-{v}"
RFE_COMMIT = "97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d"  # France_RFE v1.4.0.04
# A rule whose context is the whole document says nothing about where it looks: no path is given then.
ROOT_CONTEXTS = {
    "rsm:CrossIndustryInvoice",
    "/rsm:CrossIndustryInvoice",
    "rsm:CrossIndustryInvoice/rsm:ExchangedDocument",
    "ubl:Invoice | cn:CreditNote",
    "cn:CreditNote",
    "/ubl:Invoice | /cn:CreditNote",
}


def page_of(assert_id):
    if assert_id == "BR-FR-MV-BD":
        return "BR-FR-BD-13"
    m = re.match(r"(BR-FR-(?:CO-|DEC-|MV-|BD-)?\d+|BR-(?:[A-Z]+-)?\d+)", assert_id)
    return m.group(1) if m else assert_id


def _asserts(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    for r in RULE.finditer(text):
        context = dict(ATTR.findall(r.group(1))).get("context", "")
        for a in ASSERT.finditer(r.group(2)):
            attrs = dict(ATTR.findall(a.group(1)))
            if "id" in attrs:
                yield {
                    "id": attrs["id"],
                    "flag": attrs.get("flag", ""),
                    "context": context,
                    "test": attrs.get("test", ""),
                    "message": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "…", a.group(2))).strip(),
                }


def collect(cache):
    cache, out = Path(cache), {}
    for path in sorted(cache.glob("en16931-*/*/schematron/preprocessed/*.sch")):
        version = path.parts[-5].split("-", 1)[1]
        syntax = "cii" if "CII" in path.name else "ubl"
        for a in _asserts(path):
            if a["id"].startswith("BR-"):
                a.update(
                    syntax=syntax,
                    set="en16931",
                    version=version,
                    source=f"https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/{EN16931_TAG.format(v=version)}",
                )
                out.setdefault(page_of(a["id"]), []).append(a)
    for path in sorted(cache.glob("france-rfe-*/FNFE_RFE_INVOICE/*/*/schematron/BR-FR-Flux2-Schematron-*.sch")):
        if "WARNING" in path.name:
            continue
        version = path.parts[-6].split("-", 2)[2]
        rel = "/".join(path.parts[-5:])
        for a in _asserts(path):
            if a["id"].startswith("BR-FR"):
                a.update(
                    syntax="ubl" if "UBL" in path.name else "cii",
                    profile=path.parts[-3],
                    set="brfr",
                    version=version,
                    source=f"https://github.com/fnfempe/France_RFE/blob/{RFE_COMMIT}/{rel}",
                )
                out.setdefault(page_of(a["id"]), []).append(a)
    return out


def _clean(message, assert_id):
    """The rule's own words: no leading id, no 'current value' tail."""
    m = re.sub(r"^\[?" + re.escape(assert_id.split("_")[0]) + r"[^:\]]*\]?\s*[:\-]\s*", "", message)
    m = re.sub(r"^\[[^\]]+\]\s*-?\s*", "", m)
    m = re.split(r"\s*(?:Valeur actuelle|Current value)\s*:", m)[0]
    return m.strip()


def facts(page_id, found, manifest):
    asserts = found[page_id]
    main = next((a for a in asserts if a["id"].split("_")[0] == page_id and a["syntax"] == "cii"), asserts[0])
    by_syntax = {}
    for a in asserts:
        by_syntax.setdefault(a["syntax"], a["context"])
    bts = sorted(
        {bt for a in asserts for bt in re.findall(r"BT-\d+", a["id"] + " " + a["message"])}, key=lambda b: int(b[3:])
    )
    examples = [e for e in manifest["examples"] if e["status"] == "invalid" and page_of(e["rule"]) == page_id]
    chosen = next((e for e in examples if e["id"] == page_id), examples[0] if examples else None)
    is_fr = main["set"] == "brfr"
    return {
        "id": page_id,
        "rule_set": {
            "name": "BR-FR (France_RFE, FNFE-MPE)" if is_fr else "EN 16931 validation artefacts (ConnectingEurope)",
            "version": main["version"],
            "source": f"https://github.com/fnfempe/France_RFE/tree/{RFE_COMMIT}" if is_fr else main["source"],
            "licence": "Apache-2.0 (repository); EUPL (Schematron headers)" if is_fr else "EUPL-1.2",
        },
        "severity": "fatal" if any(a["flag"] == "fatal" for a in asserts) else (main["flag"] or "fatal"),
        "applies_to": {
            "syntaxes": sorted({a["syntax"].upper() for a in asserts}),
            "when": {"en": "TODO", "fr": "TODO"},
        },
        "business_terms": bts,
        "paths": {
            k: "" if by_syntax.get(k, "").strip() in ROOT_CONTEXTS else by_syntax.get(k, "") for k in ("cii", "ubl")
        },
        "official_message": {
            "lang": "fr" if is_fr else "en",
            "text": _clean(main["message"], main["id"]),
            "source": main["source"],
        },
        "reported_ids": sorted({a["id"] for a in asserts}),
        "title": {"en": "TODO", "fr": "TODO"},
        "brief": {"en": "TODO", "fr": "TODO"},
        "search": {"en": [page_id], "fr": [page_id]},
        "examples": {
            "source": "invoice-examples",
            "version": manifest["generator"].split()[-1],
            "target": manifest["target"],
            "valid": f"examples/{manifest['target']}/valid.xml",
            "invalid": f"examples/{manifest['target']}/{chosen['files']['xml']}" if chosen else None,
        },
        "topic": "TODO",  # one of FORMAT.md's list: the tests refuse TODO
        "related": [],
        "updated": date.today().isoformat(),
    }


def main(argv):
    cache, manifest_path, *rest = argv
    found, manifest = collect(cache), json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    if rest and rest[0] == "--facts":
        for page_id in rest[1:]:
            print(json.dumps(found[page_id], ensure_ascii=False, indent=1))
        return 0
    for page_id in rest:
        target = ROOT / "rules" / page_id / "meta.yaml"
        if target.exists():
            print(f"{page_id}: meta.yaml exists, not touched")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            yaml.safe_dump(facts(page_id, found, manifest), allow_unicode=True, sort_keys=False, width=200),
            encoding="utf-8",
        )
        print(f"{page_id}: meta.yaml written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
