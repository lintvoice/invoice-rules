"""The glossary (FORMAT.md, "The glossary"): every word in both languages with a source, in a group that exists, its
anchor kept for good, and the wording rules."""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
GLOSSARY = yaml.safe_load((ROOT / "glossary.yaml").read_text(encoding="utf-8"))
LANGS = ("en", "fr")
FORBIDDEN = re.compile(r"certif|complian|conform", re.I)  # we help check; we never certify (FORMAT.md)
RULE_ID = re.compile(r"^BR(-[A-Z0-9]+)+$")
# The anchors published on 2026-11-23 (/glossary/#peppol, /fr/glossaire/#peppol): links point to them, so they stay.
PUBLISHED = {
    "annuaire", "autoliquidation", "cadre-de-facturation", "calendrier", "categorie-tva", "chorus-pro", "cii",
    "code-service", "e-reporting", "en-16931", "factur-x", "facture-electronique", "format-structure",
    "mentions-obligatoires", "nouvelles-mentions", "numero-engagement", "pdf-a-3", "peppol", "plateforme-agreee", "ppf",
    "profil-factur-x", "rectificative-avoir", "regle-de-gestion", "rejet-refus", "schematron", "siren", "siret",
    "statuts", "terme-metier", "tva-intracommunautaire", "ubl", "xrechnung", "zugferd",
}  # fmt: skip


def _words(entry, key):
    value = entry[key]
    assert set(value) == set(LANGS), f"{entry.get('id') or entry.get('key')}: {key} in {sorted(value)}"
    assert all(isinstance(value[lang], str) and value[lang].strip() for lang in LANGS)
    return value


def test_groups_have_a_key_and_their_words_in_both_languages():
    keys = [g["key"] for g in GLOSSARY["groups"]]
    assert len(keys) == len(set(keys))
    for g in GLOSSARY["groups"]:
        assert re.fullmatch(r"[a-z]+(-[a-z]+)*", g["key"])
        _words(g, "name")
        _words(g, "line")


def test_every_term_is_complete_and_in_a_group():
    groups = {g["key"] for g in GLOSSARY["groups"]}
    for t in GLOSSARY["terms"]:
        assert set(t) <= {"id", "group", "name", "text", "source", "source_name", "rules"}, t["id"]
        assert t["group"] in groups, t["id"]
        for key in ("name", "text", "source_name"):
            _words(t, key)
        assert t["source"].startswith("https://"), t["id"]
        assert all(RULE_ID.match(r) for r in t.get("rules", [])), t["id"]


def test_every_group_has_words():
    used = {t["group"] for t in GLOSSARY["terms"]}
    assert [g["key"] for g in GLOSSARY["groups"] if g["key"] not in used] == []


def test_anchors_are_unique_and_none_published_is_lost():
    ids = [t["id"] for t in GLOSSARY["terms"]]
    assert len(ids) == len(set(ids))
    assert all(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", i) for i in ids)
    assert PUBLISHED - set(ids) == set(), "an anchor the site published was renamed or removed"


def test_wording():
    for entry in GLOSSARY["groups"] + GLOSSARY["terms"]:
        for key in ("name", "line", "text", "source_name"):
            for lang in LANGS if key in entry else ():
                assert not FORBIDDEN.findall(entry[key][lang]), (entry.get("id") or entry.get("key"), key, lang)
