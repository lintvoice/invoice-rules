# The invoice currency is missing

The invoice's currency is empty.

## What the rule checks

All the amounts of an invoice are in one currency, which the e-invoice gives once, with its three-letter code: EUR for the euro, CHF for the Swiss franc… The rule checks that the invoice gives it.

## Why it matters

BR-05 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-05 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Set the currency of each invoice, or a default currency, in your software.
2. Check that the e-invoice writes its three-letter code.
3. If it stays empty, report it to the software's publisher, quoting BR-05.

## Common causes

- **No default currency** set in the software, for invoices in the home currency.
- **A currency shown as a symbol**, €, that the software does not turn into a code.

## Technical details

The invoice currency code is BT-5. In CII, it is `ram:InvoiceCurrencyCode` of `ram:ApplicableHeaderTradeSettlement`; in UBL, `cbc:DocumentCurrencyCode`. Its code comes from ISO 4217, as rule BR-CL-04 requires.

The example invoice leaves the currency empty, and so does the currency of its VAT total (`currencyID` of `ram:TaxTotalAmount`). An empty code is not in ISO 4217, so BR-CL-04 and BR-CL-03, which checks an amount's currency, fail too: the example fails all three rules.

## Official text

> An Invoice shall have an Invoice currency code (BT-5).

BR-05, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-04](../BR-CL-04/): the invoice currency must be a three-letter ISO 4217 code, such as EUR.
- [BR-CL-03](../BR-CL-03/): the currency written next to an amount must be a three-letter ISO 4217 code, such as EUR.
- [BR-FR-CO-12](../BR-FR-CO-12/): when the invoice is not in euros, it must give the VAT accounting currency (EUR) and the VAT total in euros.
