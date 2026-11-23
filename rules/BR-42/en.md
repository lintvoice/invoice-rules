# A line allowance has no reason

An allowance on an invoice line gives neither a reason nor a reason code.

## What the rule checks

Each allowance on an invoice line must say why it is there: a reason as text ("Volume discount"), a reason code, or both. The rule checks that at least one of the two is present.

## Why it matters

BR-42 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-42 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. In your invoicing software, fill in the reason of each allowance on an invoice line, for example "Volume discount".
2. If your software offers reason codes, choose the matching one.
3. If the reason is entered but missing from the e-invoice, report it to the software's publisher, quoting BR-42.

## Common causes

- **An allowance on an invoice line entered without a label.**
- **A label printed on the PDF** but missing from the e-invoice data.

## Technical details

An allowance on a line is group BG-27, with a reason BT-139 and a reason code BT-140. In CII, the rule reads `ram:Reason` and `ram:ReasonCode` of each `ram:SpecifiedTradeAllowanceCharge` in `ram:SpecifiedLineTradeSettlement` whose `ram:ChargeIndicator` is false; in UBL, `cbc:AllowanceChargeReason` and `cbc:AllowanceChargeReasonCode` of each `cac:AllowanceCharge` in `cac:InvoiceLine` (or `cac:CreditNoteLine`) whose `cbc:ChargeIndicator` is false.

Rule BR-CO-23 requires the same: an allowance on an invoice line without a reason fails both rules, and so does the example invoice, which is BR-CO-23's.

## Official text

> Each Invoice line allowance (BG-27) shall have an Invoice line allowance reason (BT-139) or an Invoice line allowance reason code (BT-140).

BR-42, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-23](../BR-CO-23/): each allowance on an invoice line must give its reason: as text, as a code, or both.
- [BR-41](../BR-41/): each line allowance must give its amount.
