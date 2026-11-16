# An item attribute has neither a name nor a code

An item attribute on a line has an empty name, an empty code, or neither.

## What the rule checks

A line may describe the item with attributes, such as "Colour: blue". Each attribute must have a name ("Colour") or a code, and the name or code given must not be empty.

## Why it matters

BR-FR-27 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check the item attributes in your software's product records.
2. Give each attribute a name, or delete the attributes left empty.
3. If your software sends empty attributes on its own, report it to the software's publisher, quoting BR-FR-27.

## Common causes

- **An attribute with a value but no name.**
- **An empty attribute** left in a product record.

## Technical details

Item attributes are group BG-32: name BT-160 (`ram:Description`) and the French extension's code EXT-FR-FE-159 (`ram:TypeCode`), under `ram:ApplicableProductCharacteristic` in CII.

## Official text

> Le groupe Attribut d’article (BG-32) doit contenir soit un nom d’attribut d’article (BT-160 : ram:Description), soit un code d’attribut d’article (EXT-FR-FE-159 : ram:TypeCode).

BR-FR-27, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-27_BG-32`, `BR-FR-27_BT-160`, `BR-FR-27_EXT-FR-FE-159`.

## Related rules

No closely related rule.
