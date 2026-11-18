# The invoice has no line

The invoice has no line.

## What the rule checks

Every invoice must have at least one line: what is sold, its quantity, its price and its amount. This holds for a credit note and for an invoice of a lump sum too: a single line will then do, with that amount and its reason.

## Why it matters

BR-16 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-16 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. For a credit note or a goodwill gesture of a lump sum, create a single line with the amount, the reason and the VAT rate that applies.
2. Check that the lines entered in your software are sent in the e-invoice, not only printed on the PDF.
3. If your software produces invoices or credit notes without lines, report it to the software's publisher, quoting BR-16.

## Common causes

- **A credit note entered as an amount to refund**, without a line.
- **An invoice created from a total**, without the detail of what is invoiced.
- **Lines printed on the PDF** but missing from the e-invoice data.

## Technical details

An invoice line is group BG-25. In CII, the rule looks for at least one `ram:IncludedSupplyChainTradeLineItem` in the document; in UBL, for at least one `cac:InvoiceLine` (`cac:CreditNoteLine` in a credit note).

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires at least one line, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves the lines optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> An Invoice shall have at least one Invoice line (BG-25).

BR-16, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-22](../BR-22/): each line must give a quantity.
- [BR-26](../BR-26/): each line must give its net unit price.
