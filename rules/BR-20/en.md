# The tax representative's address has no country

The country of the tax representative's address is empty.

## What the rule checks

Some sellers act through a tax representative, a company that handles their VAT in a country where they are not established. When the invoice names one, the rule checks that the representative's address gives its country, as a two-letter code such as DE or FR.

## Why it matters

BR-20 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-20 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the country of the tax representative's address in your software.
2. Check that the e-invoice gives the representative's name, postal address with its country, and VAT number.
3. If they are missing from the e-invoice, report it to the software's publisher, quoting BR-20.

## Common causes

- **An address entered without a country.**
- **A representative entered with its VAT number only**, its other details left in another tool.

## Technical details

The country code of the tax representative's address is BT-69. In CII, it is `ram:CountryID` of `ram:PostalTradeAddress` in `ram:SellerTaxRepresentativeTradeParty`; in UBL, `cbc:IdentificationCode` of the address's `cac:Country`. Its code comes from ISO 3166-1, as rule BR-CL-14 requires.

The example invoice leaves the country code empty. An empty code is not in ISO 3166-1, so BR-CL-14 fails too, and the example fails both rules. The Factur-X profile's own check of country codes reads only a code that is there.

## Official text

> The Seller tax representative postal address (BG-12) shall contain a Tax representative country code (BT-69), if the Seller (BG-4) has a Seller tax representative party (BG-11).

BR-20, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-19](../BR-19/): when the seller has a tax representative, the invoice must give its postal address.
- [BR-CL-14](../BR-CL-14/): every country of the invoice's addresses must be a two-letter ISO 3166-1 code, such as DE or FR.
- [BR-56](../BR-56/): when the seller has a tax representative, the invoice must give the representative's VAT number.
