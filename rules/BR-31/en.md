# An allowance on the whole invoice has no amount

An allowance on the whole invoice gives no amount.

## What the rule checks

An allowance on the whole invoice is a discount granted on the invoice as a whole, not on one line, for example a trade discount. The rule checks that each one gives its amount, without VAT.

## Why it matters

BR-31 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-31 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check that each allowance on the whole invoice has its amount in your software, a percentage turned into an amount.
2. Check that the e-invoice writes that amount, not only the percentage.
3. If the amount is missing from the e-invoice, report it to the software's publisher, quoting BR-31.

## Common causes

- **A percentage written without the amount it comes to.**
- **A label kept as a line of text**, without an amount.

## Technical details

An allowance on document level is group BG-20, its amount BT-92. In CII, it is `ram:ActualAmount` of each `ram:SpecifiedTradeAllowanceCharge` in `ram:ApplicableHeaderTradeSettlement` whose `ram:ChargeIndicator` is false; in UBL, `cbc:Amount` of each `cac:AllowanceCharge` of the document whose `cbc:ChargeIndicator` is false.

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires the amount of an allowance on the whole invoice, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves it optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> Each Document level allowance (BG-20) shall have a Document level allowance amount (BT-92).

BR-31, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-32](../BR-32/): each allowance on the whole invoice must give its VAT category, so that the VAT breakdown can take it into account.
- [BR-33](../BR-33/): each allowance on the whole invoice must give its reason: as text, as a code, or both.
- [BR-CO-11](../BR-CO-11/): the allowance total must be exactly the sum of the allowances on the whole invoice, to the cent.
