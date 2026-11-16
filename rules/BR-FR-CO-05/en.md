# A credit note does not cite the invoice it corrects

A credit note does not say which invoice it corrects.

## What the rule checks

A credit note (types 261, 381, 396, 502 and 503) must say which invoice it corrects:

- either at the top, at least one earlier invoice with its number and date;
- or on each line, the invoice that line corrects.

## Why it matters

BR-FR-CO-05 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. On the credit note, enter the number and the date of the original invoice.
2. If the credit note covers several invoices, cite them all at the top, or give on each line the invoice it corrects.
3. If your software creates credit notes with no link to the invoice, report it to the software's publisher, quoting BR-FR-CO-05.

## Common causes

- **A credit note created from scratch**, with no link to the original invoice.
- **A number cited without its date.**
- **A credit note on several invoices** where some lines have no reference.

## Technical details

Types BT-3: 261, 381, 396, 502, 503. At document level: BT-25 with BT-26 (BG-3). On lines: the line's invoice reference (EXT-FR-FE-136, with its date EXT-FR-FE-138), required on every line with no sub-type (EXT-FR-FE-163) or with sub-type `DETAIL`.

## Official text

> Si le type de facture (BT-3) est un avoir (261, 381, 396, 502, 503), alors : - soit au moins une référence à une facture antérieure (BT-25) avec sa date (BT-26) doit être présente au niveau entête, - soit chaque ligne (BG-25) sans subtype (EXT-FR-FE-163) ou avec subtype 'DETAIL' doit contenir une référence à une facture antérieure (EXT-FR-FE-136) avec sa date (EXT-FR-FE-138).

BR-FR-CO-05, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-CO-05_BT-3`.

## Related rules

- [BR-FR-CO-04](../BR-FR-CO-04/): a corrective invoice cites exactly one earlier invoice.
- [BR-FR-01](../BR-FR-01/): a cited invoice number is at most 35 characters.
