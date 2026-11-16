# The VAT rate is not a rate allowed in France

A VAT rate on the invoice is not on the list of rates allowed in France, or is written with a % sign.

## What the rule checks

The rule checks each VAT rate on the invoice (lines, allowances and charges, VAT breakdown). It must:

- be written as a number, without the % sign (`20`, not `20 %`);
- be on the list of the official files: 0, 0.9, 1.05, 1.75, 2.1, 5.5, 7, 8.5, 9.2, 9.6, 10, 13, 19.6, 20 and 20.6;
- have at most two decimals (`20`, `20.0` or `20.00`).

## Why it matters

BR-FR-16 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check the rate applied in your software: a foreign rate (such as 21) or a typing error is refused.
2. Write the rate without the % sign, with at most two decimals.
3. If your software exports a rounded or badly formatted rate, report it to the software's publisher, quoting BR-FR-16.

## Common causes

- **A rate from another country**, such as 21.
- **The % sign in the value.**
- **A computed rate**, such as 19.99, instead of a chosen one.
- **Too many decimals** (`20.000`).

## Technical details

Rates BT-152 (lines), BT-96 and BT-103 (document-level allowances and charges), BT-119 (VAT breakdown): `ram:RateApplicablePercent` in CII. A missing rate is not checked by this rule.

## Official text

> Le taux de TVA (BT-96) doit être exprimé en pourcentage sans symbole « % » et faire partie des valeurs autorisées.

BR-FR-16, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-16_BT-103`, `BR-FR-16_BT-119`, `BR-FR-16_BT-152`, `BR-FR-16_BT-96`, `BR-FR-16_BT-96_BT-103`.

## Related rules

- [BR-FR-15](../BR-FR-15/): the VAT categories allowed in France.
- [BR-FR-DEC-04](../BR-FR-DEC-04/): the format of a VAT rate: positive, two decimals at most.
