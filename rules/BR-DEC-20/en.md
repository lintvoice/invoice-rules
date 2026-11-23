# A rate's VAT amount has more than 2 decimals

A rate's VAT amount is written with more than 2 decimals.

## What the rule checks

In the VAT breakdown, each rate has its VAT amount, the taxable amount times the rate. The rule checks that each rate's VAT amount is written with at most 2 decimals. For example, `1230.50` passes and `1230.505` fails. Trailing zeros count too, so `1230.500` fails, although it is the same amount.

## Why it matters

BR-DEC-20 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-20 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Round each rate's VAT amount to the cent.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros.
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-20.

## Common causes

- **A VAT amount computed as the taxable amount times the rate**, and not rounded.
- **An export that writes every amount with 3 decimals**, even when it is rounded.

## Technical details

A rate's VAT amount is BT-117, in group BG-23. In CII, the rule reads `ram:CalculatedAmount` of each `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`; in UBL, `cbc:TaxAmount` of each `cac:TaxSubtotal`. It counts the decimals as written after the dot.

## Official text

> The allowed maximum number of decimals for the VAT category tax amount (BT-117) is 2.

BR-DEC-20, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-19](../BR-DEC-19/): a rate's taxable amount, at most 2 decimals.
- [BR-CO-17](../BR-CO-17/): the VAT for each rate must be its taxable amount times the rate.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
