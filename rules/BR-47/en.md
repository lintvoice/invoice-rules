# A VAT rate has no VAT category

A VAT breakdown gives no VAT category.

## What the rule checks

The VAT breakdown gives, for each VAT category and rate of the invoice, its taxable amount, its VAT amount, its category and its rate. The rule checks that each one gives its category, as a code: S for a standard rate, E for an exemption, AE for a reverse charge…

## Why it matters

BR-47 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-47 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give each VAT rate of your software its category, for example E for an exemption.
2. Check that the e-invoice writes the VAT breakdown in full, one block per category and rate.
3. If it is missing from the e-invoice, report it to the software's publisher, quoting BR-47.

## Common causes

- **A rate set up without a category** in the software.
- **A VAT breakdown built by hand** in an export, field by field.

## Technical details

A VAT breakdown is group BG-23, here its VAT category code BT-118. In CII, it is `ram:CategoryCode` of each `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`; in UBL, `cac:TaxCategory/cbc:ID` of each `cac:TaxSubtotal`.

In CII, the rule reads only a breakdown whose tax type, `ram:TypeCode`, is VAT: a breakdown typed otherwise has no VAT category for it.

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires each VAT breakdown's category code, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves it optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> Each VAT breakdown (BG-23) shall be defined through a VAT category code (BT-118).

BR-47, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-18](../BR-CL-18/): the VAT category of each line and of each VAT rate must be one of the codes EN 16931 uses, such as S.
- [BR-CO-18](../BR-CO-18/): every invoice must break down its VAT by category and rate, even when the VAT is zero.
- [BR-48](../BR-48/): each VAT breakdown must give its rate, 0% included, unless the invoice is outside the scope of VAT.
