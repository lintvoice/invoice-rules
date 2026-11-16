# A date on the invoice does not have a year between 2000 and 2099

A date on the invoice (issue, due date, delivery, period…) does not exist, or its year is outside 2000 to 2099.

## What the rule checks

The rule checks the dates on the invoice:

- the issue date and the due date;
- the VAT point date;
- the delivery date;
- the start and end of the invoiced period, for the invoice and for its lines;
- the date of an earlier invoice it refers to.

Each must be a date that exists (no 31 April), with a year from 2000 to 2099.

## Why it matters

BR-FR-03 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Find the date at fault: the validation report gives its code (BT-2, BT-9…), see the technical details.
2. Correct it in your software, for example a typing error in the year (`2206` instead of `2026`).
3. If an empty or default date appears (`19000101`), your software produces it: report it to the software's publisher, quoting BR-FR-03.

## Common causes

- **A typing error in the year**, such as `2206` instead of `2026`.
- **A default date** the software writes when the field is empty, such as `19000101`.
- **A date that does not exist**, such as 30 February.
- **Day, month and year in the wrong order** after an export.

## Technical details

Expected format: `YYYYMMDD` (format 102 in CII). Dates checked: BT-2 (issue), BT-7 (VAT point date), BT-9 (due date), BT-26 (earlier invoice), BT-72 (delivery), BT-73 and BT-74 (invoiced period), and their line-level counterparts (BT-134, BT-135, EXT-FR-FE-138, EXT-FR-FE-158). The rule reads the first 8 characters and checks that the day exists in the month, leap years included.

## Official text

> La date d’émission (udt:DateTimeString) doit contenir une année comprise entre 2000 et 2099, au format AAAAMMJJ.

BR-FR-03, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-03_BT-134`, `BR-FR-03_BT-135`, `BR-FR-03_BT-2`, `BR-FR-03_BT-26`, `BR-FR-03_BT-7`, `BR-FR-03_BT-72`, `BR-FR-03_BT-73`, `BR-FR-03_BT-74`, `BR-FR-03_BT-9`, `BR-FR-03_EXT-FR-FE-134`, `BR-FR-03_EXT-FR-FE-135`, `BR-FR-03_EXT-FR-FE-138`, `BR-FR-03_EXT-FR-FE-158`.

## Related rules

- [BR-FR-CO-07](../BR-FR-CO-07/): the due date cannot be before the issue date.
