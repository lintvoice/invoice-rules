# An item's classification system is not a valid code

The code that says which classification system an item's class comes from is not in the official list.

## What the rule checks

A line can classify its item in a classification system, such as UNSPSC or the EU's Common Procurement Vocabulary (CPV). A code from the official list says which system: TST for UNSPSC, STI for CPV. The rule checks that the code comes from that list, not the system's name.

## Why it matters

BR-CL-13 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-13 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the classification system in your software from its list.
2. Check that the e-invoice writes its code, TST for UNSPSC or STI for CPV.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-13.

## Common causes

- **The system's name instead of its code**, such as UNSPSC or CPV.
- **A code invented for an internal catalogue.**

## Technical details

The item classification identifier is BT-158, its scheme identifier BT-158-1. In CII, it is the `listID` of `ram:ClassCode` in a line's `ram:DesignatedProductClassification`; in UBL, the `listID` of `cbc:ItemClassificationCode`. The list is part of UNTDID 7143.

The example invoice classifies its first line's item under UNSPSC 86101700, non scientific vocational training services, with the scheme written `UNSPSC` instead of `TST`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000297`, which fails next to it in a Factur-X invoice.

## Official text

> Item classification identifier identification scheme identifier MUST be coded using one of the UNTDID 7143 list.

BR-CL-13, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-65](../BR-65/): an item's classification must say, with a standard code, what kind of classification it is.
- [BR-CL-21](../BR-CL-21/): the code that says what kind of standard identifier an item has must be in the ISO 6523 list, such as 0160 for a GTIN.
