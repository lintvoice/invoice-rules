# The seller's address has no country

The country of the seller's address is empty.

## What the rule checks

An e-invoice gives each address's country as a two-letter code: DE for Germany, FR for France, BE for Belgium… The country tells which rules and which VAT apply, so the software that receives the invoice needs it. The rule checks that the seller's address gives it.

## Why it matters

BR-09 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-09 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the country of the seller's address in your software.
2. Check that the e-invoice writes its two-letter code, not the country's name.
3. If the country stays empty, report it to the software's publisher, quoting BR-09.

## Common causes

- **An address entered without a country**, because the business only works in its own country.
- **A country field left blank** in a record imported from another tool.

## Technical details

The country code of the seller's address is BT-40. In CII, it is `ram:CountryID` of `ram:PostalTradeAddress` in `ram:SellerTradeParty`; in UBL, `cbc:IdentificationCode` of the address's `cac:Country`. Its code comes from ISO 3166-1, as rule BR-CL-14 requires.

The example invoice leaves the country code empty. An empty code is not in ISO 3166-1, so BR-CL-14 fails too, and the example fails both rules. The Factur-X profile's own check of country codes reads only a code that is there.

## Official text

> The Seller postal address (BG-5) shall contain a Seller country code (BT-40).

BR-09, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-08](../BR-08/): every invoice must give the seller's postal address, with at least its country.
- [BR-CL-14](../BR-CL-14/): every country of the invoice's addresses must be a two-letter ISO 3166-1 code, such as DE or FR.
- [BR-11](../BR-11/): the buyer's postal address must give its country, with its two-letter code such as DE or FR.
