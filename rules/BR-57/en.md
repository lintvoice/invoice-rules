# The delivery address has no country

The country of the delivery address is empty.

## What the rule checks

An invoice can give the address where the goods were delivered or the service done, when it differs from the buyer's. The country of the delivery can change the VAT that applies. When the invoice gives a delivery address, the rule checks that it gives its country, as a two-letter code such as DE or FR.

## Why it matters

BR-57 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-57 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the country of each delivery address in your software.
2. Check that the e-invoice writes its two-letter code, not the country's name.
3. If the country stays empty, report it to the software's publisher, quoting BR-57.

## Common causes

- **A delivery address entered without a country**, as a free text.
- **A delivery site imported from another tool** without its country.

## Technical details

The deliver-to address is group BG-15, its country code BT-80. In CII, it is `ram:CountryID` of `ram:PostalTradeAddress` in `ram:ShipToTradeParty`; in UBL, `cbc:IdentificationCode` of the `cac:Country` of `cac:Address` in `cac:DeliveryLocation`. Its code comes from ISO 3166-1, as rule BR-CL-14 requires.

The example invoice gives a delivery address whose country code is empty. An empty code is not in ISO 3166-1, so BR-CL-14 fails too, and the example fails both rules. The Factur-X profile's own check of country codes reads only a code that is there.

## Official text

> Each Deliver to address (BG-15) shall contain a Deliver to country code (BT-80).

BR-57, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-14](../BR-CL-14/): every country of the invoice's addresses must be a two-letter ISO 3166-1 code, such as DE or FR.
- [BR-09](../BR-09/): the seller's postal address must give its country, with its two-letter code such as DE or FR.
- [BR-11](../BR-11/): the buyer's postal address must give its country, with its two-letter code such as DE or FR.
