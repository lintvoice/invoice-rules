# An amount has more than 2 decimals or an invalid format

An amount on the invoice has more than 2 decimals, a comma, or too many digits.

## What the rule checks

The rule checks the format of the amounts on the invoice: totals, line amounts, allowances and charges, VAT bases and VAT amounts. Each must:

- have at most 2 decimals (`1230.00`, not `1230.000`);
- use a dot as decimal separator, not a comma;
- have at most 19 characters, separator not counted.

The minus sign is allowed.

## Why it matters

BR-FR-DEC-01 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check how your software rounds amounts: to the cent.
2. Check that amounts are exported with a dot and no thousands separator.
3. If your software exports more decimals or a comma, report it to the software's publisher, quoting BR-FR-DEC-01.

## Common causes

- **An amount not rounded after a computation** (price × quantity, percentage discount).
- **A decimal comma** (`1230,00`).
- **A thousands separator** (`1 230.00`).

## Technical details

Format: decimal, at most 19 digits of which 2 decimals, dot separator, optional leading minus. Amounts checked: BT-92, BT-93, BT-99, BT-100 (document-level allowances and charges), BT-106 to BT-117 (totals and VAT breakdown), BT-131 (line net amount), BT-136, BT-137, BT-141, BT-142 (line allowances and charges). Most of these amounts also fail an EN 16931 BR-DEC rule.

## Official text

> Le montant « […] » est invalide. Il doit comporter au plus 2 décimales, être exprimé avec un point comme séparateur, et ne pas dépasser 19 caractères (hors séparateur). Le signe « - » est autorisé.

BR-FR-DEC-01, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-DEC-01_BT-106`, `BR-FR-DEC-01_BT-107`, `BR-FR-DEC-01_BT-108`, `BR-FR-DEC-01_BT-109`, `BR-FR-DEC-01_BT-110`, `BR-FR-DEC-01_BT-111`, `BR-FR-DEC-01_BT-112`, `BR-FR-DEC-01_BT-113`, `BR-FR-DEC-01_BT-114`, `BR-FR-DEC-01_BT-115`, `BR-FR-DEC-01_BT-116`, `BR-FR-DEC-01_BT-117`, `BR-FR-DEC-01_BT-131`, `BR-FR-DEC-01_BT-136_BT-141`, `BR-FR-DEC-01_BT-137_BT-142`, `BR-FR-DEC-01_BT-92_BT-99`, `BR-FR-DEC-01_BT-93_BT-100`.

## Related rules

- [BR-FR-DEC-02](../BR-FR-DEC-02/): quantities: 4 decimals at most.
- [BR-FR-DEC-03](../BR-FR-DEC-03/): unit prices: 6 decimals at most.
- [BR-FR-DEC-04](../BR-FR-DEC-04/): VAT rates: 2 decimals at most, positive.
