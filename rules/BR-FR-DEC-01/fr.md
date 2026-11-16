# Un montant a plus de 2 décimales ou un format invalide

Un montant de la facture a plus de 2 décimales, une virgule, ou trop de chiffres.

## Ce que vérifie la règle

La règle vérifie le format des montants de la facture : totaux, montants des lignes, remises et frais, bases et montants de TVA. Chacun doit :

- avoir au plus 2 décimales (`1230.00`, pas `1230.000`) ;
- utiliser un point comme séparateur décimal, pas une virgule ;
- compter au plus 19 caractères, séparateur non compris.

Le signe moins est autorisé.

## Pourquoi c'est important

BR-FR-DEC-01 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez l'arrondi des montants dans votre logiciel : au centime.
2. Vérifiez que les montants sont exportés avec un point et sans séparateur de milliers.
3. Si votre logiciel exporte plus de décimales ou une virgule, signalez-le à son éditeur en citant BR-FR-DEC-01.

## Causes fréquentes

- **Un montant non arrondi après un calcul** (prix × quantité, remise en pourcentage).
- **Une virgule décimale** (`1230,00`).
- **Un séparateur de milliers** (`1 230.00`).

## Détails techniques

Format : décimal, au plus 19 chiffres dont 2 décimales, séparateur point, signe moins facultatif en tête. Montants contrôlés : BT-92, BT-93, BT-99, BT-100 (remises et frais du document), BT-106 à BT-117 (totaux et récapitulatif de TVA), BT-131 (montant net de ligne), BT-136, BT-137, BT-141, BT-142 (remises et frais de ligne). La plupart de ces montants échouent aussi à une règle EN 16931 BR-DEC.

## Texte officiel

> Le montant « […] » est invalide. Il doit comporter au plus 2 décimales, être exprimé avec un point comme séparateur, et ne pas dépasser 19 caractères (hors séparateur). Le signe « - » est autorisé.

BR-FR-DEC-01, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-DEC-01_BT-106`, `BR-FR-DEC-01_BT-107`, `BR-FR-DEC-01_BT-108`, `BR-FR-DEC-01_BT-109`, `BR-FR-DEC-01_BT-110`, `BR-FR-DEC-01_BT-111`, `BR-FR-DEC-01_BT-112`, `BR-FR-DEC-01_BT-113`, `BR-FR-DEC-01_BT-114`, `BR-FR-DEC-01_BT-115`, `BR-FR-DEC-01_BT-116`, `BR-FR-DEC-01_BT-117`, `BR-FR-DEC-01_BT-131`, `BR-FR-DEC-01_BT-136_BT-141`, `BR-FR-DEC-01_BT-137_BT-142`, `BR-FR-DEC-01_BT-92_BT-99`, `BR-FR-DEC-01_BT-93_BT-100`.

## Règles voisines

- [BR-FR-DEC-02](../BR-FR-DEC-02/) : les quantités : 4 décimales au plus.
- [BR-FR-DEC-03](../BR-FR-DEC-03/) : les prix unitaires : 6 décimales au plus.
- [BR-FR-DEC-04](../BR-FR-DEC-04/) : les taux de TVA : 2 décimales au plus, positifs.
