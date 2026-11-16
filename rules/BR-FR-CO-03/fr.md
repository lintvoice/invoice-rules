# Un avoir de remise globale n'indique pas le contrat ou la période

Un document de type 262 n'indique pas de numéro de contrat, ou pas les deux dates de la période couverte.

## Ce que vérifie la règle

Le type 262 désigne un avoir de remise globale. Un tel avoir doit indiquer :

- le numéro du contrat concerné ;
- la période qu'il couvre, avec une date de début et une date de fin.

## Pourquoi c'est important

BR-FR-CO-03 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Sur l'avoir, indiquez le numéro du contrat auquel la remise se rapporte.
2. Indiquez la période couverte, avec sa date de début et sa date de fin.
3. Si votre logiciel n'offre pas de champ de contrat ou de période pour les avoirs, signalez-le à son éditeur en citant BR-FR-CO-03.

## Causes fréquentes

- **Un avoir créé sans contrat associé.**
- **Une période avec seulement une date de début.**

## Détails techniques

Quand le type de document BT-3 vaut `262` : la référence de contrat BT-12 et la période de facturation BG-14 (début BT-73, fin BT-74) doivent être présentes.

## Texte officiel

> Si le code type de la facture (BT-3) est égal à 262 (Avoir Remise Globale), alors : - Le numéro de contrat (BT-12) doit être présent - La période de facturation (BG-14) doit être renseignée (dates de début et de fin).

BR-FR-CO-03, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-CO-03_BT-3`.

## Règles voisines

- [BR-FR-04](../BR-FR-04/) : les types de document admis en France.
- [BR-FR-CO-05](../BR-FR-CO-05/) : les autres avoirs doivent citer la facture qu'ils corrigent.
