# A zero-rated VAT breakdown gives an exemption reason

The VAT breakdown in category Z (zero rate) gives an exemption reason, as text or as a code.

## What the rule checks

Category Z covers supplies taxed at a rate of 0 %, such as solar panels sold to their operator in Germany. The supply is taxed, at 0 %: it is not an exemption, so its breakdown gives no exemption reason (BT-120) and no reason code (BT-121). The rule checks that both are absent.

## Why it matters

BR-Z-10 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-Z-10 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Remove the exemption reason from the items in category Z.
2. If the supply is in fact exempt, give it category E and keep the reason.
3. If your software writes a reason for every category, report it to the software's publisher, quoting BR-Z-10.

## Common causes

- **A reason written for every category**, the name of the rate included.
- **An exempt supply put in category Z**, with its reason kept.

## Technical details

The exemption reason is BT-120 (text), its code BT-121, from the VATEX list (BR-CL-22). In CII: `ram:ExemptionReason` or `ram:ExemptionReasonCode` of each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `Z`; in UBL: `cbc:TaxExemptionReason` or `cbc:TaxExemptionReasonCode` of the `cac:TaxCategory` of each `cac:TaxSubtotal` of category `Z`.

The example invoice is all in Z, and its breakdown gives the name of its rate as an exemption reason; its fixed version gives none.

## Official text

> A VAT Breakdown (BG-23) with VAT Category code (BT-118) "Zero rated" shall not have a VAT exemption reason code (BT-121) or VAT exemption reason text (BT-120).

BR-Z-10, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-E-10](../BR-E-10/): when part of the invoice is exempt from VAT, its VAT breakdown must give the reason, as text or as a code.
- [BR-S-10](../BR-S-10/): an exemption reason belongs to the categories without VAT; the VAT breakdown in category S (standard rate) gives none.
- [BR-CL-22](../BR-CL-22/): when an invoice gives the reason for a VAT exemption as a code, the code must come from the VATEX list.
