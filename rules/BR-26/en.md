# A line has no net unit price

A line of the invoice gives no net unit price.

## What the rule checks

Each line must give its net unit price: the price of one unit, without VAT, after any discount on the price. For a flat-fee service of quantity 1, this price is the fee.

## Why it matters

BR-26 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-26 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give a unit price on each line; for a flat fee, enter a quantity of 1 and the fee as the price.
2. Check that the line amount is the quantity times the price, the line's allowances and charges included.
3. If your software sends no unit price, report it to the software's publisher, quoting BR-26.

## Common causes

- **A flat-fee line** entered with an amount only.
- **A unit price printed on the PDF** but missing from the e-invoice data.

## Technical details

The net unit price is BT-146. In CII: `ram:NetPriceProductTradePrice/ram:ChargeAmount` in `ram:SpecifiedLineTradeAgreement`; in UBL: `cac:Price/cbc:PriceAmount` of each `cac:InvoiceLine`. The gross price (BT-148) and the price discount (BT-147) are optional: the net price is the gross price minus that discount.

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires a net price on every line, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves the net price optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> Each Invoice line (BG-25) shall contain the Item net price (BT-146).

BR-26, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-27](../BR-27/): the net unit price cannot be negative.
- [BR-22](../BR-22/): each line must give a quantity.
