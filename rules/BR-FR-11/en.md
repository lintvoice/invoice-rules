# The buyer's SIREN is missing on a business-to-business invoice

The invoice is declared B2B, but the buyer's SIREN is missing or does not have 9 digits.

## What the rule checks

A note on the invoice, coded BAR, gives the type of operation: B2B (between businesses), B2C (to consumers), and so on. When it is B2B, the rule requires the buyer's SIREN: 9 digits, no spaces or letters.

## Why it matters

BR-FR-11 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

The reform relies on platforms approved by the State and on a directory of invoice recipients run by the administration ([DGFiP press release, 16 January 2026, in French](https://presse.economie.gouv.fr/facturation-electronique-la-direction-generale-des-finances-publiques-publie-la-liste-des-101-premieres-plateformes-agreees/)): the SIREN identifies the company that receives the invoice.

## How to fix it

1. In your software's customer record, enter the buyer's SIREN: 9 digits, no spaces.
2. You find it on the customer's invoices, its company registration or the State's company directory ([annuaire-entreprises.data.gouv.fr](https://annuaire-entreprises.data.gouv.fr/)).
3. If the customer is a private person, the invoice must not be declared B2B: check the BAR note.

## Common causes

- **The customer record has no SIREN.**
- **The SIRET (14 digits) is entered instead of the SIREN.**
- **A private customer invoiced as a business**: the BAR note says B2B by mistake.

## Technical details

The operation type is a note (BG-1) with subject code `BAR` (BT-21) and its value in the note text (BT-22). The buyer's SIREN is BT-47, the buyer's legal registration identifier with scheme `0002`.

## Official text

> Si une note contient le code sujet BAR avec la valeur 'B2B', alors le SIREN de l’acheteur (BT-47, ram:ID) est obligatoire et doit être composé exactement de 9 chiffres.

BR-FR-11, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-11_BT-47`.

## Related rules

- [BR-FR-10](../BR-FR-10/): the seller's SIREN is mandatory.
- [BR-FR-20](../BR-FR-20/): the values allowed in the BAR note.
- [BR-FR-21](../BR-FR-21/): on a B2B invoice, the buyer's electronic address starts with its SIREN.
