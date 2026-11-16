# The invoice number is longer than 35 characters

The invoice number, or the number of an invoice it refers to, is longer than 35 characters.

## What the rule checks

The rule limits to 35 characters:

- the invoice number;
- the number of an earlier invoice it refers to, such as the invoice a credit note corrects, at the top of the invoice or on a line.

## Why it matters

BR-FR-01 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. In your invoicing software, check the numbering format: prefix, year and counter together must fit in 35 characters.
2. If the invoice refers to an earlier invoice (credit note, corrective invoice), check the length of that number too.
3. If your software adds a prefix or a suffix when it exports the invoice, report it to the software's publisher, quoting BR-FR-01.

## Common causes

- **A long prefix** added to the number, such as the company or department name.
- **An order or case number joined to the invoice number.**
- **An earlier invoice cited with a long reference**, such as its full title instead of its number.

## Technical details

The invoice number is BT-1; the number of an earlier invoice is BT-25 at document level and EXT-FR-FE-136 on a line (French extension). In UBL, the official files also check under this code that these numbers use only allowed characters, which BR-FR-02 checks in CII.

## Official text

> L'identifiant de facture (ram:ID) ne doit pas dépasser 35 caractères.

BR-FR-01, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-01_BT-1`, `BR-FR-01_BT-1-1`, `BR-FR-01_BT-1-2`, `BR-FR-01_BT-25`, `BR-FR-01_BT-25-1`, `BR-FR-01_BT-25-2`, `BR-FR-01_EXT-FR-FE-136`, `BR-FR-01_EXT-FR-FE-136-1`, `BR-FR-01_EXT-FR-FE-136-2`.

## Related rules

- [BR-FR-02](../BR-FR-02/): the characters allowed in an invoice number.
- [BR-FR-CO-05](../BR-FR-CO-05/): a credit note must refer to the invoice it corrects.
