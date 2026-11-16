# An invoice already paid does not show it in its amounts

The invoice is declared already paid, but its amounts or its due date do not show it.

## What the rule checks

The billing framework B2, S2 or M2 marks an invoice already paid. Its amounts must reflect this:

- the amount already paid equals the total with VAT;
- the amount due is 0;
- the due date is given, and is the date of the payment.

## Why it matters

BR-FR-CO-09 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. If the invoice is paid, enter the amount paid (equal to the total with VAT) and the payment date as due date.
2. If it is not fully paid, do not use the framework B2, S2 or M2.
3. If the payment is recorded in your software but missing from the e-invoice, report it to the software's publisher, quoting BR-FR-CO-09.

## Common causes

- **A payment recorded in the software** but not carried into the e-invoice.
- **The framework B2, S2 or M2 chosen for a partly paid invoice.**
- **No due date.**

## Technical details

When BT-23 is `B2`, `S2` or `M2`: BT-113 (paid amount) = BT-112 (total with VAT), BT-115 (amount due) = 0, and BT-9 (due date) present. Three ids: `BR-FR-CO-09_BT-23-1`, `-2` and `-3`, one per check.

## Official text

> Si le cadre de facturation (BT-23) est B2, S2 ou M2 (facture déjà payée), alors le montant déjà payé (BT-113) doit être égal au montant total TTC (BT-112).

BR-FR-CO-09, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-CO-09_BT-23-1`, `BR-FR-CO-09_BT-23-2`, `BR-FR-CO-09_BT-23-3`.

## Related rules

- [BR-FR-08](../BR-FR-08/): the billing framework codes.
- [BR-FR-CO-07](../BR-FR-CO-07/): the due date may precede the issue date on an invoice already paid.
