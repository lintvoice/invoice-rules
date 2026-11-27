# The VAT amount for operations outside the scope of VAT must be zero

The VAT breakdown in category O (outside the scope of VAT) has a VAT amount other than 0.

## What the rule checks

Category O covers operations no VAT applies to, such as a service supplied to a business outside the EU. No VAT is charged in this category, so the VAT amount of its breakdown is 0. The rule checks it.

## Why it matters

BR-O-09 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-O-09 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. If no VAT is due, set the VAT amount of category O to 0, and correct the VAT total.
2. If VAT is due, the category is not O: give the items their right category and rate.
3. If your software computes VAT on this category, report it to the software's publisher, quoting BR-O-09.

## Common causes

- **VAT computed at the standard rate** on items whose category was changed afterwards.
- **A category O chosen by mistake** for a supply that does carry VAT.

## Technical details

A category's VAT amount is BT-117. In CII: `ram:CalculatedAmount` of each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `O`; in UBL: `cbc:TaxAmount` of each `cac:TaxSubtotal` of category `O`. The rule wants exactly 0.

The example invoice is all in O, and its breakdown gives a VAT amount at the standard rate of its taxable amount, with a rate of 0%; its VAT total follows. BR-CO-17, which checks the VAT amount against the taxable amount times the rate, fails too.

## Official text

> The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Not subject to VAT" shall be 0 (zero).

BR-O-09, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-O-08](../BR-O-08/): in the VAT breakdown, the taxable amount of category O (outside the scope of VAT) is the sum of its lines, plus its charges, minus its allowances.
- [BR-O-05](../BR-O-05/): an invoice line outside the scope of VAT (O) gives no VAT rate, not even 0%.
- [BR-CO-17](../BR-CO-17/): for each rate, the VAT amount must be the taxable amount times the rate, rounded to the cent.
