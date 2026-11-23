# A charge on the whole invoice has no VAT category

A charge on the whole invoice gives no VAT category.

## What the rule checks

A charge on the whole invoice adds to the VAT of the invoice, so it says which VAT category it belongs to (standard rate, exempt, reverse charge…) and at which rate. The VAT breakdown counts it under that category. The rule checks that the category is given.

## Why it matters

BR-37 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-37 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give each charge on the whole invoice the VAT category and rate of what it applies to, in your software.
2. Check that the e-invoice writes them, not only the amount.
3. If the category is missing from the e-invoice, report it to the software's publisher, quoting BR-37.

## Common causes

- **A charge on the whole invoice entered as an amount only**, without VAT.
- **An invoice with several VAT rates**, where the software does not know which one applies.

## Technical details

A charge on document level is group BG-21, its VAT category code BT-102. In CII, the rule reads `ram:CategoryCode` of the `ram:CategoryTradeTax` whose `ram:TypeCode` is VAT, in each `ram:SpecifiedTradeAllowanceCharge` of `ram:ApplicableHeaderTradeSettlement` whose `ram:ChargeIndicator` is true; in UBL, `cbc:ID` of the charge's `cac:TaxCategory`.

The example invoice gives a charge without its VAT category. The charge then adds to no VAT breakdown, so the taxable amount of the standard rate no longer matches its lines plus its charges, and BR-S-08 fails too. The Factur-X EN 16931 profile has its own rules, which check that the category is there too: in a Factur-X invoice, its rule `FX-SCH-A-000479` fails next to BR-37, as in the example invoice.

## Official text

> Each Document level charge (BG-21) shall have a Document level charge VAT category code (BT-102).

BR-37, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-36](../BR-36/): each charge on the whole invoice must give its amount.
- [BR-38](../BR-38/): each charge on the whole invoice must give its reason: as text, as a code, or both.
- [BR-S-08](../BR-S-08/): for each rate, the taxable amount must be the sum of the lines at that rate, plus the charges and minus the allowances at the same rate.
- [BR-CL-17](../BR-CL-17/): the VAT category of an allowance or a charge on the whole invoice must be one of the codes EN 16931 uses, such as S.
