# Both a VAT point date and a VAT point date code are given

The invoice gives both the VAT point date and a code that stands for it, while only one of the two is allowed.

## What the rule checks

VAT becomes due on a given date. The invoice can state it in two ways: the date itself, or a code that points to a date the invoice already gives. The rule checks that the invoice uses only one of these two ways.

## Why it matters

BR-CO-03 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-03 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. In your invoicing software, choose one way to state when VAT becomes due: a date, or a code.
2. Do not give both on the same invoice, even if they mean the same day.
3. If your software fills in both on its own, report it to the software's publisher, quoting BR-CO-03.

## Common causes

- **A code added by default** by the software, while a date is entered as well.
- **An invoice converted from another format** that carried both.

## Technical details

The VAT point date is BT-7, its code BT-8. In CII, the rule looks for `ram:TaxPointDate` and `ram:DueDateTypeCode` in the invoice (in the VAT breakdown, `ram:ApplicableTradeTax`); in UBL, `cbc:TaxPointDate` and `cac:InvoicePeriod/cbc:DescriptionCode`.

## Official text

> Value added tax point date (BT-7) and Value added tax point date code (BT-8) are mutually exclusive.

BR-CO-03, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-FR-03](../BR-FR-03/): the invoice's dates, the VAT point date among them, must have a year between 2000 and 2099.
