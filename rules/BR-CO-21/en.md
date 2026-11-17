# An allowance on the whole invoice has no reason

An allowance on the whole invoice gives neither a reason nor a reason code.

## What the rule checks

Each allowance on the whole invoice must say why it is there: a reason as text ("Trade discount"), a reason code, or both. The rule checks that at least one of the two is present.

## Why it matters

BR-CO-21 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-21 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. In your invoicing software, fill in the reason of each allowance on the whole invoice, for example "Trade discount".
2. If your software offers reason codes, choose the matching one.
3. If the reason is entered but missing from the e-invoice, report it to the software's publisher, quoting BR-CO-21.

## Common causes

- **An allowance on the whole invoice entered without a label.**
- **A label printed on the PDF** but missing from the e-invoice data.

## Technical details

An allowance on document level is group BG-20, with a reason BT-97 and a reason code BT-98. In CII, the rule reads `ram:Reason` and `ram:ReasonCode` of each `ram:SpecifiedTradeAllowanceCharge` in `ram:ApplicableHeaderTradeSettlement` whose `ram:ChargeIndicator` is false; in UBL, `cbc:AllowanceChargeReason` and `cbc:AllowanceChargeReasonCode` of each `cac:AllowanceCharge` of the document whose `cbc:ChargeIndicator` is false.

The EN 16931 rule BR-33 requires the same: an allowance on the whole invoice without a reason fails both rules, and so does the example invoice.

## Official text

> Each Document level allowance (BG-20) shall contain a Document level allowance reason (BT-97) or a Document level allowance reason code (BT-98), or both.

BR-CO-21, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-11](../BR-CO-11/): the allowance total must be the sum of the allowances on the whole invoice.
- [BR-33](../BR-33/): the core rule that requires the reason of an allowance on the whole invoice.
- [BR-CO-22](../BR-CO-22/): each charge on the whole invoice must have a reason, as text or as a code.
