# A global discount credit note does not give the contract or the period

A document of type 262 does not give a contract number, or not both dates of the period it covers.

## What the rule checks

Type 262 stands for a global discount credit note. Such a credit note must give:

- the number of the contract concerned;
- the period it covers, with a start date and an end date.

## Why it matters

BR-FR-CO-03 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. On the credit note, enter the number of the contract the discount relates to.
2. Enter the period covered, with both its start and end dates.
3. If your software offers no contract or period field for credit notes, report it to the software's publisher, quoting BR-FR-CO-03.

## Common causes

- **A credit note created without a linked contract.**
- **A period with only a start date.**

## Technical details

When the document type BT-3 is `262`: contract reference BT-12 and invoicing period BG-14 (start BT-73, end BT-74) must be present.

## Official text

> Si le code type de la facture (BT-3) est égal à 262 (Avoir Remise Globale), alors : - Le numéro de contrat (BT-12) doit être présent - La période de facturation (BG-14) doit être renseignée (dates de début et de fin).

BR-FR-CO-03, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-CO-03_BT-3`.

## Related rules

- [BR-FR-04](../BR-FR-04/): the document types allowed in France.
- [BR-FR-CO-05](../BR-FR-CO-05/): other credit notes must cite the invoice they correct.
