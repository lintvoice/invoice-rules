# L'adresse électronique de l'acheteur manque

La facture n'indique pas l'adresse électronique de l'acheteur.

## Ce que vérifie la règle

L'adresse électronique de l'acheteur est l'adresse à laquelle ses factures lui sont remises. Ce n'est pas forcément un e-mail. La règle l'exige sur chaque facture.

## Pourquoi c'est important

BR-FR-12 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Demandez à votre client son adresse de facturation électronique.
2. Renseignez-la dans la fiche client de votre logiciel.
3. Si votre logiciel n'a pas ce champ, signalez-le à son éditeur en citant BR-FR-12.

## Causes fréquentes

- **La fiche client n'a qu'un e-mail ou une adresse postale**, pas d'adresse de facturation électronique.
- **Le logiciel n'envoie pas ce champ** dans la facture électronique.

## Détails techniques

BT-49, adresse électronique de l'acheteur, avec son schéma BT-49-1 : `ram:URIUniversalCommunication/ram:URIID` (attribut `schemeID`) de la partie acheteur en CII, `cbc:EndpointID` en UBL.

## Texte officiel

> Le BT-49 est obligatoire.

BR-FR-12, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-12_BT-49`.

## Règles voisines

- [BR-FR-13](../BR-FR-13/) : l'adresse électronique du vendeur est obligatoire aussi.
- [BR-FR-21](../BR-FR-21/) : sur une facture B2B, elle commence par le SIREN de l'acheteur.
- [BR-FR-23](../BR-FR-23/) : les caractères admis dans une adresse électronique.
