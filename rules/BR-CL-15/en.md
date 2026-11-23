# An item's country of origin is not a country code

An item's country of origin is not a country code.

## What the rule checks

A line can give where its item comes from. Countries are written with their two-letter ISO 3166-1 code: DE for Germany, FR for France, BE for Belgium… The rule checks that this country of origin is such a code, not the country's name or another abbreviation.

## Why it matters

BR-CL-15 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-15 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the country in your software from its list, rather than typing it.
2. Check that the e-invoice writes the two-letter code, DE for Germany.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-15.

## Common causes

- **The country's name instead of its code**, such as Deutschland or France.
- **A code that is not ISO's**, such as UK for the United Kingdom, where ISO 3166-1 has GB.

## Technical details

The item country of origin is BT-159. In CII, it is `ram:ID` of `ram:OriginTradeCountry` in a line's `ram:SpecifiedTradeProduct`; in UBL, `cbc:IdentificationCode` of the item's `cac:OriginCountry`. The list is ISO 3166-1's two-letter codes.

The example invoice writes its first line's country of origin `Deutschland` instead of `DE`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000628`, which fails next to it in a Factur-X invoice.

## Official text

> Country codes in an invoice MUST be coded using ISO code list 3166-1

BR-CL-15, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-14](../BR-CL-14/): every country of the invoice's addresses must be a two-letter ISO 3166-1 code, such as DE or FR.
