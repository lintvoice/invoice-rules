# An item identifier's kind is not a valid code

The code that says what kind of standard identifier an item has is not in the official list.

## What the rule checks

A line can identify its item by a standard identifier, such as the GTIN printed under a barcode. A four-digit code from the ISO 6523 list says which kind: 0160 for a GTIN. The rule checks that the code comes from that list, not a name such as "EAN".

## Why it matters

BR-CL-21 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-21 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the kind of identifier in your software from its list.
2. Check that the e-invoice writes 0160 next to a GTIN.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-21.

## Common causes

- **The barcode's name instead of the code**, such as EAN or GTIN.
- **A code without its leading zero**, 160 for 0160.

## Technical details

The item standard identifier is BT-157, its scheme identifier BT-157-1. In CII, it is the `schemeID` of `ram:GlobalID` in a line's `ram:SpecifiedTradeProduct`; in UBL, the `schemeID` of `cbc:ID` in `cac:StandardItemIdentification`. The list is the ISO 6523 ICD list.

The example invoice gives its first line's item a GTIN with the scheme `EAN` instead of `0160`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000626`, which fails next to it in a Factur-X invoice.

## Official text

> Item standard identifier scheme identifier MUST belong to the ISO 6523 ICD code list

BR-CL-21, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-64](../BR-64/): an item's standard identifier must say, with a standard code, what kind of identifier it is.
- [BR-CL-10](../BR-CL-10/): the code that says which register a party's identifier comes from must be in the ISO 6523 list, such as 0088 for a GLN.
