# An item attribute gives its value both as text and as a measure

An item attribute on a line gives its value both as text and as a measure, or gives none.

## What the rule checks

A line can describe the item by attributes, for example "Duration: 2 days". Each attribute gives its value in one of two ways: as text ("2 days"), or as a quantity with its unit of measure (2, in days). The rule checks that each attribute gives exactly one of the two, and that a measure has its unit.

## Why it matters

BR-FR-28 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. In your software's item records, give each attribute's value once: as text, or as a quantity with its unit.
2. Check that an attribute given as a quantity has its unit of measure.
3. If your software sends both forms by itself, report it to the software's publisher, quoting BR-FR-28.

## Common causes

- **An attribute entered twice** in the item record, once as text and once as a quantity.
- **A quantity without its unit of measure.**
- **An attribute with no value**, left empty in the item record.

## Technical details

Item attributes form group BG-32: name BT-160 (`ram:Description`), value BT-161 (`ram:Value`) and, in the EXTENDED profiles, a value as a measure EXT-FR-FE-160 (`ram:ValueMeasure`) with its unit EXT-FR-FE-161 (`@unitCode`). In UBL, the rule reads `cbc:Value` and `cbc:ValueQuantity` of each `cac:AdditionalItemProperty`.

The Factur-X schema of the EN 16931 profile requires a `ram:Value` and has no `ram:ValueMeasure`, so in CII only an invoice of an EXTENDED profile can fail this rule. The example invoice, an EXTENDED-CTC-FR one, also fails that profile's rule BR-FREXT-54-2, which says the same.

## Official text

> La valeur d’attribut (ram:Value) ou la valeur (ram:ValueMeasure avec unité de mesure) doivent être présents, mais pas les deux

BR-FR-28, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-28-Value`.

## Related rules

- [BR-FR-27](../BR-FR-27/): an item attribute must have a name or a code.
