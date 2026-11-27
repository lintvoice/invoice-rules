# The taxable amount for the zero rate does not match the lines

The taxable amount of the VAT breakdown in category Z (zero rate) does not match its lines, allowances and charges.

## What the rule checks

Category Z covers supplies taxed at a rate of 0%, such as solar panels sold to their operator in Germany. Its VAT is 0, but its breakdown still gives the amount it applies to. The rule checks that this taxable amount adds up the lines in Z, plus the charges and minus the allowances in Z.

## Why it matters

BR-Z-08 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-Z-08 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Add up the net amounts of the lines in Z, add the charges and subtract the allowances in Z: that is the expected taxable amount.
2. Attach each allowance and charge to the category of what it applies to.
3. If your software computes it another way, report it to the software's publisher, quoting BR-Z-08.

## Common causes

- **An allowance on the whole invoice** deducted from the total but not from its category's taxable amount.
- **A taxable amount typed by hand**, or not computed again after a line changed.

## Technical details

A category's taxable amount is BT-116; the net amounts of the lines are BT-131, the document level allowances BT-92 and charges BT-99. In CII: `ram:BasisAmount` of each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `Z`; in UBL: `cbc:TaxableAmount` of each `cac:TaxSubtotal` of category `Z`.

In CII, the rule accepts a gap strictly below 1 (one unit of the currency); in UBL, it requires an exact match.

The example invoice is all in Z, and states a taxable amount 1 € above the sum of its lines; its fixed version states the sum.

## Official text

> In a VAT breakdown (BG-23) where VAT category code (BT-118) is "Zero rated" the VAT category taxable amount (BT-116) shall equal the sum of Invoice line net amount (BT-131) minus the sum of Document level allowance amounts (BT-92) plus the sum of Document level charge amounts (BT-99) where the VAT category codes (BT-151, BT-95, BT-102) are "Zero rated".

BR-Z-08, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-Z-09](../BR-Z-09/): in the VAT category Z (zero rate), the invoice charges no VAT: the VAT amount of the category's breakdown is 0.
- [BR-Z-01](../BR-Z-01/): an invoice with a line, an allowance or a charge in the VAT category Z (zero rate) must have exactly one VAT breakdown for it.
- [BR-S-08](../BR-S-08/): for each rate, the taxable amount must be the sum of the lines at that rate, plus the charges and minus the allowances at the same rate.
