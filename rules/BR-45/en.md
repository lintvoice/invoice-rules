# A VAT rate has no taxable amount

A VAT breakdown gives no taxable amount.

## What the rule checks

The VAT breakdown gives, for each VAT category and rate of the invoice, its taxable amount, its VAT amount, its category and its rate. The rule checks that each one gives its taxable amount.

## Why it matters

BR-45 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-45 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check that your software computes the taxable amount of every VAT category, the exempt ones and those at 0 % included.
2. Check that the e-invoice writes the VAT breakdown in full, one block per category and rate.
3. If it is missing from the e-invoice, report it to the software's publisher, quoting BR-45.

## Common causes

- **A category without VAT left out of the computation**, an exempt line for example.
- **A VAT breakdown built by hand** in an export, field by field.

## Technical details

A VAT breakdown is group BG-23, here its taxable amount BT-116. In CII, it is `ram:BasisAmount` of each `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`; in UBL, `cbc:TaxableAmount` of each `cac:TaxSubtotal`.

The example invoice has an exempt line whose VAT breakdown gives no taxable amount. Rule BR-E-08, which compares that amount with the exempt lines, fails too. The Factur-X EN 16931 profile has its own rules, which check that the amount is there too: in a Factur-X invoice, its rule `FX-SCH-A-000177` fails next to BR-45, as in the example invoice.

## Official text

> Each VAT breakdown (BG-23) shall have a VAT category taxable amount (BT-116).

BR-45, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-46](../BR-46/): each VAT breakdown must give its VAT amount, even when it is 0.
- [BR-S-08](../BR-S-08/): for each rate, the taxable amount must be the sum of the lines at that rate, plus the charges and minus the allowances at the same rate.
