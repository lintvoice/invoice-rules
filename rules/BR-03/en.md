# The invoice date is missing

The invoice's issue date is missing, or not written as a date.

## What the rule checks

Every invoice gives the date it was issued. The e-invoice writes it in a set form: year, month and day, with nothing else. The rule checks that the invoice gives its issue date in that form.

## Why it matters

BR-03 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-03 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check that each invoice has its issue date in your software.
2. Check that the e-invoice writes it as a date only, without a time.
3. If the date is missing or written with a time, report it to the software's publisher, quoting BR-03.

## Common causes

- **A date written with a time**, as a timestamp from a database.
- **A date left empty** in a draft sent too early.

## Technical details

The issue date is BT-2. In CII, the rule reads `udt:DateTimeString` of `ram:IssueDateTime` in `rsm:ExchangedDocument`, and only with the attribute `format="102"`, the form YYYYMMDD. In UBL, it reads `cbc:IssueDate`.

The example invoice writes the date and time `202610201430` in format 203. The Factur-X EN 16931 profile has its own rules, which check the date's format too: in a Factur-X invoice, its rule `FX-SCH-A-000554` fails next to BR-03, as in the example invoice.

## Official text

> An Invoice shall have an Invoice issue date (BT-2).

BR-03, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-02](../BR-02/): every invoice must have a number.
- [BR-FR-03](../BR-FR-03/): every date on the invoice must be a real date, with a year between 2000 and 2099.
