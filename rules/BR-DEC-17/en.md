# The rounding amount has more than 2 decimals

The rounding amount is written with more than 2 decimals.

## What the rule checks

The rounding amount is what is added to the total, or taken from it, to round the amount due. The rule checks that the rounding amount is written with at most 2 decimals. For example, `0.02` passes and `0.025` fails. Trailing zeros count too, so `0.020` fails, although it is the same amount.

## Why it matters

BR-DEC-17 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-17 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Enter the rounding as an amount in cents, for example `0.02`.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros.
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-17.

## Common causes

- **A rounding computed as the difference with amounts that are not rounded.**
- **An export that writes every amount with 3 decimals**, even when it is rounded.

## Technical details

The rounding amount is BT-114, in group BG-22. In CII, the rule reads `ram:RoundingAmount` of `ram:SpecifiedTradeSettlementHeaderMonetarySummation`; in UBL, `cbc:PayableRoundingAmount` of `cac:LegalMonetaryTotal`. It counts the decimals as written after the dot.

## Official text

> The allowed maximum number of decimals for the Rounding amount (BT-114) is 2.

BR-DEC-17, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-18](../BR-DEC-18/): the amount due, at most 2 decimals.
- [BR-CO-16](../BR-CO-16/): the amount due must be the total with VAT, minus the amount already paid, plus the rounding.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
