# Un taux de TVA a plus de 2 décimales ou est négatif

Un taux de TVA de la facture a plus de 2 décimales, un signe moins, ou trop de chiffres.

## Ce que vérifie la règle

La règle vérifie le format de chaque taux de TVA (lignes, remises et frais du document, récapitulatif de TVA). Chacun doit :

- être positif, sans signe moins ;
- avoir au plus 2 décimales (`20.00`, pas `20.000`) ;
- compter au plus 4 caractères, séparateur non compris.

## Pourquoi c'est important

BR-FR-DEC-04 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez comment votre logiciel écrit les taux de TVA : `20` ou `20.00`.
2. Écrivez le taux sans le signe %.
3. Si votre logiciel ajoute des décimales, signalez-le à son éditeur en citant BR-FR-DEC-04.

## Causes fréquentes

- **Un taux écrit avec 3 décimales** (`20.000`).
- **Un taux calculé** avec de nombreuses décimales.
- **Un taux négatif** utilisé pour une correction.

## Détails techniques

Taux BT-96, BT-103 (remises et frais du document), BT-119 (récapitulatif de TVA) et BT-152 (lignes), `ram:RateApplicablePercent` en CII. Un taux écrit `20.000` échoue aussi à BR-FR-16, dont la liste ne contient que les formes à 2 décimales au plus.

## Texte officiel

> Le taux de TVA « […] » est invalide. Il doit : - être un nombre strictement positif (sans signe « - »), - comporter au plus 2 décimales (séparateur « . »), - contenir au maximum 4 caractères (hors séparateur).

BR-FR-DEC-04, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-DEC-04_BT-119`, `BR-FR-DEC-04_BT-152`, `BR-FR-DEC-04_BT-96_BT-103`.

## Règles voisines

- [BR-FR-DEC-01](../BR-FR-DEC-01/) : les montants : 2 décimales au plus.
- [BR-FR-DEC-02](../BR-FR-DEC-02/) : les quantités : 4 décimales au plus.
- [BR-FR-DEC-03](../BR-FR-DEC-03/) : les prix unitaires : 6 décimales au plus.
- [BR-FR-16](../BR-FR-16/) : les taux de TVA admis en France.
