# The due date is before the invoice date

The invoice's due date is earlier than its issue date.

## What the rule checks

When the invoice gives a due date, it must be on or after the issue date. Two exceptions:

- prepayment invoices and credit notes (types 386, 500 and 503);
- invoices already paid (billing framework B2, S2 or M2).

## Why it matters

BR-FR-CO-07 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check the issue date and the due date of the invoice.
2. Check the payment terms (such as "30 days") your software uses to compute the due date.
3. For an invoice already paid, use the billing framework B2, S2 or M2 (see BR-FR-CO-09).

## Common causes

- **A typing error** in one of the two dates.
- **An invoice dated afterwards**, while the due date was computed from the order date.
- **An invoice already paid** without the framework B2, S2 or M2.

## Technical details

Due date BT-9 on or after issue date BT-2. Exceptions: BT-3 in `386`, `500`, `503`, or BT-23 in `B2`, `S2`, `M2`.

## Official text

> La date d’échéance (BT-9), si présente, doit être postérieure ou égale à la date de facture (BT-2), sauf si la facture est de type acompte (386, 500, 503) ou si le cadre de facturation (BT-23) est B2, S2 ou M2.

BR-FR-CO-07, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-CO-07_BT-9`.

## Related rules

- [BR-FR-03](../BR-FR-03/): every date has a year between 2000 and 2099.
- [BR-FR-CO-09](../BR-FR-CO-09/): an invoice already paid shows it in its amounts.
