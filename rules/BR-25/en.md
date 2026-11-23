# A line has no item name

The name of what a line invoices is empty.

## What the rule checks

Each line of an invoice names the item or service it invoices: "Training workshop", "Course handbook"… The rule checks that each line gives that name.

## Why it matters

BR-25 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-25 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give a name to each item and service in your software's catalogue.
2. For a line typed by hand, write what it invoices.
3. If the name is missing from the e-invoice, report it to the software's publisher, quoting BR-25.

## Common causes

- **An item known only by its reference** in the catalogue.
- **A description kept in a separate field** that the e-invoice does not use as the name.

## Technical details

The item name is BT-153. In CII, it is `ram:Name` of the line's `ram:SpecifiedTradeProduct`; in UBL, `cbc:Name` of the line's `cac:Item`.

The example invoice leaves its first line's item name empty, so it fails BR-25 alone.

## Official text

> Each Invoice line (BG-25) shall contain the Item name (BT-153).

BR-25, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-21](../BR-21/): each invoice line must have its identifier, a line number for example.
- [BR-16](../BR-16/): every invoice must have at least one line, credit notes included: for a lump sum, a single line will do.
