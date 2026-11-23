# The tax representative has no VAT number

The invoice names a tax representative of the seller, without its VAT number.

## What the rule checks

Some sellers act through a tax representative, a company that handles their VAT in a country where they are not established. Its VAT number is what the invoice uses for the VAT. When the invoice names a representative, the rule checks that it gives this number.

## Why it matters

BR-56 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-56 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the tax representative's VAT number in your software.
2. Check that the e-invoice writes it as a VAT number, starting with its country code.
3. If it is missing from the e-invoice, report it to the software's publisher, quoting BR-56.

## Common causes

- **A representative entered with its name and address only.**
- **Another tax number given instead**, a national tax number for example.

## Technical details

The seller tax representative's VAT identifier is BT-63. In CII, the rule reads `ram:ID` with `schemeID="VA"` of `ram:SpecifiedTaxRegistration` in `ram:SellerTaxRepresentativeTradeParty`; in UBL, `cbc:CompanyID` of the representative's `cac:PartyTaxScheme`.

The example invoice names a tax representative without a VAT number. The Factur-X EN 16931 profile has its own rules, which check that the number is there too: in a Factur-X invoice, its rule `FX-SCH-A-000169` fails next to BR-56, as in the example invoice.

## Official text

> Each Seller tax representative party (BG-11) shall have a Seller tax representative VAT identifier (BT-63).

BR-56, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-18](../BR-18/): when the seller has a tax representative, the invoice must give its name.
- [BR-19](../BR-19/): when the seller has a tax representative, the invoice must give its postal address.
- [BR-CO-09](../BR-CO-09/): a VAT identification number starts with the two-letter code of its country, FR for France.
