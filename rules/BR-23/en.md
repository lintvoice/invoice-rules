# A line's quantity has no unit

A line's invoiced quantity gives no unit of measure.

## What the rule checks

Each invoiced quantity must come with its unit of measure: unit, hour, day, kilogram… The e-invoice does not spell it out but uses a standard code, which your software picks from the unit you select.

## Why it matters

BR-23 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-23 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose a unit for each item or service in your software, for example "unit", "hour" or "day".
2. For a flat-fee service, choose the unit "unit".
3. If the unit is chosen but missing from the e-invoice, report it to the software's publisher, quoting BR-23.

## Common causes

- **A flat-fee line** without a unit.
- **A unit typed as free text** ("flat fee", "lot") that the software does not turn into a code.
- **An item created without a unit** in the software's catalogue.

## Technical details

The unit is BT-130, an attribute of the quantity BT-129: `unitCode` of `ram:BilledQuantity` in CII, of `cbc:InvoicedQuantity` (or `cbc:CreditedQuantity`) in UBL. The code comes from UN/ECE Recommendations 20 and 21, as rule BR-CL-23 requires: for example `C62` (unit), `HUR` (hour), `DAY` (day), `KGM` (kilogram).

The Factur-X XML schema leaves this attribute optional: BR-23 makes it mandatory. The example invoice removes the unit from its first line's quantity.

## Official text

> An Invoice line (BG-25) shall have an Invoiced quantity unit of measure code (BT-130).

BR-23, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-22](../BR-22/): each line must give a quantity.
