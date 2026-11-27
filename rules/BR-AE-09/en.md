# The VAT amount for reverse charge must be zero

The VAT breakdown in category AE (reverse charge) has a VAT amount other than 0.

## What the rule checks

Category AE covers supplies on which the buyer, not the seller, accounts for the VAT: the seller invoices without VAT. No VAT is charged in this category, so the VAT amount of its breakdown is 0. The rule checks it.

## Why it matters

BR-AE-09 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-AE-09 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. If no VAT is due, set the VAT amount of category AE to 0, and correct the VAT total.
2. If VAT is due, the category is not AE: give the items their right category and rate.
3. If your software computes VAT on this category, report it to the software's publisher, quoting BR-AE-09.

## Common causes

- **VAT computed at the standard rate** on items whose category was changed afterwards.
- **A category AE chosen by mistake** for a supply that does carry VAT.

## Technical details

A category's VAT amount is BT-117. In CII: `ram:CalculatedAmount` of each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `AE`; in UBL: `cbc:TaxAmount` of each `cac:TaxSubtotal` of category `AE`. The rule wants exactly 0.

The example invoice is all in AE, and its breakdown gives a VAT amount at the standard rate of its taxable amount, with a rate of 0%; its VAT total follows. BR-CO-17, which checks the VAT amount against the taxable amount times the rate, fails too.

## Official text

> The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Reverse charge" shall be 0 (zero).

BR-AE-09, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-AE-08](../BR-AE-08/): in the VAT breakdown, the taxable amount of category AE (reverse charge) is the sum of its lines, plus its charges, minus its allowances.
- [BR-AE-05](../BR-AE-05/): in the VAT category AE (reverse charge), the VAT rate of an invoice line is 0%.
- [BR-CO-17](../BR-CO-17/): for each rate, the VAT amount must be the taxable amount times the rate, rounded to the cent.
