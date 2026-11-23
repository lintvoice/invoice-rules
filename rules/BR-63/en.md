# The buyer's electronic address does not say what kind of address it is

The buyer's electronic address is given without the code that says what kind of address it is.

## What the rule checks

An e-invoice can give the electronic address where the buyer receives e-invoices: an e-mail address, a routing number on a network such as Peppol, an address on a national platform… A code says what kind of address it is, so the sending software knows where to deliver. The rule checks that the buyer's address gives this code.

## Why it matters

BR-63 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-63 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the kind of address in your software, if it asks.
2. Check that the e-invoice writes its code next to the value.
3. If the code is missing from the e-invoice, report it to the software's publisher, quoting BR-63.

## Common causes

- **The buyer's electronic address copied as a plain value**, without its code.
- **An export that writes the value and drops its attributes.**

## Technical details

The buyer electronic address is BT-49, its scheme identifier BT-49-1. In CII, the rule reads the `schemeID` of `ram:URIID` in the buyer's `ram:URIUniversalCommunication`; in UBL, the `schemeID` of the buyer's `cbc:EndpointID`. Its codes come from the EAS list, as rule BR-CL-25 requires for the seller's.

The example invoice gives the buyer's electronic address without its scheme. The Factur-X EN 16931 profile has its own rules, which check that the scheme is there too: in a Factur-X invoice, its rule `FX-SCH-A-000428` fails next to BR-63, as in the example invoice.

## Official text

> The Buyer electronic address (BT-49) shall have a Scheme identifier.

BR-63, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-62](../BR-62/): the seller's electronic address must say, with a standard code, what kind of address it is.
- [BR-CL-25](../BR-CL-25/): the code that says what kind of electronic address a party has must be in the EAS list, such as EM for an e-mail address.
- [BR-FR-22](../BR-FR-22/): on a self-billed business-to-business invoice, the seller's electronic address must start with the seller's SIREN and be declared as a French reform address.
