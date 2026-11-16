# Un identifiant privé dépasse 100 caractères

Un identifiant de vendeur ou d'acheteur déclaré avec le code de schéma 0224 compte plus de 100 caractères.

## Ce que vérifie la règle

L'identifiant privé du vendeur ou de l'acheteur, déclaré avec le code de schéma 0224, est limité à 100 caractères.

## Pourquoi c'est important

BR-FR-26 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez l'identifiant privé dans la fiche du vendeur ou du client.
2. Raccourcissez-le : une référence courte, comme un numéro de client, suffit.
3. Si votre logiciel fabrique un identifiant long à l'export, signalez-le à son éditeur en citant BR-FR-26.

## Causes fréquentes

- **Un nom ou une adresse utilisé comme identifiant.**
- **Plusieurs références réunies** dans un seul identifiant.

## Détails techniques

Identifiant du vendeur BT-29 et de l'acheteur BT-46 (`ram:GlobalID` en CII) au schéma `0224` : au plus 100 caractères.

## Texte officiel

> L'identifiant privé (ram:GlobalID) dépasse 100 caractères.

BR-FR-26, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-26_BT-29`, `BR-FR-26_BT-46`.

## Règles voisines

- [BR-FR-24](../BR-FR-24/) : les caractères admis dans un identifiant privé.
