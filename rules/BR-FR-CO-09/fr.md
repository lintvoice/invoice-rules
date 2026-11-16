# Une facture déjà payée ne le montre pas dans ses montants

La facture est déclarée déjà payée, mais ses montants ou sa date d'échéance ne le montrent pas.

## Ce que vérifie la règle

Le cadre de facturation B2, S2 ou M2 indique une facture déjà payée. Ses montants doivent le refléter :

- le montant déjà payé est égal au total TTC ;
- le net à payer vaut 0 ;
- la date d'échéance est renseignée, et c'est la date du paiement.

## Pourquoi c'est important

BR-FR-CO-09 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Si la facture est payée, indiquez le montant payé (égal au total TTC) et la date du paiement comme échéance.
2. Si elle n'est pas entièrement payée, n'utilisez pas le cadre B2, S2 ou M2.
3. Si le paiement est enregistré dans votre logiciel mais absent de la facture électronique, signalez-le à son éditeur en citant BR-FR-CO-09.

## Causes fréquentes

- **Un paiement enregistré dans le logiciel** mais pas reporté dans la facture électronique.
- **Le cadre B2, S2 ou M2 choisi pour une facture payée en partie.**
- **Pas de date d'échéance.**

## Détails techniques

Quand BT-23 vaut `B2`, `S2` ou `M2` : BT-113 (montant déjà payé) = BT-112 (total TTC), BT-115 (net à payer) = 0, et BT-9 (échéance) présente. Trois identifiants : `BR-FR-CO-09_BT-23-1`, `-2` et `-3`, un par contrôle.

## Texte officiel

> Si le cadre de facturation (BT-23) est B2, S2 ou M2 (facture déjà payée), alors le montant déjà payé (BT-113) doit être égal au montant total TTC (BT-112).

BR-FR-CO-09, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-CO-09_BT-23-1`, `BR-FR-CO-09_BT-23-2`, `BR-FR-CO-09_BT-23-3`.

## Règles voisines

- [BR-FR-08](../BR-FR-08/) : les codes de cadre de facturation.
- [BR-FR-CO-07](../BR-FR-CO-07/) : l'échéance peut précéder la date d'émission sur une facture déjà payée.
