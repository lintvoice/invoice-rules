# The total with VAT has more than 2 decimals

The total with VAT is written with more than 2 decimals.

## What the rule checks

The total with VAT is the total without VAT plus the VAT total. The rule checks that the total with VAT is written with at most 2 decimals. For example, `1230.50` passes and `1230.505` fails. Trailing zeros count too, so `1230.500` fails, although it is the same amount.

## Why it matters

BR-DEC-14 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-14 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Compute the total with VAT from the total without VAT and the VAT total, both rounded to the cent.
2. Check that the e-invoice writes this amount with at most 2 decimals, without extra zeros.
3. If your software writes more decimals, report it to the software's publisher, quoting BR-DEC-14.

## Common causes

- **A total computed from amounts that are not rounded**, and not rounded at the end.
- **An export that writes every amount with 3 decimals**, even when it is rounded.

## Technical details

The total with VAT is BT-112, in group BG-22. In CII, the rule reads `ram:GrandTotalAmount` of `ram:SpecifiedTradeSettlementHeaderMonetarySummation`; in UBL, `cbc:TaxInclusiveAmount` of `cac:LegalMonetaryTotal`. It counts the decimals as written after the dot.

## Official text

> The allowed maximum number of decimals for the Invoice total amount with VAT (BT-112) is 2.

BR-DEC-14, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-12](../BR-DEC-12/): the total without VAT, at most 2 decimals.
- [BR-DEC-13](../BR-DEC-13/): the VAT total, at most 2 decimals.
- [BR-CO-15](../BR-CO-15/): the total with VAT must be the total without VAT plus the VAT total.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
