# An amount's currency is not a valid code

The currency of an amount is not a currency code.

## What the rule checks

Currencies are written with their three-letter ISO 4217 code: EUR for the euro, USD for the US dollar, CHF for the Swiss franc… The rule checks that the currency written next to an amount is such a code, not a name, a symbol or another abbreviation.

## Why it matters

BR-CL-03 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-03 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the currency in your software from its list, rather than typing it.
2. Check that the e-invoice writes the three-letter code, EUR for the euro.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-03.

## Common causes

- **A name or a symbol instead of the code**, such as EURO or €.
- **A currency typed by hand** in a free field.

## Technical details

In CII, only the VAT total, `ram:TaxTotalAmount`, carries its currency, in its `currencyID` attribute: the VAT total in the invoice currency (BT-110) and, when there is one, in the VAT accounting currency (BT-111). In UBL, every amount carries a `currencyID`. The list is ISO 4217's three-letter codes.

The example invoice writes its currency `EURO` everywhere: in the invoice currency, so BR-CL-04 fails too, and in the VAT total's currency. The Factur-X EN 16931 profile checks the same list with its own rules `FX-SCH-A-000595` and `FX-SCH-A-000606`, which fail next to it in a Factur-X invoice.

## Official text

> currencyID MUST be coded using ISO code list 4217 alpha-3

BR-CL-03, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-04](../BR-CL-04/): the invoice currency must be a three-letter ISO 4217 code, such as EUR.
- [BR-CL-05](../BR-CL-05/): the currency in which the seller accounts for VAT must be a three-letter ISO 4217 code, such as EUR.
- [BR-05](../BR-05/): every invoice must give its currency, with its three-letter code such as EUR.
