# La facture a plus d'une note BAR

La facture contient deux notes codées BAR ou plus.

## Ce que vérifie la règle

La note codée BAR indique comment la facture doit être traitée (B2B, B2C…). Une facture n'a qu'un seul traitement : la règle n'admet qu'une note BAR.

## Pourquoi c'est important

BR-FR-31 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Gardez la note BAR qui correspond à l'opération et supprimez les autres.
2. Si votre logiciel ajoute une note BAR en plus de la vôtre, signalez-le à son éditeur en citant BR-FR-31.

## Causes fréquentes

- **Une note BAR saisie à la main** en plus de celle que le logiciel ajoute.
- **Deux valeurs pour une opération mixte**, envoyées en deux notes.

## Détails techniques

Notes (BG-1) dont le code de sujet BT-21 vaut `BAR` : au plus une.

## Texte officiel

> Lorsque plusieurs notes ont le code sujet « BAR » (BT-21), Il ne peut y avoir qu'une seule valeur associée (BT-22, contenu de la note) parmi l’une des suivantes : B2B, B2BINT, B2C, OUTOFSCOPE, ARCHIVEONLY.

BR-FR-31, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-31_BT-21`.

## Règles voisines

- [BR-FR-20](../BR-FR-20/) : les valeurs admises dans la note BAR.
