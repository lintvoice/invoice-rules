# A VAT rate has more than 2 decimals or is negative

A VAT rate on the invoice has more than 2 decimals, a minus sign, or too many digits.

## What the rule checks

The rule checks the format of each VAT rate (lines, document-level allowances and charges, VAT breakdown). Each must:

- be positive, with no minus sign;
- have at most 2 decimals (`20.00`, not `20.000`);
- have at most 4 characters, separator not counted.

## Why it matters

BR-FR-DEC-04 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check how your software writes VAT rates: `20` or `20.00`.
2. Write the rate without the % sign.
3. If your software adds decimals, report it to the software's publisher, quoting BR-FR-DEC-04.

## Common causes

- **A rate written with 3 decimals** (`20.000`).
- **A computed rate** with many decimals.
- **A negative rate** used for a correction.

## Technical details

Rates BT-96, BT-103 (document-level allowances and charges), BT-119 (VAT breakdown) and BT-152 (lines), `ram:RateApplicablePercent` in CII. A rate written `20.000` also fails BR-FR-16, whose list holds only the forms with up to 2 decimals.

## Official text

> Le taux de TVA « […] » est invalide. Il doit : - être un nombre strictement positif (sans signe « - »), - comporter au plus 2 décimales (séparateur « . »), - contenir au maximum 4 caractères (hors séparateur).

BR-FR-DEC-04, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-DEC-04_BT-119`, `BR-FR-DEC-04_BT-152`, `BR-FR-DEC-04_BT-96_BT-103`.

## Related rules

- [BR-FR-DEC-01](../BR-FR-DEC-01/): amounts: 2 decimals at most.
- [BR-FR-DEC-02](../BR-FR-DEC-02/): quantities: 4 decimals at most.
- [BR-FR-DEC-03](../BR-FR-DEC-03/): unit prices: 6 decimals at most.
- [BR-FR-16](../BR-FR-16/): the VAT rates allowed in France.
