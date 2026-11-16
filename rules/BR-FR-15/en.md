# The VAT category is not allowed in France

A line, an allowance or charge, or the VAT breakdown uses a VAT category code that is not allowed in France.

## What the rule checks

Each line, each document-level allowance or charge, and each VAT subtotal gives a VAT category as a code. In France, only these codes are allowed:

- **S**: VAT at a positive rate;
- **Z**: zero rate;
- **E**: exempt;
- **AE**: reverse charge;
- **K**: intra-community supply;
- **G**: export outside the EU;
- **O**: outside the scope of VAT.

Codes L and M, specific to the Canary Islands and to Ceuta and Melilla, are refused.

## Why it matters

BR-FR-15 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check the VAT category of your items, allowances and charges in your software.
2. Replace L or M with the category of the operation, for example S for a sale with French VAT.
3. If your software offers no allowed category, report it to the software's publisher, quoting BR-FR-15.

## Common causes

- **A code picked by mistake** in a list that holds every European code.
- **A setting made for Spain** reused for France.
- **An allowance or a charge** whose category was not updated.

## Technical details

VAT category codes (UNCL 5305 subset of EN 16931): BT-151 on lines, BT-95 and BT-102 for document-level allowances and charges, BT-118 in the VAT breakdown. Ids ending in `_LM` report codes L and M; the others, a code off the list. In UBL, the line check is published under `BR-FR-08_BT-151-2`.

## Official text

> Code de catégorie de TVA invalide.

BR-FR-15, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-15_BT-118-1`, `BR-FR-15_BT-118-2`, `BR-FR-15_BT-151-1`, `BR-FR-15_BT-95_BT-102`, `BR-FR-15_BT-95_BT-102-1`, `BR-FR-15_BT-95_BT-102-2`, `BR-FR-15_BT-95_BT-102_LM`, `BR-FR-15_BT-95_BT-118`, `BR-FR-15_BT-95_BT-118_LM`, `BR-FR-15_BT-95_BT-151`, `BR-FR-15_BT-95_BT-151_LM`.

## Related rules

- [BR-FR-16](../BR-FR-16/): the VAT rates allowed in France.
