# Une facture définitive après acompte porte un type d'acompte

Un document au cadre B4, S4 ou M4 porte un type d'acompte (386, 500 ou 503).

## Ce que vérifie la règle

Le cadre B4, S4 ou M4 indique une facture définitive, émise après un ou plusieurs acomptes. Elle ne peut donc pas être elle-même un document d'acompte : les types 386, 500 et 503 sont refusés avec ce cadre.

## Pourquoi c'est important

BR-FR-CO-08 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Si le document est une facture d'acompte, ne lui donnez pas le cadre B4, S4 ou M4.
2. Si c'est la facture finale, donnez-lui un type de facture ordinaire, comme 380.
3. Si votre logiciel fixe ces valeurs de lui-même, signalez-le à son éditeur en citant BR-FR-CO-08.

## Causes fréquentes

- **Le cadre de la facture finale appliqué par erreur** à une facture d'acompte.
- **Le type de la facture d'acompte recopié** sur la facture finale.

## Détails techniques

Combinaison refusée : BT-23 parmi `B4`, `S4`, `M4` avec BT-3 parmi `386`, `500`, `503`.

## Texte officiel

> Si le cadre de facturation (BT-23) est B4, S4 ou M4 (factures définitives après acompte), alors le type de facture (BT-3) ne peut pas être une facture ou un avoir d’acompte (386, 500, 503).

BR-FR-CO-08, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-CO-08_BT-23`.

## Règles voisines

- [BR-FR-08](../BR-FR-08/) : les codes de cadre de facturation.
- [BR-FR-CO-07](../BR-FR-CO-07/) : la date d'échéance d'une facture d'acompte.
