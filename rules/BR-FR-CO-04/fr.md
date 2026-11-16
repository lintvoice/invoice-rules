# Une facture rectificative ne cite pas exactement une facture antérieure

Une facture rectificative ne cite aucune facture antérieure, ou en cite plusieurs, ou en cite une sans sa date.

## Ce que vérifie la règle

Une facture rectificative (types 384, 471, 472 et 473) corrige une facture précise. Elle doit citer exactement une facture antérieure, avec :

- son numéro ;
- sa date d'émission.

Aucune référence, ou plusieurs, sont refusées.

## Pourquoi c'est important

BR-FR-CO-04 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Sur la facture rectificative, indiquez le numéro et la date de la facture qu'elle corrige.
2. Pour corriger plusieurs factures, émettez une facture rectificative pour chacune.
3. Si votre logiciel envoie le numéro sans la date, signalez-le à son éditeur en citant BR-FR-CO-04.

## Causes fréquentes

- **La facture corrigée n'est pas citée.**
- **Plusieurs factures citées** sur une même facture rectificative.
- **Un numéro cité sans sa date.**

## Détails techniques

Quand BT-3 vaut `384`, `471`, `472` ou `473` : exactement une référence à une facture antérieure (BG-3) avec BT-25 (numéro) et BT-26 (date).

## Texte officiel

> Si le type de facture (BT-3) est une facture rectificative (384, 471, 472, 473), alors **une et une seule** référence à une facture antérieure (BT-25) avec sa date (BT-26) doit être présente.

BR-FR-CO-04, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-CO-04_BT-3`, `BR-FR-CO-04_BT-4`.

## Règles voisines

- [BR-FR-CO-05](../BR-FR-CO-05/) : un avoir doit citer la facture qu'il corrige.
- [BR-FR-04](../BR-FR-04/) : les types de document admis en France.
