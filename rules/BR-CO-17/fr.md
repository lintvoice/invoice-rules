# La TVA d'un taux n'est pas sa base multipliée par le taux

Pour un taux de TVA de la facture, le montant de TVA n'est pas sa base HT multipliée par le taux.

## Ce que vérifie la règle

Dans la ventilation de TVA, chaque taux a sa base HT et son montant de TVA. La règle vérifie que ce montant correspond à la base multipliée par le taux, arrondie au centime, avec une petite tolérance (voir les détails techniques).

## Pourquoi c'est important

BR-CO-17 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-17 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Pour chaque taux, multipliez la base HT par le taux et arrondissez le résultat au centime.
2. Recalculez la TVA après toute modification de la base : remise ajoutée, ligne retirée.
3. Si votre logiciel calcule la TVA autrement, signalez-le à son éditeur en citant BR-CO-17.

## Causes fréquentes

- **Une base HT modifiée sans recalcul de la TVA**, après l'ajout d'une remise ou le retrait d'une ligne.
- **Un mauvais taux appliqué** au calcul, alors que la ventilation indique le bon.
- **La TVA d'un autre taux reportée** sur ce taux.

## Détails techniques

Le montant de TVA d'une catégorie est BT-117, sa base BT-116 et son taux BT-119. En CII : `ram:CalculatedAmount`, `ram:BasisAmount` et `ram:RateApplicablePercent` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` ; en UBL : `cbc:TaxAmount`, `cbc:TaxableAmount` et `cac:TaxCategory/cbc:Percent` de chaque `cac:TaxSubtotal`.

La règle accepte un écart allant jusqu'à 1 (une unité de la devise, soit 1 € pour une facture en euros), bornes comprises. Quand le taux est nul, elle exige un montant de TVA nul. Pour le taux normal, BR-S-09 fait le même contrôle avec un écart strictement inférieur à 1 : un écart d'exactement 1 € fait donc échouer BR-S-09 seule, et au-delà les deux règles échouent, comme dans la facture d'exemple (écart de 2 €).

## Texte officiel

> VAT category tax amount (BT-117) = VAT category taxable amount (BT-116) x (VAT category rate (BT-119) / 100), rounded to two decimals.

BR-CO-17, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-14](../BR-CO-14/) : le total de TVA doit être la somme de la TVA de chaque taux.
- [BR-S-09](../BR-S-09/) : le même contrôle que BR-CO-17, pour le taux normal.
