# La date d'échéance est avant la date de facture

La date d'échéance de la facture est antérieure à sa date d'émission.

## Ce que vérifie la règle

Quand la facture indique une date d'échéance, elle doit tomber le jour de la date d'émission ou après. Deux exceptions :

- les factures et avoirs d'acompte (types 386, 500 et 503) ;
- les factures déjà payées (cadre de facturation B2, S2 ou M2).

## Pourquoi c'est important

BR-FR-CO-07 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez la date d'émission et la date d'échéance de la facture.
2. Vérifiez les conditions de paiement (par exemple « 30 jours ») dont votre logiciel se sert pour calculer l'échéance.
3. Pour une facture déjà payée, utilisez le cadre de facturation B2, S2 ou M2 (voir BR-FR-CO-09).

## Causes fréquentes

- **Une faute de frappe** sur l'une des deux dates.
- **Une facture datée après coup**, alors que l'échéance a été calculée sur la date de commande.
- **Une facture déjà payée** sans le cadre B2, S2 ou M2.

## Détails techniques

Échéance BT-9 postérieure ou égale à la date d'émission BT-2. Exceptions : BT-3 parmi `386`, `500`, `503`, ou BT-23 parmi `B2`, `S2`, `M2`.

## Texte officiel

> La date d’échéance (BT-9), si présente, doit être postérieure ou égale à la date de facture (BT-2), sauf si la facture est de type acompte (386, 500, 503) ou si le cadre de facturation (BT-23) est B2, S2 ou M2.

BR-FR-CO-07, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-CO-07_BT-9`.

## Règles voisines

- [BR-FR-03](../BR-FR-03/) : chaque date a une année entre 2000 et 2099.
- [BR-FR-CO-09](../BR-FR-CO-09/) : une facture déjà payée le montre dans ses montants.
