# The total without VAT is missing

The invoice does not give the total without VAT.

## What the rule checks

The total without VAT is the total of the lines, minus the allowances and plus the charges on the whole invoice. The e-invoice gives it in its totals, and the rule checks that it is there.

## Why it matters

BR-13 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-13 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check that your software computes this amount for every invoice, even when it equals another one.
2. Check that the e-invoice writes it, not only the PDF.
3. If it is missing from the e-invoice, report it to the software's publisher, quoting BR-13.

## Common causes

- **An amount left out because it equals another one**, for example the total without VAT of an invoice without allowances or charges on the whole invoice, equal to its total of the lines.
- **An export that writes only some of the totals.**

## Technical details

The total without VAT is BT-109, in group BG-22. In CII, it is `ram:TaxBasisTotalAmount` of `ram:SpecifiedTradeSettlementHeaderMonetarySummation`; in UBL, `cbc:TaxExclusiveAmount` of `cac:LegalMonetaryTotal`.

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires the total without VAT, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves it optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> An Invoice shall have the Invoice total amount without VAT (BT-109).

BR-13, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-13](../BR-CO-13/): the total without VAT must be exactly the sum of the lines, minus the invoice's allowances, plus its charges, to the cent.
- [BR-12](../BR-12/): every invoice must give the total of the lines.
- [BR-14](../BR-14/): every invoice must give the total with VAT.
