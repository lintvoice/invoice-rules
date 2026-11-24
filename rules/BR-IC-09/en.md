# The VAT amount for intra-Community supplies must be zero

The VAT breakdown in category K (intra-Community supply) has a VAT amount other than 0.

## What the rule checks

Category K covers goods sold and sent to a business in another EU country, which accounts for the VAT there. The invoice charges no VAT on it, so the VAT amount of its breakdown is 0. The rule checks it.

## Why it matters

BR-IC-09 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-IC-09 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. If no VAT is due, set the VAT amount of category K to 0, and correct the VAT total.
2. If VAT is due, the category is not K: give the items their right category and rate.
3. If your software computes VAT on this category, report it to the software's publisher, quoting BR-IC-09.

## Common causes

- **VAT computed at the standard rate** on items whose category was changed afterwards.
- **A category K chosen by mistake** for a supply that does carry VAT.

## Technical details

A category's VAT amount is BT-117. In CII: `ram:CalculatedAmount` of each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `K`; in UBL: `cbc:TaxAmount` of each `cac:TaxSubtotal` of category `K`. The rule wants exactly 0.

The example invoice is all in K, and its breakdown gives a VAT amount at the standard rate of its taxable amount, with a rate of 0 %; its VAT total follows. BR-CO-17, which checks the VAT amount against the taxable amount times the rate, fails too.

## Official text

> The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Intra-community supply" shall be 0 (zero).

BR-IC-09, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-IC-08](../BR-IC-08/): in the VAT breakdown, the taxable amount of category K (intra-Community supply) is the sum of its lines, plus its charges, minus its allowances.
- [BR-IC-05](../BR-IC-05/): in the VAT category K (intra-Community supply), the VAT rate of an invoice line is 0 %.
- [BR-CO-17](../BR-CO-17/): for each rate, the VAT amount must be the taxable amount times the rate, rounded to the cent.
