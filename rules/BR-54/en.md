# An item attribute lacks its name or its value

An item attribute gives its name without its value, or its value without its name.

## What the rule checks

A line can describe its item with attributes, each a name and a value: "Colour: blue", "Size: M". The rule checks that each attribute has both.

## Why it matters

BR-54 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-54 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in both the name and the value of each item attribute in your software.
2. Remove the attributes left empty.
3. If the e-invoice still lacks one of them, report it to the software's publisher, quoting BR-54.

## Common causes

- **An attribute field left empty** in the item's record.
- **An attribute written as one text**, "blue", without its name.

## Technical details

An item attribute is group BG-32, with its name BT-160 and its value BT-161. In CII, the rule reads `ram:Description` and `ram:Value` of each `ram:ApplicableProductCharacteristic` of a line's `ram:SpecifiedTradeProduct`; in UBL, `cbc:Name` and `cbc:Value` of each `cac:AdditionalItemProperty`.

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires both the name and the value of each item attribute, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves it optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> Each Item attribute (BG-32) shall contain an Item attribute name (BT-160) and an Item attribute value (BT-161).

BR-54, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-FR-27](../BR-FR-27/): each item attribute must have a name or a code, and neither may be empty.
- [BR-25](../BR-25/): each invoice line must name what it invoices.
