# The allowance total is not the sum of the allowances

The invoice's allowance total is not equal to the sum of the allowances given on the whole invoice.

## What the rule checks

An invoice can give allowances on its overall amount, besides allowances on a line: for example a trade discount on the whole order. Each has its amount, and the invoice gives their total. The rule checks that this total is exactly the sum of these allowances, to the cent. An invoice without such allowances must not give an allowance total other than zero.

## Why it matters

BR-CO-11 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-11 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Add up the allowances given on the whole invoice, without the line allowances, and give the result as the allowance total.
2. If the invoice has no allowance on its overall amount, leave the allowance total empty or at zero.
3. If your software computes this total another way, report it to the software's publisher, quoting BR-CO-11.

## Common causes

- **Line allowances counted in the allowance total**, which covers only allowances on the whole invoice.
- **An allowance added, changed or removed after the totals were computed.**
- **A percentage allowance rounded differently** in the total and in the allowance itself.

## Technical details

The sum of allowances on document level is BT-107, each allowance amount BT-92 (group BG-20). In CII, the rule compares `ram:AllowanceTotalAmount` with the sum of the `ram:ActualAmount` of the `ram:SpecifiedTradeAllowanceCharge` in `ram:ApplicableHeaderTradeSettlement` whose `ram:ChargeIndicator` is false; in UBL, `cac:LegalMonetaryTotal/cbc:AllowanceTotalAmount` with the sum of the `cac:AllowanceCharge/cbc:Amount` whose `cbc:ChargeIndicator` is false. Line allowances (BG-27) are not part of this total.

## Official text

> Sum of allowances on document level (BT-107) = Σ Document level allowance amount (BT-92).

BR-CO-11, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-12](../BR-CO-12/): the charge total must be the sum of the charges added to the whole invoice.
- [BR-CO-13](../BR-CO-13/): the total without VAT must be the sum of the lines, minus allowances, plus charges.
- [BR-CO-21](../BR-CO-21/): each allowance on the whole invoice must have a reason, as text or as a code.
