# La base HT d'un taux n'est pas la somme de ses lignes

Pour un taux de TVA de la facture, la base HT ne correspond pas aux lignes, remises et frais à ce taux.

## Ce que vérifie la règle

Dans la ventilation de TVA, chaque taux a sa base HT. La règle vérifie que cette base est la somme des montants HT des lignes à ce taux, plus les frais et moins les remises sur l'ensemble de la facture qui ont le même taux.

## Pourquoi c'est important

BR-S-08 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-S-08 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Pour chaque taux, additionnez les montants HT des lignes à ce taux, ajoutez les frais et retirez les remises au même taux : c'est la base HT attendue.
2. Rattachez chaque remise et chaque frais sur l'ensemble de la facture au bon taux de TVA : un mauvais taux fausse la base de deux taux.
3. Recalculez les bases après toute modification de la facture : ligne ajoutée ou retirée, remise ajoutée.
4. Si votre logiciel calcule la base autrement, signalez-le à son éditeur en citant BR-S-08.

## Causes fréquentes

- **Une remise sur l'ensemble de la facture** déduite du total mais pas de la base de son taux.
- **Une remise rattachée à un autre taux** que celui des lignes qu'elle concerne.
- **Une base recalculée à partir du TTC**, qui ne retombe pas exactement sur la somme des lignes.

## Détails techniques

La base HT d'une catégorie est BT-116, pour la catégorie S (tout taux supérieur à zéro) et son taux BT-119. Elle doit valoir la somme des montants nets des lignes (BT-131) de catégorie S à ce taux, plus les frais (BT-99) et moins les remises (BT-92) au niveau du document de même catégorie et de même taux. En CII : `ram:BasisAmount` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` dont `ram:CategoryCode` vaut `S` ; en UBL : `cbc:TaxableAmount` de chaque `cac:TaxSubtotal` de catégorie `S`.

En CII, la règle exige une égalité exacte, chaque somme étant arrondie au centime. En UBL, elle accepte un écart strictement inférieur à 1 (une unité de la devise).

La facture d'exemple déclare une base de 1 026,00 € pour 1 025,00 € de lignes à 20 %. Son montant de TVA, 205,00 €, s'écarte de 0,20 € de la base multipliée par le taux : c'est dans la tolérance de BR-CO-17 et de BR-S-09, qui n'échouent donc pas.

## Texte officiel

> For each different value of VAT category rate (BT-119) where the VAT category code (BT-118) is "Standard rated", the VAT category taxable amount (BT-116) in a VAT breakdown (BG-23) shall equal the sum of Invoice line net amounts (BT-131) plus the sum of document level charge amounts (BT-99) minus the sum of document level allowance amounts (BT-92) where the VAT category code (BT-151, BT-102, BT-95) is "Standard rated" and the VAT rate (BT-152, BT-103, BT-96) equals the VAT category rate (BT-119).

BR-S-08, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-17](../BR-CO-17/) : la TVA d'un taux doit être sa base multipliée par le taux.
- [BR-S-09](../BR-S-09/) : le même contrôle que BR-CO-17, pour la catégorie S.
- [BR-CO-13](../BR-CO-13/) : le total HT doit être la somme des lignes, moins les remises, plus les frais.
