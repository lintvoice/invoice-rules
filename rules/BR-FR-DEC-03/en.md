# A unit price has more than 6 decimals or is negative

A unit price on the invoice has more than 6 decimals, a minus sign, or too many digits.

## What the rule checks

The rule checks the net unit price, the gross unit price and the discount on the unit price of each item. Each must:

- have at most 6 decimals;
- be positive, with no minus sign, except when the billing framework is B9, S9 or M9;
- have at most 19 characters, separator not counted.

## Why it matters

BR-FR-DEC-03 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Round the unit prices to 6 decimals at most in your software.
2. To give a discount, use an allowance rather than a negative price.
3. If your software exports negative or over-precise prices, report it to the software's publisher, quoting BR-FR-DEC-03.

## Common causes

- **A unit price computed from a total** and not rounded.
- **A negative price** used to give a discount on a line.

## Technical details

Item net price BT-146, item price discount BT-147 and item gross price BT-148 (`ram:ChargeAmount` and `ram:AppliedTradeAllowanceCharge/ram:ActualAmount` in CII): decimal, at most 19 digits of which 6 decimals, no minus sign unless BT-23 is `B9`, `S9` or `M9`.

## Official text

> Le montant « […] » est invalide. Il doit : - être un nombre strictement positif (sans signe « - »), sauf si Cadre de Facturation (BT-23) est S9, M9 ou B9 (bi-directionnel) - comporter au plus 6 décimales (séparateur « . »), - contenir au maximum 19 caractères (hors séparateur).

BR-FR-DEC-03, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-DEC-03_BT-146`, `BR-FR-DEC-03_BT-147`, `BR-FR-DEC-03_BT-148`.

## Related rules

- [BR-FR-DEC-01](../BR-FR-DEC-01/): amounts: 2 decimals at most.
- [BR-FR-DEC-02](../BR-FR-DEC-02/): quantities: 4 decimals at most.
- [BR-FR-DEC-04](../BR-FR-DEC-04/): VAT rates: 2 decimals at most, positive.
