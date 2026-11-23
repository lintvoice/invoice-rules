# The invoice has more than one BAR note

The invoice contains two or more notes coded BAR.

## What the rule checks

The note coded BAR says how the invoice is to be handled (B2B, B2C…). An invoice can have only one way of being handled: the rule allows a single BAR note.

## Why it matters

BR-FR-31 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Keep the BAR note that matches the operation and delete the others.
2. If your software adds a BAR note on top of yours, report it to the software's publisher, quoting BR-FR-31.

## Common causes

- **A BAR note typed by hand** on top of the one the software adds.
- **Two values for a mixed operation**, sent as two notes.

## Technical details

Notes (BG-1) whose subject code BT-21 is `BAR`: at most one. In the UBL rule file, this check carries the id `BR-FR-30_BT-21`, although its message names BR-FR-31.

## Official text

> Lorsque plusieurs notes ont le code sujet « BAR » (BT-21), Il ne peut y avoir qu'une seule valeur associée (BT-22, contenu de la note) parmi l’une des suivantes : B2B, B2BINT, B2C, OUTOFSCOPE, ARCHIVEONLY.

BR-FR-31, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-31_BT-21`, `BR-FR-30_BT-21`.

## Related rules

- [BR-FR-20](../BR-FR-20/): the values allowed in the BAR note.
