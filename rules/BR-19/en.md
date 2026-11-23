# The tax representative has no postal address

The invoice names a tax representative of the seller, without its postal address.

## What the rule checks

Some sellers act through a tax representative, a company that handles their VAT in a country where they are not established. When the invoice names one, the rule checks that it gives the representative's postal address.

## Why it matters

BR-19 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-19 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the tax representative's postal address in your software, country included.
2. Check that the e-invoice gives the representative's name, postal address with its country, and VAT number.
3. If they are missing from the e-invoice, report it to the software's publisher, quoting BR-19.

## Common causes

- **A representative entered with its name only.**
- **A representative entered with its VAT number only**, its other details left in another tool.

## Technical details

The tax representative's postal address is group BG-12. In CII, the rule looks for `ram:PostalTradeAddress` in `ram:SellerTaxRepresentativeTradeParty`; in UBL, for `cac:PostalAddress` in `cac:TaxRepresentativeParty`.

The example invoice names a tax representative without an address. Without an address there is no country code either, so BR-20 fails too. The Factur-X EN 16931 profile has its own rules, which check that the address is there too: in a Factur-X invoice, its rule `FX-SCH-A-000432` fails next to BR-19, as in the example invoice.

## Official text

> The Seller tax representative postal address (BG-12) shall be provided in the Invoice, if the Seller (BG-4) has a Seller tax representative party (BG-11).

BR-19, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-18](../BR-18/): when the seller has a tax representative, the invoice must give its name.
- [BR-20](../BR-20/): when the seller has a tax representative, its postal address must give its country, with its two-letter code.
- [BR-56](../BR-56/): when the seller has a tax representative, the invoice must give the representative's VAT number.
