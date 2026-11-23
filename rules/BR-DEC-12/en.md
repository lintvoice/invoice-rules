# The total without VAT has more than 2 decimals

The total without VAT is written with more than 2 decimals.

## What the rule checks

The total without VAT is the total of the lines, minus the allowances and plus the charges on the whole invoice. The rule checks that the total without VAT is written with at most 2 decimals. For example, `1230.50` passes and `1230.505` fails. Trailing zeros count too, so `1230.500` fails, although it is the same amount.

## Why it matters

BR-DEC-12 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-12 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Compute the total without VAT from amounts rounded to the cent: the lines, the allowances and the charges.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros.
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-12.

## Common causes

- **A total computed from amounts that are not rounded**, and not rounded at the end.
- **An export that writes every amount with 3 decimals**, even when it is rounded.

## Technical details

The total without VAT is BT-109, in group BG-22. In CII, the rule reads `ram:TaxBasisTotalAmount` of `ram:SpecifiedTradeSettlementHeaderMonetarySummation`; in UBL, `cbc:TaxExclusiveAmount` of `cac:LegalMonetaryTotal`. It counts the decimals as written after the dot.

## Official text

> The allowed maximum number of decimals for the Invoice total amount without VAT (BT-109) is 2.

BR-DEC-12, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-09](../BR-DEC-09/): the total of the lines, at most 2 decimals.
- [BR-CO-13](../BR-CO-13/): the total without VAT must be the lines, minus the allowances, plus the charges.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
