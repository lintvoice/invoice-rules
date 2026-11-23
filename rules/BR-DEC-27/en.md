# The amount of a line charge has more than 2 decimals

The amount of a line charge is written with more than 2 decimals.

## What the rule checks

A line charge is an amount added to one invoice line only, for example packaging. The rule checks that the amount of each line charge is written with at most 2 decimals. For example, `1230.50` passes and `1230.505` fails. Trailing zeros count too, so `1230.500` fails, although it is the same amount.

## Why it matters

BR-DEC-27 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-27 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. If the line charge is a percentage, round its amount to the cent.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros.
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-27.

## Common causes

- **A percentage charge not rounded** (1.5% of 1234.50 is 18.5175).
- **An export that writes every amount with 3 decimals**, even when it is rounded.

## Technical details

The amount of a line charge is BT-141, in group BG-28. In CII, the rule reads `ram:ActualAmount` of each `ram:SpecifiedTradeAllowanceCharge` in a line's `ram:SpecifiedLineTradeSettlement` whose `ram:ChargeIndicator` is `true`; in UBL, `cbc:Amount` of each `cac:AllowanceCharge` of a `cac:InvoiceLine` (or `cac:CreditNoteLine`) whose `cbc:ChargeIndicator` is `true`. It counts the decimals as written after the dot.

## Official text

> The allowed maximum number of decimals for the Invoice line charge amount (BT-141) is 2.

BR-DEC-27, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-28](../BR-DEC-28/): the base amount of a line charge, at most 2 decimals.
- [BR-CO-24](../BR-CO-24/): each line charge must have a reason, as text or as a code.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
