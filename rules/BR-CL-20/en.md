# A charge's reason is not a valid code

A charge's reason code is not in the official list for charges.

## What the rule checks

A charge on the whole invoice or on a line can give its reason as a code, from an official list kept for charges: FC for freight, ABL for additional packaging… The rule checks that the code comes from that list, not the reason's text.

## Why it matters

BR-CL-20 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-20 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the charge's reason code from your software's list, or give the reason as text only.
2. Check that the e-invoice writes the text in the reason and the code in the reason code.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-20.

## Common causes

- **The reason's text copied into the code**, such as Shipping.
- **An allowance code used for a charge**: the two lists are different.

## Technical details

The reason code of a document level charge is BT-105, of a line charge BT-145. In CII, it is `ram:ReasonCode` of each `ram:SpecifiedTradeAllowanceCharge` whose `ram:ChargeIndicator` is true; in UBL, `cbc:AllowanceChargeReasonCode` of each `cac:AllowanceCharge` whose `cbc:ChargeIndicator` is true. The list is UNCL 7161; an allowance's code comes from another list, UNCL 5189 (rule BR-CL-19).

The example invoice gives a charge on the whole invoice the reason code `Shipping`, its reason's text. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000604`, which fails next to it in a Factur-X invoice.

## Official text

> Coded charge reasons MUST belong to the UNCL 7161 code list

BR-CL-20, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-19](../BR-CL-19/): when an allowance gives its reason as a code, the code must come from the official list for allowances, such as 95 for a discount.
- [BR-38](../BR-38/): each charge on the whole invoice must give its reason: as text, as a code, or both.
- [BR-CO-22](../BR-CO-22/): each charge on the whole invoice must give its reason: as text, as a code, or both.
