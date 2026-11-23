# An allowance's reason is not a valid code

An allowance's reason code is not in the official list for allowances.

## What the rule checks

An allowance on the whole invoice or on a line can give its reason as a code, from an official list kept for allowances: 95 for a discount, 100 for a special rebate, 64 for a special agreement… The rule checks that the code comes from that list, not the reason's text.

## Why it matters

BR-CL-19 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-19 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the allowance's reason code from your software's list, or give the reason as text only.
2. Check that the e-invoice writes the text in the reason and the code in the reason code.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-19.

## Common causes

- **The reason's text copied into the code**, such as Discount.
- **A charge code used for an allowance**: the two lists are different.

## Technical details

The reason code of a document level allowance is BT-98, of a line allowance BT-140. In CII, it is `ram:ReasonCode` of each `ram:SpecifiedTradeAllowanceCharge` whose `ram:ChargeIndicator` is false; in UBL, `cbc:AllowanceChargeReasonCode` of each `cac:AllowanceCharge` whose `cbc:ChargeIndicator` is false. The list is the EN 16931 part of UNCL 5189, 19 codes; a charge's code comes from another list, UNCL 7161 (rule BR-CL-20).

The example invoice gives an allowance on the whole invoice the reason code `Discount`, its reason's text. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000601`, which fails next to it in a Factur-X invoice.

## Official text

> Coded allowance reasons MUST belong to the UNCL 5189 code list

BR-CL-19, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-20](../BR-CL-20/): when a charge gives its reason as a code, the code must come from the official list for charges, such as FC for freight.
- [BR-33](../BR-33/): each allowance on the whole invoice must give its reason: as text, as a code, or both.
- [BR-CO-21](../BR-CO-21/): each allowance on the whole invoice must give its reason: as text, as a code, or both.
