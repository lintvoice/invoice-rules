# La catégorie de TVA n'est pas admise en France

Une ligne, une remise ou des frais, ou le récapitulatif de TVA utilise un code de catégorie de TVA non admis en France.

## Ce que vérifie la règle

Chaque ligne, chaque remise ou frais du document et chaque sous-total de TVA indiquent une catégorie de TVA, sous forme de code. En France, seuls ces codes sont admis :

- **S** : TVA à un taux positif ;
- **Z** : taux zéro ;
- **E** : exonération ;
- **AE** : autoliquidation ;
- **K** : livraison intracommunautaire ;
- **G** : exportation hors de l'Union européenne ;
- **O** : hors du champ de la TVA.

Les codes L et M, propres aux îles Canaries et à Ceuta et Melilla, sont refusés.

## Pourquoi c'est important

BR-FR-15 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez la catégorie de TVA de vos articles, remises et frais dans votre logiciel.
2. Remplacez L ou M par la catégorie de l'opération, par exemple S pour une vente avec TVA française.
3. Si votre logiciel ne propose aucune catégorie admise, signalez-le à son éditeur en citant BR-FR-15.

## Causes fréquentes

- **Un code choisi par erreur** dans une liste qui contient tous les codes européens.
- **Un paramétrage fait pour l'Espagne** réutilisé pour la France.
- **Une remise ou des frais** dont la catégorie n'a pas été mise à jour.

## Détails techniques

Codes de catégorie de TVA (sous-ensemble UNCL 5305 de la norme EN 16931) : BT-151 sur les lignes, BT-95 et BT-102 pour les remises et frais du document, BT-118 dans le récapitulatif de TVA. Les identifiants terminés par `_LM` signalent les codes L et M ; les autres, un code hors liste. En UBL, le contrôle des lignes est publié sous `BR-FR-08_BT-151-2`.

## Texte officiel

> Code de catégorie de TVA invalide.

BR-FR-15, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-15_BT-118-1`, `BR-FR-15_BT-118-2`, `BR-FR-15_BT-151-1`, `BR-FR-15_BT-95_BT-102`, `BR-FR-15_BT-95_BT-102-1`, `BR-FR-15_BT-95_BT-102-2`, `BR-FR-15_BT-95_BT-102_LM`, `BR-FR-15_BT-95_BT-118`, `BR-FR-15_BT-95_BT-118_LM`, `BR-FR-15_BT-95_BT-151`, `BR-FR-15_BT-95_BT-151_LM`.

## Règles voisines

- [BR-FR-16](../BR-FR-16/) : les taux de TVA admis en France.
