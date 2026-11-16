# Une quantité a plus de 4 décimales

Une quantité de la facture a plus de 4 décimales ou un format invalide.

## Ce que vérifie la règle

La règle vérifie la quantité facturée de chaque ligne, et la quantité de base de son prix (par exemple, un prix pour 100 unités). Chacune doit :

- avoir au plus 4 décimales ;
- utiliser un point comme séparateur décimal ;
- compter au plus 19 caractères, séparateur non compris.

Le signe moins est autorisé.

## Pourquoi c'est important

BR-FR-DEC-02 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Arrondissez les quantités à 4 décimales au plus dans votre logiciel.
2. Pour une quantité dans une petite unité, comme le gramme, préférez une unité plus grande, comme le kilogramme, à de nombreuses décimales.
3. Si votre logiciel exporte plus de décimales, signalez-le à son éditeur en citant BR-FR-DEC-02.

## Causes fréquentes

- **Une quantité calculée par division** (comme 1/3) et non arrondie.
- **Une conversion d'unités** qui ajoute des décimales.
- **Une virgule décimale.**

## Détails techniques

Quantités BT-129 (quantité facturée, `ram:BilledQuantity`) et BT-149 (quantité de base du prix, `ram:BasisQuantity`) : décimal, au plus 19 chiffres dont 4 décimales.

## Texte officiel

> La quantité « […] » est invalide. Elle doit : - être un nombre avec au plus 4 décimales (séparateur « . »), - contenir au maximum 19 caractères (hors séparateur), - et peut commencer par un signe « - ».

BR-FR-DEC-02, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-DEC-02_BT-129`, `BR-FR-DEC-02_BT-149`.

## Règles voisines

- [BR-FR-DEC-01](../BR-FR-DEC-01/) : les montants : 2 décimales au plus.
- [BR-FR-DEC-03](../BR-FR-DEC-03/) : les prix unitaires : 6 décimales au plus.
- [BR-FR-DEC-04](../BR-FR-DEC-04/) : les taux de TVA : 2 décimales au plus, positifs.
