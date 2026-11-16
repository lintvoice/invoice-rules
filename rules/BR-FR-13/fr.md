# L'adresse électronique du vendeur manque

La facture n'indique pas l'adresse électronique du vendeur.

## Ce que vérifie la règle

L'adresse électronique du vendeur est l'adresse à laquelle ses factures lui sont remises. Ce n'est pas forcément un e-mail. La règle l'exige sur chaque facture.

## Pourquoi c'est important

BR-FR-13 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Repérez l'adresse de facturation électronique de votre entreprise : ce n'est pas votre e-mail.
2. Renseignez-la dans la fiche de votre entreprise, dans votre logiciel.
3. Si votre logiciel n'a pas ce champ, signalez-le à son éditeur en citant BR-FR-13.

## Causes fréquentes

- **La fiche de l'entreprise n'a qu'un e-mail ou une adresse postale**, pas d'adresse de facturation électronique.
- **Le logiciel n'envoie pas ce champ** dans la facture électronique.

## Détails techniques

BT-34, adresse électronique du vendeur, avec son schéma BT-34-1 : `ram:URIUniversalCommunication/ram:URIID` (attribut `schemeID`) de la partie vendeur en CII, `cbc:EndpointID` en UBL.

## Texte officiel

> Le BT-34 est obligatoire.

BR-FR-13, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-13_BT-34`.

## Règles voisines

- [BR-FR-12](../BR-FR-12/) : l'adresse électronique de l'acheteur est obligatoire aussi.
- [BR-FR-22](../BR-FR-22/) : sur une autofacture B2B, elle commence par le SIREN du vendeur.
- [BR-FR-23](../BR-FR-23/) : les caractères admis dans une adresse électronique.
