# Une référence d'objet facturé de type AFL ou AVV est répétée ou vide

La facture donne deux références d'objet facturé du même type AFL ou AVV, ou l'une d'elles est vide.

## Ce que vérifie la règle

Une facture peut citer des « objets facturés » : des références à ce sur quoi elle porte, comme un numéro d'abonnement ou un point de comptage. Deux types de ces références, codés AFL et AVV, ne peuvent apparaître qu'une fois chacun, et ne doivent pas être vides.

## Pourquoi c'est important

BR-FR-29 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Repérez la référence répétée ou vide : le rapport de validation précise AFL ou AVV.
2. Gardez une seule référence de chaque type, avec sa valeur renseignée.
3. Si votre logiciel répète ou vide ces références, signalez-le à son éditeur en citant BR-FR-29.

## Causes fréquentes

- **La même référence envoyée deux fois.**
- **Un type de référence posé sans valeur.**

## Détails techniques

Identifiant d'objet facturé BT-18 avec son schéma BT-18-1 : en CII, `ram:AdditionalReferencedDocument` de code type `130` et de `ram:ReferenceTypeCode` `AFL` ou `AVV` ; la valeur est `ram:IssuerAssignedID`. Une référence AFL ou AVV vide échoue aussi à la règle EN 16931 BR-52.

## Texte officiel

> Parmi les identifiants d’objets facturés (BT-18), les schémas d’identification "AFL" et "AVV" ne doivent être présents qu’une seule fois chacun.

BR-FR-29, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-29_AFL`, `BR-FR-29_AVV`, `BR-FR-29_BT-18`.

## Règles voisines

- [BR-FR-30](../BR-FR-30/) : la même règle pour les références d'objet facturé d'une ligne.
