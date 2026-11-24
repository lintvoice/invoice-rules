# The reverse charge mention is missing

The invoice uses the VAT category AE (reverse charge), but its VAT breakdown does not say why there is no VAT.

## What the rule checks

Category AE covers supplies on which the buyer, not the seller, accounts for the VAT: the seller invoices without VAT. Its breakdown says why the invoice charges no VAT. Here, it is the mention the law requires on the invoice, such as "Reverse charge" (the VATEX code `VATEX-EU-AE`). The rule checks that it gives a reason as text (BT-120), a reason code (BT-121), or both.

## Why it matters

BR-AE-10 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-AE-10 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the reason of each item in this category, for example the mention you print on your invoices.
2. If your software offers VATEX reason codes, choose the one that matches your case.
3. If the reason is entered but missing from the e-invoice, report it to the software's publisher, quoting BR-AE-10.

## Common causes

- **A mention printed on the PDF** but missing from the e-invoice data.
- **An item or a customer set up without a reason** in the software.

## Technical details

The exemption reason is BT-120 (text), its code BT-121, from the VATEX list (BR-CL-22). In CII: `ram:ExemptionReason` or `ram:ExemptionReasonCode` of each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `AE`; in UBL: `cbc:TaxExemptionReason` or `cbc:TaxExemptionReasonCode` of the `cac:TaxCategory` of each `cac:TaxSubtotal` of category `AE`.

The example invoice is all in AE, and its breakdown gives neither reason nor code; its fixed version gives both.

## Official text

> A VAT Breakdown (BG-23) with VAT Category code (BT-118) "Reverse charge" shall have a VAT exemption reason code (BT-121), meaning "Reverse charge" or the VAT exemption reason text (BT-120) "Reverse charge" (or the equivalent standard text in another language).

BR-AE-10, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-E-10](../BR-E-10/): when part of the invoice is exempt from VAT, its VAT breakdown must give the reason, as text or as a code.
- [BR-AE-01](../BR-AE-01/): an invoice with a line, an allowance or a charge in the VAT category AE (reverse charge) must have exactly one VAT breakdown for it.
- [BR-CL-22](../BR-CL-22/): when an invoice gives the reason for a VAT exemption as a code, the code must come from the VATEX list.
