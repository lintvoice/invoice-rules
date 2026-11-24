# The taxable amount for operations outside the scope of VAT does not match the lines

The taxable amount of the VAT breakdown in category O (outside the scope of VAT) does not match its lines, allowances and charges.

## What the rule checks

Category O covers operations no VAT applies to, such as a service supplied to a business outside the EU. Its VAT is 0, but its breakdown still gives the amount it applies to. The rule checks that this taxable amount adds up the lines in O, plus the charges and minus the allowances in O.

## Why it matters

BR-O-08 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-O-08 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Add up the net amounts of the lines in O, add the charges and subtract the allowances in O: that is the expected taxable amount.
2. Attach each allowance and charge to the category of what it applies to.
3. If your software computes it another way, report it to the software's publisher, quoting BR-O-08.

## Common causes

- **An allowance on the whole invoice** deducted from the total but not from its category's taxable amount.
- **A taxable amount typed by hand**, or not computed again after a line changed.

## Technical details

A category's taxable amount is BT-116; the net amounts of the lines are BT-131, the document level allowances BT-92 and charges BT-99. In CII: `ram:BasisAmount` of each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `O`; in UBL: `cbc:TaxableAmount` of each `cac:TaxSubtotal` of category `O`.

In CII and in UBL, the rule requires an exact match, each sum rounded to the cent.

The example invoice is all in O, and states a taxable amount 1 € above the sum of its lines; its fixed version states the sum.

## Official text

> In a VAT breakdown (BG-23) where the VAT category code (BT-118) is " Not subject to VAT" the VAT category taxable amount (BT-116) shall equal the sum of Invoice line net amounts (BT-131) minus the sum of Document level allowance amounts (BT-92) plus the sum of Document level charge amounts (BT-99) where the VAT category codes (BT-151, BT-95, BT-102) are "Not subject to VAT".

BR-O-08, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-O-09](../BR-O-09/): in the VAT category O (outside the scope of VAT), the invoice charges no VAT: the VAT amount of the category's breakdown is 0.
- [BR-O-01](../BR-O-01/): an invoice with a line, an allowance or a charge in the VAT category O (outside the scope of VAT) must have exactly one VAT breakdown for it.
- [BR-S-08](../BR-S-08/): for each rate, the taxable amount must be the sum of the lines at that rate, plus the charges and minus the allowances at the same rate.
