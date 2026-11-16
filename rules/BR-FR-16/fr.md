# Le taux de TVA n'est pas un taux admis en France

Un taux de TVA de la facture ne figure pas dans la liste des taux admis en France, ou il est écrit avec le signe %.

## Ce que vérifie la règle

La règle vérifie chaque taux de TVA de la facture (lignes, remises et frais, récapitulatif de TVA). Il doit :

- être écrit en nombre, sans le signe % (`20`, pas `20 %`) ;
- figurer dans la liste des fichiers officiels : 0, 0.9, 1.05, 1.75, 2.1, 5.5, 7, 8.5, 9.2, 9.6, 10, 13, 19.6, 20 et 20.6 ;
- avoir au plus deux décimales (`20`, `20.0` ou `20.00`).

## Pourquoi c'est important

BR-FR-16 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez le taux appliqué dans votre logiciel : un taux étranger (comme 21) ou une faute de frappe est refusé.
2. Écrivez le taux sans le signe %, avec au plus deux décimales.
3. Si votre logiciel exporte un taux arrondi ou mal formaté, signalez-le à son éditeur en citant BR-FR-16.

## Causes fréquentes

- **Un taux d'un autre pays**, comme 21.
- **Le signe % dans la valeur.**
- **Un taux calculé**, comme 19.99, au lieu d'un taux choisi.
- **Trop de décimales** (`20.000`).

## Détails techniques

Taux BT-152 (lignes), BT-96 et BT-103 (remises et frais du document), BT-119 (récapitulatif de TVA) : `ram:RateApplicablePercent` en CII. Un taux absent n'est pas contrôlé par cette règle.

## Texte officiel

> Le taux de TVA (BT-96) doit être exprimé en pourcentage sans symbole « % » et faire partie des valeurs autorisées.

BR-FR-16, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-16_BT-103`, `BR-FR-16_BT-119`, `BR-FR-16_BT-152`, `BR-FR-16_BT-96`, `BR-FR-16_BT-96_BT-103`.

## Règles voisines

- [BR-FR-15](../BR-FR-15/) : les catégories de TVA admises en France.
- [BR-FR-DEC-04](../BR-FR-DEC-04/) : le format d'un taux de TVA : positif, deux décimales au plus.
