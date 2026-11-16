# A coded statement appears more than once

The invoice contains two notes with the same code: PMT, PMD, AAB or TXD.

## What the rule checks

Four coded statements may appear only once each in the invoice notes:

- **PMT**: the fixed indemnity for recovery costs;
- **PMD**: the late-payment penalties;
- **AAB**: the early-payment discount or its absence;
- **TXD**: a statement about tax.

If the information takes several sentences, they go in the same note.

## Why it matters

BR-FR-06 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Find the duplicated statement: the validation report gives its code.
2. Merge the two notes into one, or delete the extra one.
3. If your software adds a statement automatically that you also typed, report it to the software's publisher, quoting BR-FR-06.

## Common causes

- **A statement typed by hand on top of the one the software adds.**
- **A long statement split into several notes** with the same code.
- **An invoice template that repeats the payment terms.**

## Technical details

Notes BG-1, subject code BT-21. In CII, at most one `ram:IncludedNote` per `ram:SubjectCode` among `PMT`, `PMD`, `AAB` and `TXD`. In UBL, at most one occurrence each of `#PMT#`, `#PMD#`, `#AAB#` and `#TXD#` across the notes.

## Official text

> Le code sujet PMT (indemnité forfaitaire pour frais de recouvrement) ne doit apparaître qu'une seule fois dans les notes (BG-1).

BR-FR-06, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-06_BT-21-1`, `BR-FR-06_BT-21-2`, `BR-FR-06_BT-21-3`, `BR-FR-06_BT-21-4`, `BR-FR-06_BT-21_AAB`, `BR-FR-06_BT-21_PMD`, `BR-FR-06_BT-21_PMT`, `BR-FR-06_BT-21_TXD`.

## Related rules

- [BR-FR-05](../BR-FR-05/): the PMT, PMD and AAB statements are mandatory.
