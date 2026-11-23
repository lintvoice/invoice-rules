# The amount due is missing

The invoice does not give the amount due.

## What the rule checks

The amount due is what the buyer still has to pay: the total with VAT, minus any amount already paid, plus any rounding. The e-invoice gives it in its totals, and the rule checks that it is there.

## Why it matters

BR-15 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-15 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check that your software computes this total for every invoice, even when it equals another one.
2. Check that the e-invoice writes it, not only the PDF.
3. If it is missing from the e-invoice, report it to the software's publisher, quoting BR-15.

## Common causes

- **A total left out because it equals another one**, the total without VAT of an invoice without allowances or charges for example.
- **An export that writes only some of the totals.**

## Technical details

The amount due is BT-115, in group BG-22. In CII, it is `ram:DuePayableAmount` of `ram:SpecifiedTradeSettlementHeaderMonetarySummation`; in UBL, `cbc:PayableAmount` of `cac:LegalMonetaryTotal`.

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires the amount due, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves it optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> An Invoice shall have the Amount due for payment (BT-115).

BR-15, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-16](../BR-CO-16/): the amount due must be exactly the total with VAT, minus the amount already paid, plus any rounding.
- [BR-14](../BR-14/): every invoice must give the total with vat.
