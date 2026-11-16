# Un avoir ne cite pas la facture qu'il corrige

Un avoir ne dit pas quelle facture il corrige.

## Ce que vérifie la règle

Un avoir (types 261, 381, 396, 502 et 503) doit dire quelle facture il corrige :

- soit en tête, au moins une facture antérieure avec son numéro et sa date ;
- soit sur chaque ligne, la facture que la ligne corrige.

## Pourquoi c'est important

BR-FR-CO-05 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Sur l'avoir, indiquez le numéro et la date de la facture d'origine.
2. Si l'avoir porte sur plusieurs factures, citez-les toutes en tête, ou indiquez sur chaque ligne la facture qu'elle corrige.
3. Si votre logiciel crée des avoirs sans lien avec la facture, signalez-le à son éditeur en citant BR-FR-CO-05.

## Causes fréquentes

- **Un avoir créé de zéro**, sans lien avec la facture d'origine.
- **Un numéro cité sans sa date.**
- **Un avoir sur plusieurs factures** dont certaines lignes n'ont pas de référence.

## Détails techniques

Types BT-3 : 261, 381, 396, 502, 503. En tête : BT-25 avec BT-26 (BG-3). Sur les lignes : la référence de facture de la ligne (EXT-FR-FE-136, avec sa date EXT-FR-FE-138), exigée sur chaque ligne sans sous-type (EXT-FR-FE-163) ou de sous-type `DETAIL`.

## Texte officiel

> Si le type de facture (BT-3) est un avoir (261, 381, 396, 502, 503), alors : - soit au moins une référence à une facture antérieure (BT-25) avec sa date (BT-26) doit être présente au niveau entête, - soit chaque ligne (BG-25) sans subtype (EXT-FR-FE-163) ou avec subtype 'DETAIL' doit contenir une référence à une facture antérieure (EXT-FR-FE-136) avec sa date (EXT-FR-FE-138).

BR-FR-CO-05, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-CO-05_BT-3`.

## Règles voisines

- [BR-FR-CO-04](../BR-FR-CO-04/) : une facture rectificative cite exactement une facture antérieure.
- [BR-FR-01](../BR-FR-01/) : un numéro de facture cité compte au plus 35 caractères.
