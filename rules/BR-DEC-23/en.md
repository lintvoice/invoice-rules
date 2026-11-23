# A line's net amount has more than 2 decimals

A line's net amount is written with more than 2 decimals.

## What the rule checks

Each invoice line has a net amount, the quantity times the price, minus the line's allowances and plus its charges. The rule checks that each line's net amount is written with at most 2 decimals. For example, `1230.50` passes and `1230.505` fails. Trailing zeros count too, so `1230.500` fails, although it is the same amount.

## Why it matters

BR-DEC-23 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-23 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Round each line's net amount to the cent, after multiplying the quantity by the price.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros (`1230.50`, not `1230.500`).
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-23.

## Common causes

- **A quantity times a price not rounded** (2.5 hours at 33.33 is 83.325).
- **An export that writes amounts with 3 decimals or more** (`1230.500`), even when they are rounded.

## Technical details

A line's net amount is BT-131, in group BG-25. In CII, the rule reads `ram:LineTotalAmount` of each line's `ram:SpecifiedTradeSettlementLineMonetarySummation`; in UBL, `cbc:LineExtensionAmount` of each `cac:InvoiceLine` (or `cac:CreditNoteLine`). It counts the decimals written after the dot, so a trailing zero counts too, and `10.250` fails although it is worth `10.25`.

## Official text

> The allowed maximum number of decimals for the Invoice line net amount (BT-131) is 2.

BR-DEC-23, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-09](../BR-DEC-09/): the total of the lines, at most 2 decimals.
- [BR-CO-10](../BR-CO-10/): the total of the lines must be the sum of the lines.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
