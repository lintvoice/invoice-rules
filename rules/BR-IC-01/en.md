# Intra-Community supplies need exactly one VAT breakdown

The invoice uses the VAT category K (intra-Community supply), but its VAT breakdown leaves it out, or gives it twice.

## What the rule checks

The VAT breakdown sums up the invoice's VAT: for each category and rate, its taxable amount and its VAT. Category K covers goods sold and sent to a business in another EU country, which accounts for the VAT there. Its VAT is 0, but it still has a breakdown, one for all its lines, allowances and charges together. The rule checks that the invoice has exactly one.

## Why it matters

BR-IC-01 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-IC-01 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Let your software compute the VAT breakdown from the lines: one per category and rate, even when the VAT is 0.
2. Check that the breakdown is written once per category, not once per line.
3. If the breakdown is missing or repeated, report it to the software's publisher, quoting BR-IC-01.

## Common causes

- **A breakdown written only for the categories that carry VAT**, leaving out those at 0.
- **One breakdown per line** instead of one per category and rate.

## Technical details

The VAT breakdown is group BG-23, its category code BT-118; the categories of a line, an allowance and a charge are BT-151, BT-95 and BT-102. In CII: each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `K`; in UBL: each `cac:TaxSubtotal` whose `cac:TaxCategory/cbc:ID` is `K`.

In CII, the rule also refuses a breakdown in the category when no line, allowance or charge uses it; UBL does not check that direction ([issue #538](https://github.com/ConnectingEurope/eInvoicing-EN16931/issues/538), open).

The example invoice is all in K and gives one breakdown per line instead of one for the category. A Factur-X invoice cannot leave its only breakdown out: its XML schema requires one. Each breakdown then has its own line's amount as taxable amount, so BR-IC-08, which compares it with all the lines of the category, fails too.

## Official text

> An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Intra-community supply" shall contain in the VAT breakdown (BG-23) exactly one VAT category code (BT-118) equal with "Intra-community supply".

BR-IC-01, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-IC-08](../BR-IC-08/): in the VAT breakdown, the taxable amount of category K (intra-Community supply) is the sum of its lines, plus its charges, minus its allowances.
- [BR-CO-18](../BR-CO-18/): every invoice must break down its VAT by category and rate, even when the VAT is zero.
- [BR-IC-02](../BR-IC-02/): an invoice with a line in the VAT category K (intra-Community supply) must give the seller's and the buyer's VAT numbers.
