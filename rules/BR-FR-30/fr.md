# Une référence d'objet facturé de type AFL ou AVV est répétée ou vide sur une ligne

Une ligne de la facture donne deux fois une référence d'objet facturé du même type, AFL ou AVV, ou une référence vide.

## Ce que vérifie la règle

Une ligne peut citer des « objets facturés » : des références à ce sur quoi elle porte, comme un numéro d'abonnement ou un point de comptage. Sur chaque ligne, les deux types de références codés AFL et AVV ne peuvent apparaître qu'une fois chacun, et ne doivent pas être vides. BR-FR-29 vérifie la même chose pour les références de toute la facture.

## Pourquoi c'est important

BR-FR-30 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Sur chaque ligne, gardez une seule référence de type AFL et une seule de type AVV.
2. Supprimez les références vides, ou renseignez-les.
3. Si votre logiciel répète ces références de lui-même, signalez-le à son éditeur en citant BR-FR-30.

## Causes fréquentes

- **Deux numéros d'abonnement ou de point de comptage sur une même ligne**, au lieu d'une ligne par objet facturé.
- **Une référence créée sans valeur.**

## Détails techniques

Identifiant d'objet facturé de ligne BT-128 avec son schéma BT-128-1. En UBL, la règle lit `cbc:ID` de chaque `cac:DocumentReference` d'une `cac:InvoiceLine` (ou `cac:CreditNoteLine`), selon son `schemeID`, `AFL` ou `AVV`.

En CII, la règle cherche un `ram:AdditionalReferencedDocument` directement sous `ram:IncludedSupplyChainTradeLineItem`, où aucun schéma CII ne le place (Factur-X 1.09.2 EN 16931 et EXTENDED, CII D22B), car BT-128 se trouve sous `ram:SpecifiedLineTradeSettlement`. Dans les fichiers 1.4.0.04, la règle ne se déclenche donc jamais sur une facture Factur-X ou CII.

Dans le fichier UBL, l'identifiant `BR-FR-30_BT-21` porte un autre contrôle, celui de BR-FR-31 (une seule mention de cadre de facturation).

## Texte officiel

> Parmi les identifiants d’objets facturés à la ligne (BT-128), les schémas d’identification "AFL" et "AVV" ne doivent être présents qu’une seule fois chacun.

BR-FR-30, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-30_AFL`, `BR-FR-30_AVV`, `BR-FR-30_BT-128`.

## Règles voisines

- [BR-FR-29](../BR-FR-29/) : la même règle pour les références d'objet facturé de toute la facture.
