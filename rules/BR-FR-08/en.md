# The billing framework is missing or unknown

The invoice does not give its billing framework, or uses a code that is not on the French list.

## What the rule checks

Every invoice must carry a billing framework code, which describes the invoice's situation. For example, according to the French rules themselves:

- S2, B2 or M2: an invoice already paid (see BR-FR-CO-09);
- S4, B4 or M4: a final invoice after a prepayment (see BR-FR-CO-08).

The 20 allowed codes: B1, S1, M1, B2, S2, M2, S3, B4, S4, M4, S5, S6, B7, S7, B8, S8, M8, B9, S9, M9.

## Why it matters

BR-FR-08 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check that your software fills in the billing framework: it is a setting of the e-invoice, not a printed statement.
2. Choose the code that matches your situation from the list above; your approved platform or your software's publisher can tell you which one to use.
3. If your software does not offer it, report it to the software's publisher, quoting BR-FR-08.

## Common causes

- **The software does not fill in this field**, which the European standard leaves optional.
- **A code from another country or profile** instead of the French framework.
- **A typing error** in the code, or a lowercase letter (`s1`).

## Technical details

The billing framework uses BT-23 of EN 16931 (business process type): `ram:BusinessProcessSpecifiedDocumentContextParameter/ram:ID` in CII, `cbc:ProfileID` in UBL. In UBL, the official files also publish under `BR-FR-08_BT-151-2` a check of VAT category codes L and M that belongs to BR-FR-15.

## Official text

> La valeur du mode de facturation (ram:ID) est absente ou n’est pas autorisée. Valeurs acceptées : B1, S1, M1, B2, S2, M2, S3, B4, S4, M4, S5, S6, B7, S7, B8, S8, M8, B9, S9, M9.

BR-FR-08, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-08_BT-151-2`, `BR-FR-08_BT-23`.

## Related rules

- [BR-FR-CO-08](../BR-FR-CO-08/): a final invoice after prepayment cannot be a prepayment invoice.
- [BR-FR-CO-09](../BR-FR-CO-09/): an invoice already paid must show it in its amounts.
