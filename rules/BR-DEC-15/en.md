# The VAT total in the VAT accounting currency is not rounded to the cent

The VAT total in the VAT accounting currency has more than 2 decimals, because it is not rounded to the cent.

## What the rule checks

When the invoice is in another currency than the one the seller accounts for VAT in, it also gives its VAT total converted into that currency, for example in euros for an invoice in US dollars. The rule checks that the VAT total in that currency is rounded to the cent, with at most 2 decimals. For example, `179.48` passes and `179.482` fails.

## Why it matters

BR-DEC-15 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-DEC-15 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Convert the VAT total at the exchange rate, then round the result to the cent.
2. Check that the e-invoice writes this amount rounded to the cent.
3. If your software writes it with more decimals, report it to the software's publisher, quoting BR-DEC-15.

## Common causes

- **The VAT total converted at the exchange rate**, and not rounded to the cent.
- **The VAT of each line converted one by one**, then added up without rounding.

## Technical details

The VAT total in the VAT accounting currency is BT-111, in group BG-22. The invoice must give it when it names a VAT accounting currency (BT-6), which must differ from the invoice currency (BT-5), as rule BR-53 requires. In CII, it is the `ram:TaxTotalAmount` whose `currencyID` is the VAT accounting currency, and the rule reads its value, not how it is written, so `179.480` passes and `179.482` fails. In UBL, the test of the 1.3.17 files compares the amount's currency with a currency code it looks for under the amount itself, where there is none, so the rule does not fire; the UBL syntax rule UBL-DT-01, which allows at most 2 decimals in every amount, catches such an amount.

## Official text

> The allowed maximum number of decimals for the Invoice total VAT amount in accounting currency (BT-111) is 2.

BR-DEC-15, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-13](../BR-DEC-13/): the VAT total, at most 2 decimals.
- [BR-FR-CO-12](../BR-FR-CO-12/): in France, an invoice in a foreign currency gives its VAT in euros.
- [BR-FR-DEC-01](../BR-FR-DEC-01/): in France, the same limit on every amount, with a dot as decimal separator.
