# The taxable amount for reverse charge does not match the lines

The taxable amount of the VAT breakdown in category AE (reverse charge) does not match its lines, allowances and charges.

## What the rule checks

Category AE covers supplies on which the buyer, not the seller, accounts for the VAT: the seller invoices without VAT. Its VAT is 0, but its breakdown still gives the amount it applies to. The rule checks that this taxable amount adds up the lines in AE, plus the charges and minus the allowances in AE.

## Why it matters

BR-AE-08 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-AE-08 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Add up the net amounts of the lines in AE, add the charges and subtract the allowances in AE: that is the expected taxable amount.
2. Attach each allowance and charge to the category of what it applies to.
3. If your software computes it another way, report it to the software's publisher, quoting BR-AE-08.

## Common causes

- **An allowance on the whole invoice** deducted from the total but not from its category's taxable amount.
- **A taxable amount typed by hand**, or not computed again after a line changed.

## Technical details

A category's taxable amount is BT-116; the net amounts of the lines are BT-131, the document level allowances BT-92 and charges BT-99. In CII: `ram:BasisAmount` of each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `AE`; in UBL: `cbc:TaxableAmount` of each `cac:TaxSubtotal` of category `AE`.

In CII, the rule accepts a gap strictly below 1 (one unit of the currency); in UBL, it requires an exact match.

The example invoice is all in AE, and states a taxable amount 1 € above the sum of its lines; its fixed version states the sum.

## Official text

> In a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Reverse charge" the VAT category taxable amount (BT-116) shall equal the sum of Invoice line net amounts (BT-131) minus the sum of Document level allowance amounts (BT-92) plus the sum of Document level charge amounts (BT-99) where the VAT category codes (BT-151, BT-95, BT-102) are "Reverse charge".

BR-AE-08, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-AE-09](../BR-AE-09/): in the VAT category AE (reverse charge), the invoice charges no VAT: the VAT amount of the category's breakdown is 0.
- [BR-AE-01](../BR-AE-01/): an invoice with a line, an allowance or a charge in the VAT category AE (reverse charge) must have exactly one VAT breakdown for it.
- [BR-S-08](../BR-S-08/): for each rate, the taxable amount must be the sum of the lines at that rate, plus the charges and minus the allowances at the same rate.
