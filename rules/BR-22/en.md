# A line has no quantity

A line of the invoice gives no invoiced quantity.

## What the rule checks

Each line must give the invoiced quantity: a number of items, hours, days… A flat-fee service has a quantity too: 1.

## Why it matters

BR-22 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-22 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give a quantity on each line; for a flat fee, enter 1, with the fee as the unit price.
2. Give the quantity's unit too (unit, hour, day…), which rule BR-23 requires.
3. If your software sends no quantity for flat-fee lines, report it to the software's publisher, quoting BR-22.

## Common causes

- **A flat-fee line** entered with an amount only, without quantity or unit price.
- **A heading or comment line** sent as an invoice line.

## Technical details

The invoiced quantity is BT-129, with its unit BT-130 (BR-23). In CII: `ram:SpecifiedLineTradeDelivery/ram:BilledQuantity` of each `ram:IncludedSupplyChainTradeLineItem`; in UBL: `cbc:InvoicedQuantity` of each `cac:InvoiceLine` (`cbc:CreditedQuantity` in a credit note).

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires a quantity on every line, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves the quantity optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> Each Invoice line (BG-25) shall have an Invoiced quantity (BT-129).

BR-22, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-23](../BR-23/): the quantity must give its unit.
- [BR-26](../BR-26/): each line must give its net unit price.
