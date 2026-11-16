# Plus d'une pièce jointe est décrite LISIBLE

Deux pièces jointes ou plus sont décrites LISIBLE.

## Ce que vérifie la règle

Une pièce jointe décrite LISIBLE est la version lisible de la facture, par exemple un PDF joint à une facture XML. La règle n'en admet qu'une par facture.

## Pourquoi c'est important

BR-FR-18 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Gardez une seule pièce jointe LISIBLE : la copie lisible de la facture elle-même.
2. Décrivez les autres pièces jointes avec leur propre code, comme DOCUMENT_ANNEXE ou BON_LIVRAISON.
3. Si votre logiciel marque toutes les pièces jointes LISIBLE, signalez-le à son éditeur en citant BR-FR-18.

## Causes fréquentes

- **Le PDF lisible joint deux fois.**
- **Toutes les pièces jointes décrites LISIBLE** par défaut.

## Détails techniques

La règle compte les documents justificatifs (groupe BG-24) dont la description BT-123 vaut `LISIBLE` : au plus un.

## Texte officiel

> Il ne peut y avoir **qu’un seul** document additionnel (BG-24) dont la description (BT-123) est "LISIBLE".

BR-FR-18, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-18_BT-123`.

## Règles voisines

- [BR-FR-17](../BR-FR-17/) : les codes admis pour décrire une pièce jointe.
