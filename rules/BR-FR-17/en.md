# The type of an attachment is not on the French list

An attachment to the invoice is described with a code that is not on the French list.

## What the rule checks

Each document attached to the invoice is described by a code that says what it is. The French rules allow only these codes, written exactly like this: RIB, LISIBLE, FEUILLE_DE_STYLE, PJA, BORDEREAU_SUIVI, DOCUMENT_ANNEXE, BON_LIVRAISON, BON_COMMANDE, BORDEREAU_SUIVI_VALIDATION, ETAT_ACOMPTE, FACTURE_PAIEMENT_DIRECT, RECAPITULATIF_COTRAITANCE.

## Why it matters

BR-FR-17 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check how your software describes the attachments: bank details, delivery note, purchase order…
2. Use the code from the list that matches, for example BON_LIVRAISON for a delivery note, or DOCUMENT_ANNEXE for another document.
3. If your software writes its own descriptions, report it to the software's publisher, quoting BR-FR-17.

## Common causes

- **A free description**, such as the file name, instead of a code.
- **A code with a different spelling**, such as `Bon de commande` or `BON-COMMANDE`.
- **A code from another system.**

## Technical details

The rule reads the description BT-123 of the supporting documents (group BG-24) whose type code is `916` (`ram:AdditionalReferencedDocument` in CII). A missing description is not checked by this rule.

## Official text

> Le code de qualification de la pièce jointe "[…]" est invalide. Il doit appartenir à la liste des codes autorisés.

BR-FR-17, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-17_BT-123`.

## Related rules

- [BR-FR-18](../BR-FR-18/): only one attachment may be LISIBLE.
