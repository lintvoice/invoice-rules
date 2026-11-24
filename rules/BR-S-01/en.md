# Standard-rated lines need a VAT breakdown

The invoice uses the VAT category S (standard rate), but its VAT breakdown leaves it out.

## What the rule checks

The VAT breakdown sums up the invoice's VAT: for each category and rate, its taxable amount and its VAT. Category S covers VAT charged at a rate above zero, the reduced rates included. The rule checks that an invoice using S for a line, an allowance or a charge has a breakdown in S, one per rate.

## Why it matters

BR-S-01 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-S-01 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Let your software compute the VAT breakdown from the lines: one per category and rate.
2. Check that the breakdown is written once per category, not once per line.
3. If the breakdown is missing or repeated, report it to the software's publisher, quoting BR-S-01.

## Common causes

- **A breakdown dropped by an export or a conversion**, while the totals still count its VAT.
- **One breakdown per line** instead of one per category and rate.

## Technical details

The VAT breakdown is group BG-23, its category code BT-118; the categories of a line, an allowance and a charge are BT-151, BT-95 and BT-102. In CII: each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `S`; in UBL: each `cac:TaxSubtotal` whose `cac:TaxCategory/cbc:ID` is `S`.

In CII, the test adds the standard-rated lines (or allowances and charges) and the standard-rated breakdowns, and asks for at least two: an invoice with two standard-rated lines and no standard-rated breakdown passes it. UBL asks for a breakdown as soon as a line, allowance or charge is in S.

The example invoice has one standard-rated line and one exempt line, and no breakdown for the standard rate. Its VAT total still holds the line's VAT, as software that computes it from the lines would write it: BR-CO-14, which compares the VAT total with the breakdowns, fails too.

## Official text

> An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Standard rated" shall contain in the VAT breakdown (BG-23) at least one VAT category code (BT-118) equal with "Standard rated".

BR-S-01, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-S-08](../BR-S-08/): for each rate, the taxable amount must be the sum of the lines at that rate, plus the charges and minus the allowances at the same rate.
- [BR-CO-18](../BR-CO-18/): every invoice must break down its VAT by category and rate, even when the VAT is zero.
- [BR-CO-14](../BR-CO-14/): the VAT total must be exactly the sum of the VAT amounts computed for each rate, to the cent.
