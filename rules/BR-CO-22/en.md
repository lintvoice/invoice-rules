# A charge on the whole invoice has no reason

A charge on the whole invoice gives neither a reason nor a reason code.

## What the rule checks

Each charge on the whole invoice must say why it is there: a reason as text ("Shipping"), a reason code, or both. The rule checks that at least one of the two is present.

## Why it matters

BR-CO-22 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-22 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. In your invoicing software, fill in the reason of each charge on the whole invoice, for example "Shipping".
2. If your software offers reason codes, choose the matching one.
3. If the reason is entered but missing from the e-invoice, report it to the software's publisher, quoting BR-CO-22.

## Common causes

- **A charge on the whole invoice entered without a label.**
- **A label printed on the PDF** but missing from the e-invoice data.

## Technical details

A charge on document level is group BG-21, with a reason BT-104 and a reason code BT-105. In CII, the rule reads `ram:Reason` and `ram:ReasonCode` of each `ram:SpecifiedTradeAllowanceCharge` in `ram:ApplicableHeaderTradeSettlement` whose `ram:ChargeIndicator` is true; in UBL, `cbc:AllowanceChargeReason` and `cbc:AllowanceChargeReasonCode` of each `cac:AllowanceCharge` of the document whose `cbc:ChargeIndicator` is true.

The EN 16931 rule BR-38 requires the same: a charge on the whole invoice without a reason fails both rules, and so does the example invoice.

## Official text

> Each Document level charge (BG-21) shall contain a Document level charge reason (BT-104) or a Document level charge reason code (BT-105), or both.

BR-CO-22, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-12](../BR-CO-12/): the charge total must be the sum of the charges on the whole invoice.
- [BR-38](../BR-38/): the core rule that requires the reason of a charge on the whole invoice.
- [BR-CO-21](../BR-CO-21/): each allowance on the whole invoice must have a reason, as text or as a code.
