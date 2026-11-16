# The sum of line net amounts is not the total of the lines

The invoice's sum of line net amounts is not equal to the total of each line's net amount.

## What the rule checks

Each invoice line has a net amount: the quantity times the price, after the line's allowances and charges. The invoice also gives the total of these amounts. The rule checks that this total is exactly the sum of the lines, to the cent.

## Why it matters

BR-CO-10 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-10 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Add up the net amounts of all lines, each rounded to the cent, and give the result as the sum of line net amounts.
2. Check that no line was added, removed or changed after the totals were computed.
3. If your software computes this total another way, report it to the software's publisher, quoting BR-CO-10.

## Common causes

- **A line changed, added or removed after the totals were computed.**
- **Different rounding:** the total is computed from unrounded amounts, while each line is rounded.

## Technical details

The sum of line net amounts is BT-106, each line's net amount BT-131. The rule compares BT-106 with the sum of the BT-131, rounded to the cent. In CII, it compares the `ram:LineTotalAmount` of `ram:SpecifiedTradeSettlementHeaderMonetarySummation` with those of the `ram:SpecifiedTradeSettlementLineMonetarySummation`; in UBL, `cac:LegalMonetaryTotal/cbc:LineExtensionAmount` with the `cbc:LineExtensionAmount` of each `cac:InvoiceLine` (or `cac:CreditNoteLine`).

## Official text

> Sum of Invoice line net amount (BT-106) = Σ Invoice line net amount (BT-131).

BR-CO-10, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-13](../BR-CO-13/): the total without VAT must be the sum of the lines, minus allowances, plus charges.
- [BR-CO-15](../BR-CO-15/): the total with VAT must be the total without VAT plus the VAT.
