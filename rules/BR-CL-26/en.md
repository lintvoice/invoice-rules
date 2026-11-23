# A delivery place identifier's kind is not a valid code

The code that says what kind of identifier the delivery place has is not in the official list.

## What the rule checks

An invoice can identify the place of delivery, a warehouse or a site, by an identifier such as a GLN or a SIRET. A four-digit code from the ISO 6523 list says which kind: 0088 for a GLN, 0009 for a SIRET. The rule checks that the code comes from that list, not a name such as "GLN".

## Why it matters

BR-CL-26 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-26 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the kind of identifier in your software from its list, rather than typing it.
2. Check that the e-invoice writes the four-digit code next to the identifier.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-26.

## Common causes

- **The register's name instead of its code**, such as GLN, SIRET or EAN.
- **A code without its leading zeros**, 88 for 0088.

## Technical details

The deliver-to location identifier is BT-71, its scheme identifier BT-71-1. In CII, it is the `schemeID` of `ram:GlobalID` in `ram:ShipToTradeParty`; in UBL, the `schemeID` of `cbc:ID` in `cac:DeliveryLocation`. The list is the ISO 6523 ICD list.

The example invoice gives a delivery place whose GLN has the scheme `GLN` instead of `0088`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000585`, which fails next to it in a Factur-X invoice.

## Official text

> Delivery location identifier scheme identifier MUST belong to the ISO 6523 ICD code list

BR-CL-26, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-10](../BR-CL-10/): the code that says which register a party's identifier comes from must be in the ISO 6523 list, such as 0088 for a GLN.
- [BR-57](../BR-57/): when the invoice gives a delivery address, it must give its country, with its two-letter code.
