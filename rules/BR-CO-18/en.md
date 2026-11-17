# The invoice has no VAT breakdown

The invoice contains no VAT breakdown.

## What the rule checks

The invoice must contain at least one VAT breakdown: for each category and rate, the taxable amount and the VAT amount. This holds even for an invoice without VAT, an exempt one for example: the breakdown then gives the category, the taxable amount and a VAT amount of zero.

## Why it matters

BR-CO-18 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-18 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check that your software writes, for each VAT rate used, a breakdown with the taxable amount and the VAT amount.
2. For an invoice without VAT, give the category that applies (exemption, reverse charge…) with its taxable amount and a VAT amount of zero.
3. If your software does not send the VAT breakdown, report it to the software's publisher, quoting BR-CO-18.

## Common causes

- **An invoice without VAT** for which the software writes no breakdown.
- **A conversion from another format** that did not carry the VAT breakdown.

## Technical details

The VAT breakdown is group BG-23: taxable amount (BT-116), tax amount (BT-117), category (BT-118) and rate (BT-119). In CII, the rule looks for at least one `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`; in UBL, at least one `cac:TaxTotal/cac:TaxSubtotal`.

This page has no example file: a Factur-X invoice without a VAT breakdown does not pass the format's XML schema either, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only.

## Official text

> An Invoice shall at least have one VAT breakdown group (BG-23).

BR-CO-18, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-14](../BR-CO-14/): the VAT total must be the sum of the VAT for each rate.
- [BR-CO-04](../BR-CO-04/): each line must give its VAT category.
