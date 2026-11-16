# Un SIREN de la facture n'a pas 9 chiffres

Un identifiant déclaré avec le code de schéma 0002 ou 0231 n'a pas exactement 9 chiffres.

## Ce que vérifie la règle

La règle vérifie tous les identifiants de la facture déclarés avec :

- le code de schéma 0002, qui désigne le SIREN ;
- le code 0231, utilisé pour un membre d'un assujetti unique (un groupe TVA).

Chacun doit compter exactement 9 chiffres, sans espace ni lettre, quelle que soit la partie : vendeur, acheteur, bénéficiaire, lieu de livraison…

## Pourquoi c'est important

BR-FR-32 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Repérez la partie en cause dans le rapport de validation.
2. Corrigez son SIREN dans votre logiciel : 9 chiffres, sans espace ; pas le SIRET (14 chiffres).
3. Si le SIREN est juste et que l'erreur persiste, signalez-le à l'éditeur de votre logiciel en citant BR-FR-32.

## Causes fréquentes

- **Un SIRET déclaré avec le schéma 0002.**
- **Des espaces dans le SIREN.**
- **Un SIREN auquel il manque un chiffre.**

## Détails techniques

Deux contrôles : tout `ram:SpecifiedLegalOrganization/ram:ID` au `schemeID="0002"` (`BR-FR-32-LEGALID`), et tout `ram:GlobalID` au `schemeID` `0002` ou `0231` (`BR-FR-32-GLOBALID`), pour toute partie de la facture. Expression : `^\d{9}$`.

## Texte officiel

> Tout identifiant légal d'une Partie avec schemeID = '0002' DOIT être composé de 9 chiffres.

BR-FR-32, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-32-GLOBALID`, `BR-FR-32-ID`, `BR-FR-32-LEGALID`.

## Règles voisines

- [BR-FR-10](../BR-FR-10/) : le SIREN du vendeur est obligatoire.
- [BR-FR-09](../BR-FR-09/) : un SIRET commence par le SIREN de sa partie.
