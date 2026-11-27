# Le montant de TVA des exportations doit être nul

La ventilation de TVA de la catégorie G (exportation hors de l'UE) a un montant de TVA autre que 0.

## Ce que vérifie la règle

La catégorie G couvre les biens expédiés à un acheteur hors de l'Union européenne, exonérés de TVA. Aucune TVA n'est facturée dans cette catégorie, donc le montant de TVA de sa ventilation vaut 0. La règle le vérifie.

## Pourquoi c'est important

BR-G-09 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-G-09 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Si aucune TVA n'est due, mettez à 0 le montant de TVA de la catégorie G, et corrigez le total de TVA.
2. Si de la TVA est due, la catégorie n'est pas G : donnez aux articles leur bonne catégorie et leur bon taux.
3. Si votre logiciel calcule de la TVA sur cette catégorie, signalez-le à l'éditeur de votre logiciel en citant BR-G-09.

## Causes fréquentes

- **Une TVA calculée au taux normal** sur des articles dont la catégorie a été changée ensuite.
- **Une catégorie G choisie par erreur** pour une opération qui porte bien de la TVA.

## Détails techniques

Le montant de TVA d'une catégorie est BT-117. En CII : `ram:CalculatedAmount` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` dont le `ram:CategoryCode` vaut `G` ; en UBL : `cbc:TaxAmount` de chaque `cac:TaxSubtotal` de catégorie `G`. La règle veut exactement 0.

La facture d'exemple est entièrement en catégorie G, et sa ventilation indique un montant de TVA au taux normal de sa base, avec un taux de 0 % ; son total de TVA suit. BR-CO-17, qui compare le montant de TVA à la base multipliée par le taux, échoue aussi.

## Texte officiel

> The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Export outside the EU" shall be 0 (zero).

BR-G-09, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-G-08](../BR-G-08/) : dans la ventilation de TVA, la base de la catégorie G (exportation hors de l'UE) est la somme de ses lignes, plus ses frais, moins ses remises.
- [BR-G-05](../BR-G-05/) : dans la catégorie de TVA G (exportation hors de l'UE), le taux de TVA d'une ligne est de 0 %.
- [BR-CO-17](../BR-CO-17/) : pour chaque taux, le montant de TVA doit être la base HT multipliée par le taux, arrondie au centime.
