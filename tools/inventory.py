"""List the business rules the site covers, from the official rule files lintvoice installs, and which ones
already have a failing example in invoice-examples.

    uv run python tools/inventory.py RULES_CACHE EXAMPLES_MANIFEST > inventory.json

RULES_CACHE is lintvoice's rules folder (en16931-<version>/, france-rfe-<version>/); EXAMPLES_MANIFEST is
invoice-examples' examples/fr/manifest.json.
"""

import json
import re
import sys
from pathlib import Path

# the attributes may hold ">" inside quotes (a test like "a >= b"): match quoted values whole
ASSERT = re.compile(r"<(?:\w+:)?assert\b((?:[^>\"]|\"[^\"]*\")*)>(.*?)</(?:\w+:)?assert>", re.S)
ATTR = re.compile(r'(\w+)="([^"]*)"')


def asserts(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    rules = []
    for m in re.finditer(r"<(?:\w+:)?rule\b([^>]*)>(.*?)</(?:\w+:)?rule>", text, re.S):
        context = dict(ATTR.findall(m.group(1))).get("context", "")
        for a in ASSERT.finditer(m.group(2)):
            attrs = dict(ATTR.findall(a.group(1)))
            if "id" in attrs:
                message = re.sub(r"<[^>]+>", "…", a.group(2))
                rules.append(
                    {
                        "id": attrs["id"],
                        "flag": attrs.get("flag", ""),
                        "context": context,
                        "message": re.sub(r"\s+", " ", message).strip(),
                    }
                )
    return rules


def base_id(assert_id):
    return re.sub(r"_.*$", "", assert_id)


def main(cache, manifest):
    cache = Path(cache)
    found = {}
    for path in sorted(cache.glob("en16931-*/*/schematron/preprocessed/*.sch")):
        syntax = path.parts[-4].upper()
        for r in asserts(path):
            if r["id"].startswith("BR-"):
                e = found.setdefault(
                    r["id"],
                    {
                        "id": r["id"],
                        "set": "en16931",
                        "flags": set(),
                        "syntaxes": set(),
                        "messages": set(),
                        "asserts": set(),
                    },
                )
                e["flags"].add(r["flag"])
                e["syntaxes"].add(syntax)
                e["messages"].add(r["message"])
                e["asserts"].add(r["id"])
    for path in sorted(cache.glob("france-rfe-*/FNFE_RFE_INVOICE/*/*/schematron/BR-FR-Flux2-Schematron-*.sch")):
        if "WARNING" in path.name:
            continue
        syntax, profile = path.parts[-4], path.parts[-3]
        for r in asserts(path):
            if r["id"].startswith("BR-FR"):
                rid = base_id(r["id"])
                e = found.setdefault(
                    rid,
                    {
                        "id": rid,
                        "set": "brfr",
                        "flags": set(),
                        "syntaxes": set(),
                        "messages": set(),
                        "asserts": set(),
                        "profiles": set(),
                    },
                )
                e["flags"].add(r["flag"])
                e["syntaxes"].add(syntax)
                e["messages"].add(r["message"])
                e["asserts"].add(r["id"])
                e.setdefault("profiles", set()).add(profile)
    examples = json.loads(Path(manifest).read_text(encoding="utf-8"))["examples"]
    fired = {}
    for ex in examples:
        for f in ex.get("fires", []):
            fired.setdefault(base_id(f) if f.startswith("BR-FR") else f, []).append(ex["id"])
    out = []
    for rid in sorted(found):
        e = found[rid]
        out.append({k: sorted(v) if isinstance(v, set) else v for k, v in e.items()} | {"examples": fired.get(rid, [])})
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(*sys.argv[1:3])
