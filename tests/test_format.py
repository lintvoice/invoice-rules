"""The rule page format (FORMAT.md): every rule folder is complete, both languages have the same sections,
facts point to pinned sources, and the wording rules hold."""

import json
import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
RULES = sorted(p for p in (ROOT / "rules").iterdir() if p.is_dir())
SECTIONS = {
    "en": [
        "What the rule checks",
        "Why it matters",
        "How to fix it",
        "Common causes",
        "Technical details",
        "Official text",
        "Related rules",
    ],
    "fr": [
        "Ce que vérifie la règle",
        "Pourquoi c'est important",
        "Comment corriger",
        "Causes fréquentes",
        "Détails techniques",
        "Texte officiel",
        "Règles voisines",
    ],
}
REQUIRED = [
    "id",
    "rule_set",
    "severity",
    "applies_to",
    "business_terms",
    "paths",
    "official_message",
    "reported_ids",
    "title",
    "search",
    "examples",
    "related",
    "updated",
    "topic",
]
# What a rule is about on the invoice, one per rule, from this fixed list (FORMAT.md): the rules index groups by it.
TOPICS = {
    "addresses",
    "parties",
    "identifiers",
    "payment",
    "totals",
    "vat",
    "invoice",
    "lines",
    "corrections",
    "attachments",
}
FORBIDDEN = re.compile(r"certif|complian|conform", re.I)  # we help check; we never certify (FORMAT.md)
EXAMPLES_REPO = ROOT.parent / "invoice-examples"


def meta(folder):
    return yaml.safe_load((folder / "meta.yaml").read_text(encoding="utf-8"))


@pytest.mark.parametrize("folder", RULES, ids=lambda p: p.name)
def test_rule_folder_is_complete(folder):
    for name in ("meta.yaml", "en.md", "fr.md"):
        assert (folder / name).exists(), name
    m = meta(folder)
    assert [k for k in REQUIRED if k not in m] == []
    assert m["id"] == folder.name
    assert set(m["title"]) == set(m["search"]) == {"en", "fr"}
    assert all(terms[0] == m["id"] for terms in m["search"].values()), "search terms start with the rule id"
    assert m["rule_set"]["source"].startswith("https://") and (
        "/tree/" in m["rule_set"]["source"] or "/tag/" in m["rule_set"]["source"]
    ), "the rule set source is pinned to a commit or a tag"
    assert set(m["paths"]) == {"cii", "ubl"}
    assert all(re.fullmatch(r"BT-\d+", bt) for bt in m["business_terms"])
    assert m["topic"] in TOPICS, f"topic {m['topic']!r} is not one of {sorted(TOPICS)}"


@pytest.mark.parametrize("lang", ["en", "fr"])
@pytest.mark.parametrize("folder", RULES, ids=lambda p: p.name)
def test_page_sections_and_title(folder, lang):
    m, text = meta(folder), (folder / f"{lang}.md").read_text(encoding="utf-8")
    assert text.splitlines()[0] == f"# {m['title'][lang]}"
    assert re.findall(r"^## (.+)$", text, re.M) == SECTIONS[lang]


@pytest.mark.parametrize("lang", ["en", "fr"])
@pytest.mark.parametrize("folder", RULES, ids=lambda p: p.name)
def test_official_message_is_quoted_in_its_section(folder, lang):
    m, text = meta(folder), (folder / f"{lang}.md").read_text(encoding="utf-8")
    section = text.split(f"## {SECTIONS[lang][5]}")[1].split("\n## ")[0]
    assert f"> {m['official_message']['text']}" in section


@pytest.mark.parametrize("lang", ["en", "fr"])
@pytest.mark.parametrize("folder", RULES, ids=lambda p: p.name)
def test_wording(folder, lang):
    text = (folder / f"{lang}.md").read_text(encoding="utf-8")
    assert not FORBIDDEN.findall(text)


TARGETS = {"en16931", "fr"}  # invoice-examples' targets, the European one first


@pytest.mark.parametrize("folder", RULES, ids=lambda p: p.name)
def test_examples_name_known_targets_the_european_one_first(folder):
    targets = list(meta(folder)["examples"]["targets"])
    assert set(targets) <= TARGETS
    assert targets == sorted(targets, key=["en16931", "fr"].index)


@pytest.mark.skipif(not EXAMPLES_REPO.exists(), reason="invoice-examples is not checked out next to this repo")
@pytest.mark.parametrize("folder", RULES, ids=lambda p: p.name)
def test_examples_exist_and_fail_the_rule(folder):
    ex = meta(folder)["examples"]
    if not ex["targets"]:
        # the page says why it has no example, in both languages, so that a visitor does not take it for a bug
        assert set(ex.get("none") or {}) == {"en", "fr"}, "a page without an example says why (examples.none)"
        pytest.skip("no example file for this rule")
    for target, files in ex["targets"].items():
        for key in ("valid", "invalid"):
            assert (EXAMPLES_REPO / files[key]).exists(), files[key]
        folder_of = f"examples/{target}/"
        manifest = json.loads((EXAMPLES_REPO / folder_of / "manifest.json").read_text(encoding="utf-8"))
        entry = next(e for e in manifest["examples"] if e["files"].get("xml") == files["invalid"].split(folder_of)[1])
        # a rule can be reported under several ids (one per field it checks); the example fails at least one of them
        assert set(meta(folder)["reported_ids"]) & set(entry["fires"]), (target, entry["id"])
        # the fix shown is the same invoice without the mistake: the fixed counterpart when the example first adds
        # something
        fixed = entry.get("fixed", {}).get("xml")
        assert files["valid"] == f"{folder_of}{fixed or 'valid.xml'}"
