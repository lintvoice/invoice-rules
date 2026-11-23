# The VAT accounting currency is not a valid code

The VAT accounting currency is not a currency code.

## What the rule checks

An invoice in a foreign currency can say in which currency the seller accounts for VAT. Currencies are written with their three-letter ISO 4217 code: EUR for the euro, USD for the US dollar, CHF for the Swiss franc… The rule checks that this currency is such a code, not a name, a symbol or another abbreviation.

## Why it matters

BR-CL-05 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-05 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the currency in your software from its list, rather than typing it.
2. Check that the e-invoice writes the three-letter code, EUR for the euro.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-05.

## Common causes

- **A name or a symbol instead of the code**, such as EURO or €.
- **A currency typed by hand** in a free field.

## Technical details

The VAT accounting currency code is BT-6. In CII, it is `ram:TaxCurrencyCode` of `ram:ApplicableHeaderTradeSettlement`; in UBL, `cbc:TaxCurrencyCode`. The list is ISO 4217's three-letter codes.

The example invoice is in US dollars and writes its VAT accounting currency `EURO`, and so the currency of its VAT total in that currency: BR-CL-03, which checks an amount's currency, fails too. The Factur-X EN 16931 profile checks the same list with its own rules `FX-SCH-A-000607` and `FX-SCH-A-000610`, which fail next to it in a Factur-X invoice.

## Official text

> Tax currency code MUST be coded using ISO code list 4217 alpha-3

BR-CL-05, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-53](../BR-53/): when the invoice names a VAT accounting currency, another one than its own, it must give its VAT total in that currency.
- [BR-CL-04](../BR-CL-04/): the invoice currency must be a three-letter ISO 4217 code, such as EUR.
- [BR-FR-CO-12](../BR-FR-CO-12/): when the invoice is not in euros, it must give the VAT accounting currency (EUR) and the VAT total in euros.
