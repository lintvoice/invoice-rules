# The amount of an allowance on the whole invoice has more than 2 decimals

The amount of an allowance on the whole invoice is written with more than 2 decimals.

## What the rule checks

An allowance on the whole invoice is a discount granted on the invoice as a whole, not on one line, for example a trade discount. The rule checks that the amount of each allowance on the whole invoice is written with at most 2 decimals. For example, `1230.50` passes and `1230.505` fails. Trailing zeros count too, so `1230.500` fails, although it is the same amount.

## Why it matters

BR-DEC-01 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-01 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. If the allowance is a percentage, round its amount to the cent in your invoicing software.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros.
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-01.

## Common causes

- **A percentage allowance not rounded** (1.5% of 1234.50 is 18.5175).
- **An export that writes every amount with 3 decimals**, even when it is rounded.

## Technical details

The amount of an allowance on the whole invoice is BT-92, in group BG-20. In CII, the rule reads `ram:ActualAmount` of each `ram:SpecifiedTradeAllowanceCharge` in `ram:ApplicableHeaderTradeSettlement` whose `ram:ChargeIndicator` is `false`; in UBL, `cbc:Amount` of each `cac:AllowanceCharge` of the document whose `cbc:ChargeIndicator` is `false`. It counts the decimals as written after the dot.

## Official text

> The allowed maximum number of decimals for the Document level allowance amount (BT-92) is 2.

BR-DEC-01, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-02](../BR-DEC-02/): the base amount of an allowance on the whole invoice, at most 2 decimals.
- [BR-DEC-10](../BR-DEC-10/): the allowance total, at most 2 decimals.
- [BR-CO-11](../BR-CO-11/): the allowance total must be the sum of the allowances on the whole invoice.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
