# The seller's electronic address does not say what kind of address it is

The seller's electronic address is given without the code that says what kind of address it is.

## What the rule checks

An e-invoice can give the electronic address where the seller receives e-invoices: an e-mail address, a routing number on a network such as Peppol, an address on a national platform… A code says what kind of address it is, so the sending software knows where to deliver. The rule checks that the seller's address gives this code.

## Why it matters

BR-62 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-62 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the kind of address in your software, if it asks.
2. Check that the e-invoice writes its code next to the value.
3. If the code is missing from the e-invoice, report it to the software's publisher, quoting BR-62.

## Common causes

- **The seller's electronic address copied as a plain value**, without its code.
- **An export that writes the value and drops its attributes.**

## Technical details

The seller electronic address is BT-34, its scheme identifier BT-34-1. In CII, the rule reads the `schemeID` of `ram:URIID` in the seller's `ram:URIUniversalCommunication`; in UBL, the `schemeID` of the seller's `cbc:EndpointID`. Its codes come from the EAS list, as rule BR-CL-25 requires: `EM` for an e-mail address, `0088` for a GLN, `0225` for an address of the French reform's platforms…

The example invoice gives the seller's electronic address without its scheme. The Factur-X EN 16931 profile has its own rules, which check that the scheme is there too: in a Factur-X invoice, its rule `FX-SCH-A-000446` fails next to BR-62, as in the example invoice.

## Official text

> The Seller electronic address (BT-34) shall have a Scheme identifier.

BR-62, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-63](../BR-63/): the buyer's electronic address must say, with a standard code, what kind of address it is.
- [BR-CL-25](../BR-CL-25/): the code that says what kind of electronic address a party has must be in the EAS list, such as EM for an e-mail address.
- [BR-FR-21](../BR-FR-21/): on a business-to-business invoice, the buyer's electronic address must start with the buyer's SIREN and be declared as a French reform address.
