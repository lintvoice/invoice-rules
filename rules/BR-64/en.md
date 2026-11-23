# An item's standard identifier does not say what kind of identifier it is

An item's standard identifier is given without the code that says what kind of identifier it is.

## What the rule checks

A line can identify its item by a standard identifier, such as the GTIN printed under a barcode. A code says which kind of identifier it is: 0160 for a GTIN, for example. The rule checks that a standard identifier always comes with this code.

## Why it matters

BR-64 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-64 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the kind of identifier in your software, if it asks.
2. Check that the e-invoice writes its code next to the value.
3. If the code is missing from the e-invoice, report it to the software's publisher, quoting BR-64.

## Common causes

- **An item's standard identifier copied as a plain value**, without its code.
- **An export that writes the value and drops its attributes.**

## Technical details

The item standard identifier is BT-157, its scheme identifier BT-157-1. In CII, the rule reads the `schemeID` of `ram:GlobalID` in a line's `ram:SpecifiedTradeProduct`; in UBL, the `schemeID` of `cbc:ID` in `cac:StandardItemIdentification`. Its codes come from the ISO 6523 ICD list, as rule BR-CL-21 requires.

The example invoice gives an item's standard identifier without its scheme. The CII syntax rule `CII-SR-046`, which asks for the same scheme, fails too. The Factur-X EN 16931 profile has its own rules, which check that the scheme is there too: in a Factur-X invoice, its rule `FX-SCH-A-000551` fails next to BR-64, as in the example invoice.

## Official text

> The Item standard identifier (BT-157) shall have a Scheme identifier.

BR-64, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-21](../BR-CL-21/): the code that says what kind of standard identifier an item has must be in the ISO 6523 list, such as 0160 for a GTIN.
- [BR-65](../BR-65/): an item's classification must say, with a standard code, what kind of classification it is.
