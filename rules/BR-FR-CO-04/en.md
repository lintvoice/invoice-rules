# A corrective invoice does not cite exactly one earlier invoice

A corrective invoice cites no earlier invoice, or several, or one without its date.

## What the rule checks

A corrective invoice (types 384, 471, 472 and 473) corrects one specific invoice. It must cite exactly one earlier invoice, with:

- its number;
- its issue date.

No reference, or more than one, is refused.

## Why it matters

BR-FR-CO-04 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. On the corrective invoice, enter the number and the date of the invoice it corrects.
2. To correct several invoices, issue one corrective invoice for each.
3. If your software sends the number without the date, report it to the software's publisher, quoting BR-FR-CO-04.

## Common causes

- **The corrected invoice is not cited.**
- **Several invoices cited** on one corrective invoice.
- **A number cited without its date.**

## Technical details

When BT-3 is `384`, `471`, `472` or `473`: exactly one preceding invoice reference (BG-3) with both BT-25 (number) and BT-26 (date).

## Official text

> Si le type de facture (BT-3) est une facture rectificative (384, 471, 472, 473), alors **une et une seule** référence à une facture antérieure (BT-25) avec sa date (BT-26) doit être présente.

BR-FR-CO-04, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-CO-04_BT-3`, `BR-FR-CO-04_BT-4`.

## Related rules

- [BR-FR-CO-05](../BR-FR-CO-05/): a credit note must cite the invoice it corrects.
- [BR-FR-04](../BR-FR-04/): the document types allowed in France.
