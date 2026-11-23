# The buyer has no postal address

The invoice gives no postal address for the buyer.

## What the rule checks

An invoice gives the buyer's postal address. In an e-invoice, the address is a block of fields: street, city, post code, country… The rule checks that the block is there; another rule, BR-11, checks that it gives at least the country.

## Why it matters

BR-10 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-10 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the buyer's full address in your software, country included.
2. Check that the address printed on the PDF is also in the e-invoice.
3. If the address is missing from the e-invoice, report it to the software's publisher, quoting BR-10.

## Common causes

- **An address printed on the PDF** but not written in the e-invoice data.
- **A customer record without an address**, for a client known only by e-mail.

## Technical details

The buyer's postal address is group BG-8. In CII, the rule looks for `ram:PostalTradeAddress` in `ram:BuyerTradeParty`; in UBL, for `cac:PostalAddress` of the party.

The example invoice has no address for the buyer. Without an address there is no country code either, so BR-11 fails too. The Factur-X EN 16931 profile has its own rules, which check that the address is there too: in a Factur-X invoice, its rule `FX-SCH-A-000419` fails next to BR-10, as in the example invoice.

## Official text

> An Invoice shall contain the Buyer postal address (BG-8).

BR-10, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-11](../BR-11/): the buyer's postal address must give its country, with its two-letter code such as DE or FR.
- [BR-07](../BR-07/): every invoice must give the buyer's name.
- [BR-08](../BR-08/): every invoice must give the seller's postal address, with at least its country.
