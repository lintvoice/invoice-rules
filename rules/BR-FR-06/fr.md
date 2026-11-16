# Une mention codée apparaît plus d'une fois

La facture contient deux notes avec le même code : PMT, PMD, AAB ou TXD.

## Ce que vérifie la règle

Quatre mentions codées ne peuvent apparaître qu'une fois chacune dans les notes de la facture :

- **PMT** : l'indemnité forfaitaire pour frais de recouvrement ;
- **PMD** : les pénalités de retard ;
- **AAB** : l'escompte ou son absence ;
- **TXD** : une mention relative à la taxe.

Si l'information tient en plusieurs phrases, elles vont dans la même note.

## Pourquoi c'est important

BR-FR-06 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Repérez la mention en double : le rapport de validation cite son code.
2. Fusionnez les deux notes en une seule, ou supprimez celle qui est en trop.
3. Si votre logiciel ajoute automatiquement une mention que vous avez aussi saisie, signalez-le à son éditeur en citant BR-FR-06.

## Causes fréquentes

- **Une mention saisie à la main en plus de celle que le logiciel ajoute.**
- **Une mention longue découpée en plusieurs notes** portant le même code.
- **Un modèle de facture qui répète les conditions de paiement.**

## Détails techniques

Notes BG-1, code du sujet BT-21. En CII, au plus un `ram:IncludedNote` par `ram:SubjectCode` parmi `PMT`, `PMD`, `AAB` et `TXD`. En UBL, au plus une occurrence de `#PMT#`, `#PMD#`, `#AAB#` et `#TXD#` dans l'ensemble des notes.

## Texte officiel

> Le code sujet PMT (indemnité forfaitaire pour frais de recouvrement) ne doit apparaître qu'une seule fois dans les notes (BG-1).

BR-FR-06, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-06_BT-21-1`, `BR-FR-06_BT-21-2`, `BR-FR-06_BT-21-3`, `BR-FR-06_BT-21-4`, `BR-FR-06_BT-21_AAB`, `BR-FR-06_BT-21_PMD`, `BR-FR-06_BT-21_PMT`, `BR-FR-06_BT-21_TXD`.

## Règles voisines

- [BR-FR-05](../BR-FR-05/) : les mentions PMT, PMD et AAB sont obligatoires.
