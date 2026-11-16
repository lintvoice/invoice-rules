# A quantity has more than 4 decimals

A quantity on the invoice has more than 4 decimals or an invalid format.

## What the rule checks

The rule checks the invoiced quantity of each line, and the base quantity of its price (for example, a price per 100 units). Each must:

- have at most 4 decimals;
- use a dot as decimal separator;
- have at most 19 characters, separator not counted.

The minus sign is allowed.

## Why it matters

BR-FR-DEC-02 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Round the quantities to 4 decimals at most in your software.
2. For a quantity in a small unit, such as grams, consider a larger unit, such as kilograms, rather than many decimals.
3. If your software exports more decimals, report it to the software's publisher, quoting BR-FR-DEC-02.

## Common causes

- **A quantity computed by division** (such as 1/3) and not rounded.
- **A conversion between units** that adds decimals.
- **A decimal comma.**

## Technical details

Quantities BT-129 (invoiced quantity, `ram:BilledQuantity`) and BT-149 (item price base quantity, `ram:BasisQuantity`): decimal, at most 19 digits of which 4 decimals.

## Official text

> La quantité « […] » est invalide. Elle doit : - être un nombre avec au plus 4 décimales (séparateur « . »), - contenir au maximum 19 caractères (hors séparateur), - et peut commencer par un signe « - ».

BR-FR-DEC-02, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-DEC-02_BT-129`, `BR-FR-DEC-02_BT-149`.

## Related rules

- [BR-FR-DEC-01](../BR-FR-DEC-01/): amounts: 2 decimals at most.
- [BR-FR-DEC-03](../BR-FR-DEC-03/): unit prices: 6 decimals at most.
- [BR-FR-DEC-04](../BR-FR-DEC-04/): VAT rates: 2 decimals at most, positive.
