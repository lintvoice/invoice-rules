# A rate's taxable amount has more than 2 decimals

A rate's taxable amount is written with more than 2 decimals.

## What the rule checks

In the VAT breakdown, each rate has its taxable amount, the total without VAT of what is invoiced at that rate. The rule checks that each rate's taxable amount is written with at most 2 decimals. For example, `1230.50` passes and `1230.505` fails. Trailing zeros count too, so `1230.500` fails, although it is the same amount.

## Why it matters

BR-DEC-19 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-19 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Compute each rate's taxable amount from the lines, allowances and charges at that rate, rounded to the cent.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros (`1230.50`, not `1230.500`).
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-19.

## Common causes

- **A taxable amount computed from line amounts that are not rounded.**
- **An export that writes amounts with 3 decimals or more** (`1230.500`), even when they are rounded.

## Technical details

A rate's taxable amount is BT-116, in group BG-23. In CII, the rule reads `ram:BasisAmount` of each `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`; in UBL, `cbc:TaxableAmount` of each `cac:TaxSubtotal`. It counts the decimals written after the dot, so a trailing zero counts too, and `10.250` fails although it is worth `10.25`.

## Official text

> The allowed maximum number of decimals for the VAT category taxable amount (BT-116) is 2.

BR-DEC-19, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-20](../BR-DEC-20/): a rate's VAT amount, at most 2 decimals.
- [BR-S-08](../BR-S-08/): a rate's taxable amount must be the sum of its lines, charges and allowances.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
