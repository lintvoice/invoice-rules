# The charge total is not the sum of the charges

The invoice's charge total is not equal to the sum of the charges added to the whole invoice.

## What the rule checks

An invoice can add charges to its overall amount, besides charges on a line: for example shipping or packaging. Each has its amount, and the invoice gives their total. The rule checks that this total is exactly the sum of these charges, to the cent. An invoice without such charges must not give a charge total other than zero.

## Why it matters

BR-CO-12 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-12 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Add up the charges added to the whole invoice, without the line charges, and give the result as the charge total.
2. If the invoice has no charge on its overall amount, leave the charge total empty or at zero.
3. If your software computes this total another way, report it to the software's publisher, quoting BR-CO-12.

## Common causes

- **Line charges counted in the charge total**, which covers only charges on the whole invoice.
- **A charge added, changed or removed after the totals were computed.**

## Technical details

The sum of charges on document level is BT-108, each charge amount BT-99 (group BG-21). In CII, the rule compares `ram:ChargeTotalAmount` with the sum of the `ram:ActualAmount` of the `ram:SpecifiedTradeAllowanceCharge` in `ram:ApplicableHeaderTradeSettlement` whose `ram:ChargeIndicator` is true; in UBL, `cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` with the sum of the `cac:AllowanceCharge/cbc:Amount` whose `cbc:ChargeIndicator` is true. Line charges (BG-28) are not part of this total.

## Official text

> Sum of charges on document level (BT-108) = Σ Document level charge amount (BT-99).

BR-CO-12, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-11](../BR-CO-11/): the allowance total must be the sum of the allowances given on the whole invoice.
- [BR-CO-13](../BR-CO-13/): the total without VAT must be the sum of the lines, minus allowances, plus charges.
- [BR-CO-22](../BR-CO-22/): each charge on the whole invoice must have a reason, as text or as a code.
