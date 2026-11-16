# Un prix unitaire a plus de 6 décimales ou est négatif

Un prix unitaire de la facture a plus de 6 décimales, un signe moins, ou trop de chiffres.

## Ce que vérifie la règle

La règle vérifie le prix unitaire net, le prix unitaire brut et la remise sur le prix unitaire de chaque article. Chacun doit :

- avoir au plus 6 décimales ;
- être positif, sans signe moins, sauf si le cadre de facturation est B9, S9 ou M9 ;
- compter au plus 19 caractères, séparateur non compris.

## Pourquoi c'est important

BR-FR-DEC-03 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Arrondissez les prix unitaires à 6 décimales au plus dans votre logiciel.
2. Pour accorder une réduction, utilisez une remise plutôt qu'un prix négatif.
3. Si votre logiciel exporte des prix négatifs ou trop précis, signalez-le à son éditeur en citant BR-FR-DEC-03.

## Causes fréquentes

- **Un prix unitaire calculé à partir d'un total** et non arrondi.
- **Un prix négatif** utilisé pour accorder une réduction sur une ligne.

## Détails techniques

Prix net BT-146, remise sur prix BT-147 et prix brut BT-148 (`ram:ChargeAmount` et `ram:AppliedTradeAllowanceCharge/ram:ActualAmount` en CII) : décimal, au plus 19 chiffres dont 6 décimales, sans signe moins sauf si BT-23 vaut `B9`, `S9` ou `M9`.

## Texte officiel

> Le montant « […] » est invalide. Il doit : - être un nombre strictement positif (sans signe « - »), sauf si Cadre de Facturation (BT-23) est S9, M9 ou B9 (bi-directionnel) - comporter au plus 6 décimales (séparateur « . »), - contenir au maximum 19 caractères (hors séparateur).

BR-FR-DEC-03, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-DEC-03_BT-146`, `BR-FR-DEC-03_BT-147`, `BR-FR-DEC-03_BT-148`.

## Règles voisines

- [BR-FR-DEC-01](../BR-FR-DEC-01/) : les montants : 2 décimales au plus.
- [BR-FR-DEC-02](../BR-FR-DEC-02/) : les quantités : 4 décimales au plus.
- [BR-FR-DEC-04](../BR-FR-DEC-04/) : les taux de TVA : 2 décimales au plus, positifs.
