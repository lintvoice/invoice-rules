# A VAT exemption gives no reason

Part of the invoice is exempt from VAT, but its VAT breakdown does not give the reason.

## What the rule checks

When lines, allowances or charges are exempt from VAT, the invoice's VAT breakdown has an "exempt" row. It must say why: a reason as text, for example the legal mention of the exemption, a reason code, or both.

## Why it matters

BR-E-10 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-E-10 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. In your software, fill in the exemption reason of each exempt item or service, for example the mention you already print on your invoices.
2. If your software offers reason codes, choose the one that matches your case.
3. If the reason is entered but missing from the e-invoice, report it to the software's publisher, quoting BR-E-10.

## Common causes

- **An exemption mention printed on the PDF** but missing from the e-invoice data.
- **A seller under the VAT franchise** whose software does not send the reason of the franchise.
- **An exempt item** created without a reason in the software's catalogue.

## Technical details

The VAT breakdown is group BG-23; for category E ("Exempt from VAT"), it carries the exemption reason BT-120 (text) or its code BT-121. In CII: `ram:ExemptionReason` or `ram:ExemptionReasonCode` of each `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `E`; in UBL: `cbc:TaxExemptionReason` or `cbc:TaxExemptionReasonCode` of the `cac:TaxCategory` of each `cac:TaxSubtotal` of category `E`.

The reason code comes from the VATEX list, as rule BR-CL-22 requires; it has codes of its own for France, such as `VATEX-FR-FRANCHISE` for the French VAT franchise. The other categories without VAT have their own rule: BR-AE-10 (reverse charge), BR-IC-10 (intra-community supply), BR-G-10 (export outside the European Union), BR-O-10 (not subject to VAT).

The example invoice adds an exempt line to the base invoice and removes the reason from its breakdown; its fixed version gives the reason.

## Official text

> A VAT Breakdown (BG-23) with VAT Category code (BT-118) "Exempt from VAT" shall have a VAT exemption reason code (BT-121) or a VAT exemption reason text (BT-120).

BR-E-10, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-S-02](../BR-S-02/): lines subject to VAT require the seller's VAT number.
- [BR-CO-18](../BR-CO-18/): every invoice must break down its VAT by category and rate.
