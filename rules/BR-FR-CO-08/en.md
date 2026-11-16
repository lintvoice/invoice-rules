# A final invoice after prepayment has a prepayment type

A document with the framework B4, S4 or M4 has a prepayment type (386, 500 or 503).

## What the rule checks

The framework B4, S4 or M4 marks a final invoice, issued after one or more prepayments. So it cannot itself be a prepayment document: types 386, 500 and 503 are refused with this framework.

## Why it matters

BR-FR-CO-08 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. If the document is a prepayment invoice, do not give it the framework B4, S4 or M4.
2. If it is the final invoice, give it an ordinary invoice type, such as 380.
3. If your software sets these values on its own, report it to the software's publisher, quoting BR-FR-CO-08.

## Common causes

- **The final invoice's framework applied by mistake** to a prepayment invoice.
- **The prepayment invoice's type copied** onto the final invoice.

## Technical details

Refused combination: BT-23 in `B4`, `S4`, `M4` with BT-3 in `386`, `500`, `503`.

## Official text

> Si le cadre de facturation (BT-23) est B4, S4 ou M4 (factures définitives après acompte), alors le type de facture (BT-3) ne peut pas être une facture ou un avoir d’acompte (386, 500, 503).

BR-FR-CO-08, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-CO-08_BT-23`.

## Related rules

- [BR-FR-08](../BR-FR-08/): the billing framework codes.
- [BR-FR-CO-07](../BR-FR-CO-07/): the due date of a prepayment invoice.
