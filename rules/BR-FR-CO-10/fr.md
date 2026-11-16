# Un identifiant de partie n'a pas de schéma, ou un schéma est répété

Un identifiant d'une partie n'a pas de code de schéma, ou la partie a deux identifiants du même schéma.

## Ce que vérifie la règle

Une partie (vendeur, acheteur, bénéficiaire, lieu de livraison…) peut avoir des identifiants, chacun avec un code de schéma qui dit ce qu'il est : 0009 pour un SIRET, 0088 pour un GLN, 0224 pour un identifiant privé… La règle vérifie que :

- chaque identifiant a son code de schéma ;
- une même partie n'a pas deux identifiants du même schéma.

## Pourquoi c'est important

BR-FR-CO-10 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Dans la fiche de la partie, vérifiez que chaque identifiant a son type.
2. Supprimez les identifiants répétés : gardez par exemple un seul SIRET par partie.
3. Si votre logiciel envoie les identifiants sans leur schéma, signalez-le à son éditeur en citant BR-FR-CO-10.

## Causes fréquentes

- **Un identifiant saisi sans son type.**
- **Deux SIRET pour une même partie**, par exemple un ancien et un nouvel établissement.

## Détails techniques

Identifiants globaux `ram:GlobalID` et leur attribut `schemeID` : BT-29 (vendeur), BT-46 (acheteur), BT-60 (bénéficiaire), BT-71 (livraison) et parties de l'extension française. Identifiants terminés par `-1` : schéma absent ; `-2` : schéma répété.

## Texte officiel

> Si l’identifiant global du vendeur (BT-29) est renseigné, alors son schéma (BT-29-1) doit également être renseigné.

BR-FR-CO-10, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-CO-10_BT-29-1`, `BR-FR-CO-10_BT-29-2`, `BR-FR-CO-10_BT-46-1`, `BR-FR-CO-10_BT-46-2`, `BR-FR-CO-10_BT-60-1`, `BR-FR-CO-10_BT-60-2`, `BR-FR-CO-10_BT-71-1`, `BR-FR-CO-10_BT-71-2`, `BR-FR-CO-10_EXT-FR-FE-06-1`, `BR-FR-CO-10_EXT-FR-FE-06-2`, `BR-FR-CO-10_EXT-FR-FE-115-1`, `BR-FR-CO-10_EXT-FR-FE-115-2`, `BR-FR-CO-10_EXT-FR-FE-146-1`, `BR-FR-CO-10_EXT-FR-FE-146-2`, `BR-FR-CO-10_EXT-FR-FE-46-1`, `BR-FR-CO-10_EXT-FR-FE-46-2`, `BR-FR-CO-10_EXT-FR-FE-69-1`, `BR-FR-CO-10_EXT-FR-FE-69-2`, `BR-FR-CO-10_EXT-FR-FE-92-1`, `BR-FR-CO-10_EXT-FR-FE-92-2`.

## Règles voisines

- [BR-FR-09](../BR-FR-09/) : un SIRET commence par le SIREN de sa partie.
- [BR-FR-24](../BR-FR-24/) : les caractères admis dans un identifiant privé.
