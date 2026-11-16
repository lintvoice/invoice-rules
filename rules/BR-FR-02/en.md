# The invoice number contains a character that is not allowed

The invoice number, or the number of an invoice it refers to, contains a space or a character other than letters, digits and + - _ /.

## What the rule checks

The invoice number, and the number of any earlier invoice it refers to, may contain only:

- letters without accents and digits;
- the signs `+`, `-`, `_` and `/`.

Spaces, dots, accented letters and other signs are refused.

## Why it matters

BR-FR-02 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. In your software, remove spaces, dots, accents and other signs from the numbering: keep letters, digits and + - _ /.
2. For example, `INV 2026.001` becomes `INV-2026-001`.
3. For a credit note or a corrective invoice, cite the original invoice with a number in the same format.

## Common causes

- **A space in the number**, such as `INV 2026-001`.
- **A dot or a colon** used as a separator.
- **An accented letter** in a prefix.
- **A number typed by hand** with signs the software would not have used.

## Technical details

Checked on the invoice number (BT-1), the number of an earlier invoice (BT-25) and the same number on a line (EXT-FR-FE-136). The accepted format is the pattern `^[A-Za-z0-9+\-_/]+$`. In UBL, the official files publish this check under BR-FR-01.

## Official text

> L'identifiant de facture (ram:ID) contient des caractères non autorisés.

BR-FR-02, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-02_BT-1`, `BR-FR-02_BT-25`, `BR-FR-02_EXT-FR-FE-136`.

## Related rules

- [BR-FR-01](../BR-FR-01/): an invoice number is at most 35 characters long.
