# A country is not written as a country code

A country of the invoice is not a country code.

## What the rule checks

Countries are written with their two-letter ISO 3166-1 code: DE for Germany, FR for France, BE for Belgium… The rule checks that the country of every address of the invoice is such a code, not the country's name or another abbreviation.

## Why it matters

BR-CL-14 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-14 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the country in your software from its list, rather than typing it.
2. Check that the e-invoice writes the two-letter code, DE for Germany.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-14.

## Common causes

- **The country's name instead of its code**, such as Deutschland or France.
- **A code that is not ISO's**, such as UK for the United Kingdom, where ISO 3166-1 has GB.

## Technical details

The rule reads every country code of an address: the seller's (BT-40), the buyer's (BT-55), the tax representative's (BT-69) and the deliver-to address's (BT-80). In CII, it is each `ram:CountryID`; in UBL, `cbc:IdentificationCode` of each `cac:Country`. The list is ISO 3166-1's two-letter codes. An item's country of origin has its own rule, BR-CL-15.

The example invoice writes the buyer's country `Deutschland` instead of `DE`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000568`, which fails next to it in a Factur-X invoice.

## Official text

> Country codes in an invoice MUST be coded using ISO code list 3166-1

BR-CL-14, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-09](../BR-09/): the seller's postal address must give its country, with its two-letter code such as DE or FR.
- [BR-11](../BR-11/): the buyer's postal address must give its country, with its two-letter code such as DE or FR.
- [BR-57](../BR-57/): when the invoice gives a delivery address, it must give its country, with its two-letter code.
- [BR-CL-15](../BR-CL-15/): an item's country of origin must be a two-letter ISO 3166-1 code, such as DE or FR.
