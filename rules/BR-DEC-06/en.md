# The base amount of a charge on the whole invoice has more than 2 decimals

The base amount of a charge on the whole invoice is written with more than 2 decimals.

## What the rule checks

When a charge on the whole invoice is a percentage, the invoice can give the amount it is computed on, its base amount. The rule checks that the base amount of each charge on the whole invoice is written with at most 2 decimals. For example, `1230.50` passes and `1230.505` fails. Trailing zeros count too, so `1230.500` fails, although it is the same amount.

## Why it matters

BR-DEC-06 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-06 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Round the base amount of the charge to the cent.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros.
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-06.

## Common causes

- **A base amount taken from a total that is not rounded.**
- **An export that writes every amount with 3 decimals**, even when it is rounded.

## Technical details

The base amount of a charge on the whole invoice is BT-100, in group BG-21. In CII, the rule reads `ram:BasisAmount` of each `ram:SpecifiedTradeAllowanceCharge` in `ram:ApplicableHeaderTradeSettlement` whose `ram:ChargeIndicator` is `true`; in UBL, `cbc:BaseAmount` of each `cac:AllowanceCharge` of the document whose `cbc:ChargeIndicator` is `true`. It counts the decimals as written after the dot.

## Official text

> The allowed maximum number of decimals for the Document level charge base amount (BT-100) is 2.

BR-DEC-06, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-05](../BR-DEC-05/): the amount of a charge on the whole invoice, at most 2 decimals.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
