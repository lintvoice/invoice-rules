# The base amount of a line charge has more than 2 decimals

The base amount of a line charge is written with more than 2 decimals.

## What the rule checks

When a line charge is a percentage, the invoice can give the amount it is computed on, its base amount. The rule checks that the base amount of each line charge is written with at most 2 decimals. For example, `1230.50` passes and `1230.505` fails. Trailing zeros count too, so `1230.500` fails, although it is the same amount.

## Why it matters

BR-DEC-28 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-28 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Round the base amount of the line charge to the cent.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros (`1230.50`, not `1230.500`).
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-28.

## Common causes

- **A base amount taken from a total that is not rounded.**
- **An export that writes amounts with 3 decimals or more** (`1230.500`), even when they are rounded.

## Technical details

The base amount of a line charge is BT-142, in group BG-28. In CII, the rule reads `ram:BasisAmount` of each `ram:SpecifiedTradeAllowanceCharge` in a line's `ram:SpecifiedLineTradeSettlement` whose `ram:ChargeIndicator` is `true`; in UBL, `cbc:BaseAmount` of each `cac:AllowanceCharge` of a `cac:InvoiceLine` (or `cac:CreditNoteLine`) whose `cbc:ChargeIndicator` is `true`. It counts the decimals written after the dot, so a trailing zero counts too, and `10.250` fails although it is worth `10.25`.

## Official text

> The allowed maximum number of decimals for the Invoice line charge base amount (BT-142) is 2.

BR-DEC-28, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-27](../BR-DEC-27/): the amount of a line charge, at most 2 decimals.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
