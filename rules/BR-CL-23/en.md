# A unit of measure is not a valid code

A unit of measure of the invoice is not a code from the official list.

## What the rule checks

An e-invoice writes each unit of measure as a code from a United Nations list: C62 for one unit, H87 for a piece, HUR for an hour, DAY for a day, KGM for a kilogram… The rule checks that each unit is a code from that list, not an abbreviation such as "pcs".

## Why it matters

BR-CL-23 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-23 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Map each unit of your software to its code in the list: "unit" to C62, "hour" to HUR.
2. Check that the e-invoice writes the code, not the unit's short name.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-23.

## Common causes

- **A local abbreviation instead of the code**, such as Stk, pcs or U.
- **A unit created in the catalogue** with no code mapped to it.

## Technical details

The invoiced quantity's unit of measure is BT-130, the price base quantity's BT-150. In CII, it is the `unitCode` of `ram:BilledQuantity` and of `ram:BasisQuantity`; in UBL, the `unitCode` of `cbc:InvoicedQuantity` (`cbc:CreditedQuantity` in a credit note) and of `cbc:BaseQuantity`. The list is UN/ECE Recommendation 20, with Recommendation 21's extension.

The example invoice gives its first line the unit `Stk`, a German abbreviation for a piece, instead of `C62`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000613`, which fails next to it in a Factur-X invoice.

## Official text

> Unit code MUST be coded according to the UN/ECE Recommendation 20 with Rec 21 extension

BR-CL-23, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-23](../BR-23/): each invoiced quantity must give its unit of measure (unit, hour, day…), as a standard code.
