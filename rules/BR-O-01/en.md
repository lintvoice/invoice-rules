# Lines outside the scope of VAT need exactly one VAT breakdown

The invoice uses the VAT category O (outside the scope of VAT), but its VAT breakdown leaves it out, or gives it twice.

## What the rule checks

The VAT breakdown sums up the invoice's VAT: for each category and rate, its taxable amount and its VAT. Category O covers operations no VAT applies to, such as a service supplied to a business outside the EU. Its VAT is 0, but it still has a breakdown, one for all its lines, allowances and charges together. The rule checks that the invoice has exactly one.

## Why it matters

BR-O-01 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-O-01 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Let your software compute the VAT breakdown from the lines: one per category and rate, even when the VAT is 0.
2. Check that the breakdown is written once per category, not once per line.
3. If the breakdown is missing or repeated, report it to the software's publisher, quoting BR-O-01.

## Common causes

- **A breakdown written only for the categories that carry VAT**, leaving out those at 0.
- **One breakdown per line** instead of one per category and rate.

## Technical details

The VAT breakdown is group BG-23, its category code BT-118; the categories of a line, an allowance and a charge are BT-151, BT-95 and BT-102. In CII: each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `O`; in UBL: each `cac:TaxSubtotal` whose `cac:TaxCategory/cbc:ID` is `O`.

In CII, the rule only runs when the invoice has a breakdown in category O: it then refuses a second one, or one without any line, allowance or charge in O. An invoice with lines in O and no breakdown in O passes it in CII; UBL refuses it.

The example invoice is all in O and gives one breakdown per line instead of one for the category. A Factur-X invoice cannot leave its only breakdown out: its XML schema requires one. Each breakdown then has its own line's amount as taxable amount, so BR-O-08, which compares it with all the lines of the category, fails too.

## Official text

> An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Not subject to VAT" shall contain exactly one VAT breakdown group (BG-23) with the VAT category code (BT-118) equal to "Not subject to VAT".

BR-O-01, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-O-08](../BR-O-08/): in the VAT breakdown, the taxable amount of category O (outside the scope of VAT) is the sum of its lines, plus its charges, minus its allowances.
- [BR-CO-18](../BR-CO-18/): every invoice must break down its VAT by category and rate, even when the VAT is zero.
- [BR-O-02](../BR-O-02/): an invoice with a line outside the scope of VAT (O) must give no VAT number: not the seller's, not its tax representative's, not the buyer's.
