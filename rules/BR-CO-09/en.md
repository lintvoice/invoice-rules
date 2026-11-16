# A VAT number does not start with a country code

A VAT number on the invoice does not start with the code of the country that issued it.

## What the rule checks

The rule looks at the invoice's VAT identification numbers: the seller's, the seller's tax representative's if there is one, and the buyer's. Each must start with the two letters of the country that issued it, for example FR for France or DE for Germany.

## Why it matters

BR-CO-09 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-09 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check the VAT number in your company's record and in your customer's: it starts with the country's two letters, then the number.
2. Put no space or other character before these two letters.
3. Do not give a SIREN or SIRET instead of the VAT number.
4. If the number is right in your software but not in the e-invoice, report it to the software's publisher, quoting BR-CO-09.

## Common causes

- **The number entered without its country prefix**, digits only.
- **A SIREN or SIRET given instead of the VAT number.**
- **A space or another character before the number**, since the rule reads its first two characters.
- **A Greek number written with EL** (see the technical details).

## Technical details

The numbers checked are the seller's (BT-31), the seller's tax representative's (BT-63) and the buyer's (BT-48). The rule compares their first two characters with a list of ISO 3166-1 alpha-2 country codes, plus 1A and XI. In CII, it reads each `ram:SpecifiedTaxRegistration/ram:ID` whose `schemeID` is `VA`; in UBL, `cac:PartyTaxScheme/cbc:CompanyID` when the tax scheme is `VAT`.

The official message allows the prefix EL for Greece, but the list in the 1.3.17 files does not include it: a number starting with EL fails BR-CO-09 there, and GR passes. We checked it on the valid example invoice, with the seller's number replaced by EL123456789.

## Official text

> The Seller VAT identifier (BT-31), the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48) shall have a prefix in accordance with ISO code ISO 3166-1 alpha-2 by which the country of issue may be identified. Nevertheless, Greece may use the prefix ‘EL’.

BR-CO-09, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-26](../BR-CO-26/): the seller must have at least one identifier: an identifier, a registration number or a VAT number.
