# A line has no line number

A line of the invoice has an empty identifier.

## What the rule checks

Each line of an e-invoice has an identifier, usually its number: 1, 2, 3… The buyer's software uses it to refer to a line, in a dispute or a credit note for example. The rule checks that each line has one.

## Why it matters

BR-21 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-21 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check that your software numbers the lines of each invoice.
2. Check that the e-invoice writes each line's number, the lines added by hand too.
3. If a line has no number in the e-invoice, report it to the software's publisher, quoting BR-21.

## Common causes

- **A line added by hand**, a comment or a discount line, that the software does not number.
- **Lines numbered on the PDF only.**

## Technical details

The invoice line identifier is BT-126. In CII, it is `ram:LineID` of the line's `ram:AssociatedDocumentLineDocument`; in UBL, `cbc:ID` of `cac:InvoiceLine` (`cac:CreditNoteLine` in a credit note).

The example invoice leaves its first line's identifier empty, so it fails BR-21 alone.

## Official text

> Each Invoice line (BG-25) shall have an Invoice line identifier (BT-126).

BR-21, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-25](../BR-25/): each invoice line must name what it invoices.
- [BR-16](../BR-16/): every invoice must have at least one line, credit notes included: for a lump sum, a single line will do.
