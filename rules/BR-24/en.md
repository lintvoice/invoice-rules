# A line has no net amount

A line of the invoice gives no net amount.

## What the rule checks

Each line of an invoice has a net amount: the quantity times the price, minus the line's allowances and plus its charges, without VAT. The rule checks that each line gives it.

## Why it matters

BR-24 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-24 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check that each line of the invoice has its amount in your software, the free-text lines included.
2. For a line that is only a comment, write it as a note rather than as a line.
3. If a line has no amount in the e-invoice, report it to the software's publisher, quoting BR-24.

## Common causes

- **A comment typed as a line**, without an amount.
- **A title line** that groups the next ones.

## Technical details

The invoice line net amount is BT-131. In CII, it is `ram:LineTotalAmount` of the line's `ram:SpecifiedTradeSettlementLineMonetarySummation`; in UBL, `cbc:LineExtensionAmount` of `cac:InvoiceLine`.

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires each line's net amount, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves it optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> Each Invoice line (BG-25) shall have an Invoice line net amount (BT-131).

BR-24, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-10](../BR-CO-10/): the sum of line net amounts must be exactly the total of each line's net amount, to the cent.
- [BR-16](../BR-16/): every invoice must have at least one line, credit notes included: for a lump sum, a single line will do.
- [BR-26](../BR-26/): each line must give its net unit price; for a flat fee of quantity 1, it is the line's amount.
