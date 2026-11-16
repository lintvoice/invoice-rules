# Une facture en devise étrangère n'indique pas la TVA en euros

La facture est dans une autre devise que l'euro, mais n'indique pas la TVA en euros.

## Ce que vérifie la règle

Une facture peut être établie dans une autre devise que l'euro. Dans ce cas, la règle exige :

- la devise de comptabilisation de la TVA, égale à EUR ;
- le total de TVA exprimé en euros.

## Pourquoi c'est important

BR-FR-CO-12 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Pour une facture en devise, indiquez EUR comme devise de comptabilisation de la TVA dans votre logiciel.
2. Faites convertir le total de TVA en euros et envoyer avec la facture.
3. Si votre logiciel ne sait pas le faire, signalez-le à son éditeur en citant BR-FR-CO-12.

## Causes fréquentes

- **Une facture en dollars ou en livres** sans conversion de la TVA.
- **La devise de comptabilisation de la TVA indiquée**, mais pas le montant en euros.

## Détails techniques

Si BT-5 (devise de facture) n'est pas `EUR` : BT-6 (devise de comptabilisation de la TVA) = `EUR`, et BT-111 (total de TVA en devise de comptabilisation) présent avec `currencyID="EUR"`. En CII, BT-111 est le second `ram:TaxTotalAmount`, dans la devise de comptabilisation.

## Texte officiel

> Si la devise de facture (BT-5) est différente de EUR, alors : - la devise de comptabilité (BT-6) doit être présente et égale à EUR, - le montant de TVA en devise de comptabilité (BT-111) doit être renseigné, - et sa devise (BT-111-1) doit être égale à EUR.

BR-FR-CO-12, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-CO-12_BT-5`.

## Règles voisines

Pas de règle voisine directe.
