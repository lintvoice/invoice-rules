# A line charge has no reason

A charge on an invoice line gives neither a reason nor a reason code.

## What the rule checks

Each charge on an invoice line must say why it is there: a reason as text ("Packaging"), a reason code, or both. The rule checks that at least one of the two is present.

## Why it matters

BR-CO-24 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-24 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. In your invoicing software, fill in the reason of each charge on an invoice line, for example "Packaging".
2. If your software offers reason codes, choose the matching one.
3. If the reason is entered but missing from the e-invoice, report it to the software's publisher, quoting BR-CO-24.

## Common causes

- **A charge on an invoice line entered without a label.**
- **A label printed on the PDF** but missing from the e-invoice data.

## Technical details

A charge on a line is group BG-28, with a reason BT-144 and a reason code BT-145. In CII, the rule reads `ram:Reason` and `ram:ReasonCode` of each `ram:SpecifiedTradeAllowanceCharge` in `ram:SpecifiedLineTradeSettlement` whose `ram:ChargeIndicator` is true; in UBL, `cbc:AllowanceChargeReason` and `cbc:AllowanceChargeReasonCode` of each `cac:AllowanceCharge` in `cac:InvoiceLine` (or `cac:CreditNoteLine`) whose `cbc:ChargeIndicator` is true.

The EN 16931 rule BR-44 requires the same: a charge on an invoice line without a reason fails both rules, and so does the example invoice.

## Official text

> Each Invoice line charge (BG-28) shall contain an Invoice line charge reason (BT-144) or an Invoice line charge reason code (BT-145), or both.

BR-CO-24, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-23](../BR-CO-23/): each line allowance must have a reason, as text or as a code.
- [BR-44](../BR-44/): the core rule that requires the reason of a line charge.
- [BR-CO-22](../BR-CO-22/): each charge on the whole invoice must have a reason, as text or as a code.
