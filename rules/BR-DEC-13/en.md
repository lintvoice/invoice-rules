# The VAT total is not rounded to the cent

The VAT total has more than 2 decimals, because it is not rounded to the cent.

## What the rule checks

The VAT total is the VAT of the whole invoice, all rates together, in the invoice's currency. The rule checks that the VAT total is rounded to the cent, with at most 2 decimals. For example, `194.75` passes and `194.754` fails.

## Why it matters

BR-DEC-13 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-13 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Round the VAT of each rate to the cent, then add up these rounded amounts to get the VAT total.
2. Do not compute the VAT total line by line from amounts that are not rounded.
3. If your software writes the VAT total with more decimals, report it to the software's publisher, quoting BR-DEC-13.

## Common causes

- **A VAT total computed line by line from VAT amounts that are not rounded**, and not rounded at the end.
- **A VAT total computed apart from the VAT breakdown**, which is rounded rate by rate.

## Technical details

The VAT total is BT-110, in group BG-22. In CII, the rule reads the value of the `ram:TaxTotalAmount` whose `currencyID` is the invoice currency (BT-5), not how it is written, so `194.750` passes and `194.754` fails. In UBL, the test of the 1.3.17 files compares the amount's currency with a currency code it looks for under the amount itself, where there is none, so the rule does not fire; the UBL syntax rule UBL-DT-01, which allows at most 2 decimals in every amount, catches such an amount.

A VAT total that is not rounded to the cent is no longer the sum of the VAT breakdown, which is rounded rate by rate, so BR-CO-14 fails with it, and the example invoice fails both rules.

## Official text

> The allowed maximum number of decimals for the Invoice total VAT amount (BT-110) is 2.

BR-DEC-13, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-20](../BR-DEC-20/): a rate's VAT amount, at most 2 decimals.
- [BR-CO-14](../BR-CO-14/): the VAT total must be the sum of the VAT for each rate.
- [BR-DEC-15](../BR-DEC-15/): the VAT total in the VAT accounting currency, at most 2 decimals.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
