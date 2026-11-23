# The allowance total has more than 2 decimals

The allowance total is written with more than 2 decimals.

## What the rule checks

The allowance total is the sum of the allowances on the whole invoice. The rule checks that the allowance total is written with at most 2 decimals. For example, `1230.50` passes and `1230.505` fails. Trailing zeros count too, so `1230.500` fails, although it is the same amount.

## Why it matters

BR-DEC-10 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-10 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Compute the allowance total from the allowances rounded to the cent.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros (`1230.50`, not `1230.500`).
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-10.

## Common causes

- **A total computed from amounts that are not rounded**, and not rounded at the end.
- **An export that writes amounts with 3 decimals or more** (`1230.500`), even when they are rounded.

## Technical details

The allowance total is BT-107, in group BG-22. In CII, the rule reads `ram:AllowanceTotalAmount` of `ram:SpecifiedTradeSettlementHeaderMonetarySummation`; in UBL, `cbc:AllowanceTotalAmount` of `cac:LegalMonetaryTotal`. It counts the decimals written after the dot, so a trailing zero counts too, and `10.250` fails although it is worth `10.25`.

## Official text

> The allowed maximum number of decimals for the Sum of allowanced on document level (BT-107) is 2.

BR-DEC-10, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-01](../BR-DEC-01/): the amount of an allowance on the whole invoice, at most 2 decimals.
- [BR-CO-11](../BR-CO-11/): the allowance total must be the sum of the allowances on the whole invoice.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
