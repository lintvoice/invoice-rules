# L'adresse électronique dépasse 125 caractères

Une adresse électronique de la facture compte plus de 125 caractères.

## Ce que vérifie la règle

La règle limite à 125 caractères l'adresse électronique de chaque partie : vendeur, acheteur, bénéficiaire, agents, payeur, facturé, facturant, quel que soit le code de schéma.

## Pourquoi c'est important

BR-FR-25 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez l'adresse dans la fiche de la partie : un texte collé par erreur n'est pas une adresse.
2. Remplacez-la par l'adresse de facturation électronique de la partie.
3. Si votre logiciel assemble plusieurs champs dans l'adresse, signalez-le à son éditeur en citant BR-FR-25.

## Causes fréquentes

- **Une note ou un commentaire collé** dans le champ de l'adresse.
- **Plusieurs adresses réunies** dans un seul champ.

## Détails techniques

Adresses électroniques du vendeur (BT-34), acheteur (BT-49), et parties de l'extension française : agent de l'acheteur, bénéficiaire, payeur, agent du vendeur, facturé et facturant (EXT-FR-FE-12, -29, -52, -75, -98, -121) (`ram:URIUniversalCommunication/ram:URIID` en CII) : au plus 125 caractères.

## Texte officiel

> L'adresse électronique (ram:URIID) dépasse 125 caractères.

BR-FR-25, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-25_BT-34`, `BR-FR-25_BT-49`, `BR-FR-25_EXT-FR-FE-12`, `BR-FR-25_EXT-FR-FE-121`, `BR-FR-25_EXT-FR-FE-29`, `BR-FR-25_EXT-FR-FE-52`, `BR-FR-25_EXT-FR-FE-75`, `BR-FR-25_EXT-FR-FE-98`.

## Règles voisines

- [BR-FR-23](../BR-FR-23/) : les caractères admis dans une adresse électronique.
