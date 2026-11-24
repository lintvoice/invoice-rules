# La TVA d'un taux normal n'est pas sa base multipliée par le taux

Pour un des taux de TVA de la catégorie S de la facture, le montant de TVA n'est pas la base multipliée par le taux.

## Ce que vérifie la règle

La catégorie S couvre la TVA facturée à un taux supérieur à zéro, taux réduits compris. Dans la ventilation de TVA, chaque taux en S a sa base et son montant de TVA. La règle vérifie que le montant de TVA est la base multipliée par le taux, à moins de 1 près (une unité de la devise).

## Pourquoi c'est important

BR-S-09 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-S-09 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Pour chaque taux, multipliez la base par le taux et arrondissez au centime : c'est le montant de TVA attendu.
2. Calculez la TVA sur la base de chaque taux, et non ligne par ligne.
3. Si votre logiciel le calcule autrement, signalez-le à l'éditeur de votre logiciel en citant BR-S-09.

## Causes fréquentes

- **Une TVA arrondie ligne par ligne** puis additionnée, sur une facture de nombreuses lignes.
- **Un montant de TVA saisi à la main**, ou non recalculé après une modification.

## Détails techniques

La base d'une catégorie est BT-116, son montant de TVA BT-117, son taux BT-119. En CII : `ram:CalculatedAmount`, `ram:BasisAmount` et `ram:RateApplicablePercent` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` dont le `ram:CategoryCode` vaut `S` ; en UBL : `cbc:TaxAmount`, `cbc:TaxableAmount` et `cac:TaxCategory/cbc:Percent` de chaque `cac:TaxSubtotal` de catégorie `S`. BR-CO-17 fait le même contrôle pour toutes les catégories, avec une tolérance de 0,01 : un écart de 1 ou plus fait échouer les deux.

La facture d'exemple est celle de BR-CO-17 : son montant de TVA au taux normal dépasse de 1 la base multipliée par le taux, et les deux règles échouent.

## Texte officiel

> The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where VAT category code (BT-118) is "Standard rated" shall equal the VAT category taxable amount (BT-116) multiplied by the VAT category rate (BT-119).

BR-S-09, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-17](../BR-CO-17/) : pour chaque taux, le montant de TVA doit être la base HT multipliée par le taux, arrondie au centime.
- [BR-S-08](../BR-S-08/) : pour chaque taux, la base HT doit être la somme des lignes à ce taux, plus les frais et moins les remises au même taux.
- [BR-CO-14](../BR-CO-14/) : le total de TVA doit être exactement la somme des montants de TVA calculés pour chaque taux, au centime près.
