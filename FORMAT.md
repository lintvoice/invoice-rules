# Rule page format

One folder per rule, named by its official id: `rules/<RULE-ID>/`. Three files, all required:

| File | Content |
| --- | --- |
| `meta.yaml` | Facts about the rule: rule set and version, business terms, XML paths, the official message, examples, related rules, search terms. Machine-read by the site and by lintvoice |
| `en.md` | The page in English |
| `fr.md` | The same page in French, written natively, not translated word for word |

German (`de.md`) comes later, starting with the BR-DE rules.

## `meta.yaml`

```yaml
id: BR-FR-10                         # the official rule id
rule_set:
  name: BR-FR (France_RFE, FNFE-MPE)
  version: 1.4.0.04
  source: https://github.com/fnfempe/France_RFE/tree/<commit>   # pinned: a tag or a commit
  licence: Apache-2.0 (repository); EUPL (Schematron headers)
severity: fatal                      # as the Schematron flags it
applies_to:
  syntaxes: [CII, UBL]
  when: {en: "...", fr: "..."}       # in one line, when the rule runs
business_terms: [BT-30]
paths:                               # where the checked value sits
  cii: /rsm:CrossIndustryInvoice/...
  ubl: /Invoice/...
official_message:                    # a short quote of the rule's own message, never more
  lang: fr
  text: "..."
  source: https://github.com/.../<file>.sch   # pinned
reported_ids: [BR-FR-10_BT-30]       # the ids a validator reports (assert ids)
title: {en: "...", fr: "..."}        # the H1, in plain words
brief: {en: "...", fr: "..."}        # "In short" / "En bref": one sentence under the title, the fix
search: {en: [...], fr: [...]}       # what people type: rule id first, then the problem in their words
examples:                            # from lintvoice/invoice-examples, CC0
  source: invoice-examples
  version: 0.1.0
  target: fr
  valid: examples/fr/valid.xml
  invalid: examples/fr/invalid/BR-FR-10.xml   # or null when there is no example
  none: {en: "...", fr: "..."}   # with invalid: null, why there is no example, in plain words (shown on the page)
topic: identifiers                   # what the rule is about on the invoice (list below)
related: [BR-FR-09, BR-FR-11]
updated: 2026-11-05
```

**`topic`**, one per rule, from this fixed list: what the rule is about on the invoice, in the words of the people who
invoice. The rules index groups and filters by it. A new value comes only with a new subject (for example the rules
for several sellers or billing on behalf of a third party).

| `topic` | Subject |
| --- | --- |
| `addresses` | Electronic addresses |
| `identifiers` | Company identifiers: SIREN, SIRET, VAT numbers |
| `payment` | Payment and mandatory notes |
| `totals` | Amounts and totals |
| `vat` | VAT |
| `invoice` | Invoice number, dates and type |
| `lines` | Lines, allowances and charges |
| `corrections` | Credit notes, corrected invoices and advance payments |
| `attachments` | Attachments |

## `en.md` and `fr.md`

The same sections, in this order. The tests check them.

| English | French | What goes there |
| --- | --- | --- |
| `# <title>` | `# <titre>` | The plain-words title from `meta.yaml`, then one sentence: what fails |
| `## What the rule checks` | `## Ce que vérifie la règle` | The condition, in everyday words, for the people who invoice |
| `## Why it matters` | `## Pourquoi c'est important` | Who publishes the rule, since when it applies, what a failure means. Sourced |
| `## How to fix it` | `## Comment corriger` | Steps a person can take in their invoicing software, and when to report it to the software's publisher |
| `## Common causes` | `## Causes fréquentes` | What usually produces the error, in everyday words |
| `## Technical details` | `## Détails techniques` | For the people who build the software: business term numbers (BT), codes, XML elements, edge cases. The site adds the XML paths, the reported ids and the fix in the example file, from `meta.yaml` and the examples |
| `## Official text` | `## Texte officiel` | The rule's own message, quoted, with rule set, version and link |
| `## Related rules` | `## Règles voisines` | Links to the related rule pages, each with one line in everyday words |

The example is not written in the page: the site shows the difference between the failing example file and the
valid one, so it always matches the files people download.

## Writing rules

- **Everyday words first.** The sections before `Technical details` speak to the people who invoice (business owners,
  accountants): no business term numbers, no XML, no "Schematron" or "scheme". Say "vous" in French. Factual, teaching,
  concise: the reader gets the answer fast.
- **Our own words.** Explanations are written by us. The only copied text is the rule's own message, quoted and sourced,
  in the `Official text` section.
- **No AFNOR text, ever.** The BR-FR rules come from the AFNOR XP Z12-012 standard; we quote the FNFE-MPE Schematron
  messages (open licence), never the standard, and we do not use the French labels of NF EN 16931 (an AFNOR edition).
- **Facts carry a source:** an official document, a pinned rule file, or a pinned example.
- **"Checks against the official rules" (or "helps check"), never "certified" or "compliant".** An example "passes" or "fails" named rules at named versions.
- **Titles for search:** the site builds the HTML title as `<problem in plain words> (<RULE-ID>) · validator | lintvoice`;
  the page's H1 is the plain-words title.
- **Licence:** page text CC BY-SA 4.0 (`LICENSE`); XML examples CC0 (they come from `invoice-examples`).
