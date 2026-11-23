# A VAT rate has no VAT amount

A VAT breakdown gives no VAT amount.

## What the rule checks

The VAT breakdown gives, for each VAT category and rate of the invoice, its taxable amount, its VAT amount, its category and its rate. The rule checks that each one gives its VAT amount, 0 for a category without VAT.

## Why it matters

BR-46 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-46 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. For an exempt category, or a rate of 0 %, write a VAT amount of 0.
2. Check that the e-invoice writes the VAT breakdown in full, one block per category and rate.
3. If it is missing from the e-invoice, report it to the software's publisher, quoting BR-46.

## Common causes

- **A VAT amount left out because it is 0**, for an exempt line.
- **A VAT breakdown built by hand** in an export, field by field.

## Technical details

A VAT breakdown is group BG-23, here its VAT amount BT-117. In CII, it is `ram:CalculatedAmount` of each `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`; in UBL, `cbc:TaxAmount` of each `cac:TaxSubtotal`.

The example invoice has an exempt line whose VAT breakdown gives no VAT amount, although it is 0. Rules BR-CO-17 and BR-E-09, which check that amount, fail too. The Factur-X EN 16931 profile has its own rules, which check that the amount is there too: in a Factur-X invoice, its rule `FX-SCH-A-000176` fails next to BR-46, as in the example invoice.

## Official text

> Each VAT breakdown (BG-23) shall have a VAT category tax amount (BT-117).

BR-46, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-45](../BR-45/): each VAT breakdown must give its taxable amount, the total without VAT of what is invoiced in its category and at its rate.
- [BR-CO-17](../BR-CO-17/): for each rate, the VAT amount must be the taxable amount times the rate, rounded to the cent.
