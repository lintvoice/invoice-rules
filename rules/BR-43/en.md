# A line charge has no amount

A line charge gives no amount.

## What the rule checks

A line charge is an amount added to one invoice line only, for example packaging. The rule checks that each one gives its amount, without VAT.

## Why it matters

BR-43 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-43 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check that each line charge has its amount in your software, a percentage turned into an amount.
2. Check that the e-invoice writes that amount, not only the percentage.
3. If the amount is missing from the e-invoice, report it to the software's publisher, quoting BR-43.

## Common causes

- **A percentage written without the amount it comes to.**
- **A label kept as a line of text**, without an amount.

## Technical details

An invoice line charge is group BG-28, its amount BT-141. In CII, it is `ram:ActualAmount` of each `ram:SpecifiedTradeAllowanceCharge` in a line's `ram:SpecifiedLineTradeSettlement` whose `ram:ChargeIndicator` is true; in UBL, `cbc:Amount` of each `cac:AllowanceCharge` of a `cac:InvoiceLine` whose `cbc:ChargeIndicator` is true.

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires the amount of a line charge, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves it optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> Each Invoice line charge (BG-28) shall have an Invoice line charge amount (BT-141).

BR-43, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-44](../BR-44/): each charge on an invoice line must give its reason: as text, as a code, or both.
- [BR-41](../BR-41/): each line allowance must give its amount.
