# Le type d'une pièce jointe n'est pas dans la liste française

Une pièce jointe de la facture est décrite par un code absent de la liste française.

## Ce que vérifie la règle

Chaque document joint à la facture est décrit par un code qui dit ce qu'il est. Les règles françaises n'admettent que ces codes, écrits exactement ainsi : RIB, LISIBLE, FEUILLE_DE_STYLE, PJA, BORDEREAU_SUIVI, DOCUMENT_ANNEXE, BON_LIVRAISON, BON_COMMANDE, BORDEREAU_SUIVI_VALIDATION, ETAT_ACOMPTE, FACTURE_PAIEMENT_DIRECT, RECAPITULATIF_COTRAITANCE.

## Pourquoi c'est important

BR-FR-17 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez comment votre logiciel décrit les pièces jointes : RIB, bon de livraison, bon de commande…
2. Utilisez le code de la liste qui correspond, par exemple BON_LIVRAISON pour un bon de livraison, ou DOCUMENT_ANNEXE pour un autre document.
3. Si votre logiciel écrit ses propres descriptions, signalez-le à son éditeur en citant BR-FR-17.

## Causes fréquentes

- **Une description libre**, comme le nom du fichier, au lieu d'un code.
- **Un code écrit autrement**, comme `Bon de commande` ou `BON-COMMANDE`.
- **Un code venu d'un autre système.**

## Détails techniques

La règle lit la description BT-123 des documents justificatifs (groupe BG-24) de code type `916` (`ram:AdditionalReferencedDocument` en CII). Une description absente n'est pas contrôlée par cette règle.

## Texte officiel

> Le code de qualification de la pièce jointe "[…]" est invalide. Il doit appartenir à la liste des codes autorisés.

BR-FR-17, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-17_BT-123`.

## Règles voisines

- [BR-FR-18](../BR-FR-18/) : une seule pièce jointe peut être LISIBLE.
