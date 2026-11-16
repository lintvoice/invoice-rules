# E-invoicing rules, explained

What each e-invoicing rule checks, why it matters and how to fix it, in plain words, with a valid and an invalid
example. One page per rule, in English and French, for the business rules of EN 16931 and of the French reform (BR-FR).

> Status: 40 pages: the 39 French reform rules (BR-FR) that have an example file, and BR-CO-15. Published on
> [lintvoice.com/rules](https://lintvoice.com/rules/) ([en français](https://lintvoice.com/fr/regles/)).

## Layout

```
rules/<RULE-ID>/meta.yaml   facts: rule set and version, business terms, XML paths, official message, examples
rules/<RULE-ID>/en.md       the page in English
rules/<RULE-ID>/fr.md       the page in French, written natively
```

The format is specified in [FORMAT.md](FORMAT.md). `uv run pytest` checks:
- every folder against it: required fields, the same sections in both languages, the official message quoted;
- the wording;
- that each invalid example fails the rule (with `invoice-examples` checked out next to this repo).

## Tools

```sh
uv run python tools/inventory.py RULES_CACHE EXAMPLES_MANIFEST            # every business rule, and which ones have an example
uv run python tools/scaffold.py RULES_CACHE EXAMPLES_MANIFEST BR-FR-12    # write a page's facts (meta.yaml) from the rule files
```

`RULES_CACHE` is the folder where lintvoice installs the official rule packs; `EXAMPLES_MANIFEST` is
`examples/fr/manifest.json` in invoice-examples. The words of a page are written by hand.

## Sources

The explanations are ours. The only quoted text is each rule's own message, from the pinned official files:
- [EN 16931 validation artefacts](https://github.com/ConnectingEurope/eInvoicing-EN16931) (ConnectingEurope);
- [France_RFE](https://github.com/fnfempe/France_RFE) (FNFE-MPE);
- [XRechnung Schematron](https://github.com/itplr-kosit/xrechnung-schematron) (KoSIT).

The examples come from [invoice-examples](https://github.com/lintvoice/invoice-examples).

## Licences

- Page text: [CC BY-SA 4.0](LICENSE). Reuse it, credit "invoice-rules (lintvoice)", share alike.
- XML examples: CC0, from invoice-examples.
