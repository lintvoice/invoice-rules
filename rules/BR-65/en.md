# An item's classification does not say what kind of classification it is

An item's classification is given without the code that says what kind of classification it is.

## What the rule checks

A line can classify its item in a classification system, such as UNSPSC or the EU's Common Procurement Vocabulary (CPV). A code says which system the classification comes from: TST for UNSPSC, STI for CPV. The rule checks that a classification always comes with this code.

## Why it matters

BR-65 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-65 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the kind of classification in your software, if it asks.
2. Check that the e-invoice writes its code next to the value.
3. If the code is missing from the e-invoice, report it to the software's publisher, quoting BR-65.

## Common causes

- **An item's classification copied as a plain value**, without its code.
- **An export that writes the value and drops its attributes.**

## Technical details

The item classification identifier is BT-158, its scheme identifier BT-158-1. In CII, the rule reads the `listID` of `ram:ClassCode` in a line's `ram:DesignatedProductClassification`; in UBL, the `listID` of `cbc:ItemClassificationCode` in `cac:CommodityClassification`. Its codes come from the UNTDID 7143 list, as rule BR-CL-13 requires.

The example invoice gives an item's classification without its scheme. The Factur-X EN 16931 profile has its own rules, which check that the scheme is there too: in a Factur-X invoice, its rule `FX-SCH-A-000296` fails next to BR-65, as in the example invoice.

## Official text

> The Item classification identifier (BT-158) shall have a Scheme identifier.

BR-65, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-13](../BR-CL-13/): the code that says which classification system an item's class comes from must be in the official list, such as TST for UNSPSC.
- [BR-64](../BR-64/): an item's standard identifier must say, with a standard code, what kind of identifier it is.
