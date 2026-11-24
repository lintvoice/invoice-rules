# The exemption reason is not a valid code

The code that gives the reason for a VAT exemption is not in the VATEX list.

## What the rule checks

When no VAT is charged (an exemption, a reverse charge, an export…), the VAT breakdown gives the reason: as text, as a code, or both. The codes come from the VATEX list. Each one names the article of the EU VAT directive or of a national law behind the case: VATEX-EU-132 for the exemptions of article 132 of the directive, VATEX-EU-132-1I for education and vocational training… The rule checks that the code is one of the list's.

## Why it matters

BR-CL-22 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-22 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the exemption reason code from your software's list, or give the reason as text only.
2. Check that the e-invoice writes the code in full, as in the list.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-22.

## Common causes

- **A code cut short**, VATEX-EU-132-1 where the list has VATEX-EU-132 and VATEX-EU-132-1A to VATEX-EU-132-1Q.
- **The law's article written instead of the code.**

## Technical details

The VAT exemption reason code is BT-121. In CII, it is `ram:ExemptionReasonCode` of each `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`; in UBL, `cbc:TaxExemptionReasonCode` of each `cac:TaxCategory` of the VAT breakdown. The list is the European Commission's VATEX list, version 9 in the 1.3.17 files.

The example invoice has an exempt line whose VAT breakdown gives the code `VATEX-EU-132-1`, cut short. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000589`, which fails next to it in a Factur-X invoice.

## Official text

> Tax exemption reason code identifier scheme identifier MUST belong to the CEF VATEX code list

BR-CL-22, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-E-10](../BR-E-10/): when part of the invoice is exempt from VAT, its VAT breakdown must give the reason, as text or as a code.
