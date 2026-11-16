# The document type is not on the French list

The code that says what the document is (invoice, credit note, prepayment…) is not allowed by the French rules.

## What the rule checks

Every invoice carries a 3-digit code that says what it is, for example 380 (invoice), 381 (credit note), 384 (corrective invoice), 386 (prepayment invoice) or 389 (self-billed invoice). The French rules allow only these 16 codes: 380, 389, 393, 501, 386, 500, 384, 471, 472, 473, 261, 262, 381, 396, 502, 503.

The rule checks the code of the invoice, and of an earlier document it refers to, at the top of the invoice or on a line.

## Why it matters

BR-FR-04 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

The international code list (UNTDID 1001) has many more codes; the official message states that the others must not be used.

## How to fix it

1. Check the type chosen in your software: invoice, credit note, prepayment, corrective invoice.
2. Use a code from the list, for example 380 for an ordinary invoice instead of 326 (partial invoice).
3. If your software offers no allowed type, report it to the software's publisher, quoting BR-FR-04.

## Common causes

- **A code valid in Europe but not in France**, such as 326 (partial invoice).
- **A default code from software made for another country.**
- **The type of an earlier document cited** is wrong, while the invoice's own type is right.

## Technical details

The document type is BT-3 (UNTDID 1001 codes). The rule also applies to the type of a referenced document (EXT-FR-FE-02) and of a document referenced on a line (EXT-FR-FE-137).

## Official text

> Le code type de document (ram:TypeCode) n’est pas autorisé. Valeurs acceptées : 380, 389, 393, 501, 386, 500, 384, 471, 472, 473, 261, 262, 381, 396, 502, 503.

BR-FR-04, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-04_BT-3`, `BR-FR-04_EXT-FR-FE-02`, `BR-FR-04_EXT-FR-FE-137`.

## Related rules

- [BR-FR-CO-04](../BR-FR-CO-04/): a corrective invoice must cite exactly one earlier invoice.
- [BR-FR-CO-05](../BR-FR-CO-05/): a credit note must refer to the invoice it corrects.
