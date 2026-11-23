# A company identifier's kind is not a valid code

The code that says which register an identifier comes from is not in the official list.

## What the rule checks

Identifiers come from many registers: a GLN, a SIRET, a DUNS number… A four-digit code from the ISO 6523 list says which register an identifier comes from: 0088 for a GLN, 0009 for a SIRET, 0002 for a SIREN. The rule checks that the identifier of the seller, the buyer or the payee uses such a code, not the register's name.

## Why it matters

BR-CL-10 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-10 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the kind of identifier in your software from its list, rather than typing it.
2. Check that the e-invoice writes the four-digit code next to the identifier.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-10.

## Common causes

- **The register's name instead of its code**, such as GLN, SIRET or EAN.
- **A code without its leading zeros**, 88 for 0088.

## Technical details

The rule reads the scheme of the seller identifier (BT-29-1), the buyer identifier (BT-46-1) and the payee identifier (BT-60-1). In CII, it is the `schemeID` of each `ram:GlobalID`, except those of an item and of the deliver-to place, which BR-CL-21 and BR-CL-26 check; in UBL, the `schemeID` of `cbc:ID` in each `cac:PartyIdentification`. The list is the ISO 6523 ICD list.

The example invoice writes the scheme of the seller's GLN `GLN` instead of `0088`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000579`, which fails next to it in a Factur-X invoice.

## Official text

> Any identifier identification scheme identifier MUST be coded using one of the ISO 6523 ICD list.

BR-CL-10, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-11](../BR-CL-11/): when a party's legal registration number gives the register it comes from, the code must be in the ISO 6523 list, such as 0002 for a SIREN.
- [BR-CL-21](../BR-CL-21/): the code that says what kind of standard identifier an item has must be in the ISO 6523 list, such as 0160 for a GTIN.
- [BR-CL-26](../BR-CL-26/): the code that says what kind of identifier the delivery place has must be in the ISO 6523 list, such as 0088 for a GLN.
- [BR-FR-CO-10](../BR-FR-CO-10/): each identifier of a party must state its type (SIRET, GLN…), and a party cannot have two identifiers of the same type.
