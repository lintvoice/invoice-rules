# Une remise sur une exportation doit avoir un taux de 0 %

Une remise sur une exportation a un taux de TVA autre que 0 %.

## Ce que vérifie la règle

La catégorie G couvre les biens expédiés à un acheteur hors de l'Union européenne, exonérés de TVA. La facture ne porte pas de TVA, donc le taux est de 0 %. La règle vérifie que le taux (BT-96) de chaque remise au niveau du document en G vaut 0.

## Pourquoi c'est important

BR-G-06 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-G-06 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Mettez le taux de TVA à 0 % sur les articles de catégorie G.
2. Si la TVA s'applique à un autre taux, la catégorie n'est pas G : donnez à l'article sa bonne catégorie.
3. Si votre logiciel garde le taux normal, signalez-le à l'éditeur de votre logiciel en citant BR-G-06.

## Causes fréquentes

- **La catégorie changée mais pas le taux** : le taux normal d'un article conservé quand il passe dans une autre catégorie.
- **Un taux repris de la fiche article du catalogue**, quelle que soit la catégorie de la facture.

## Détails techniques

La catégorie de TVA d'une remise au niveau du document est BT-95, son taux BT-96. En CII : `ram:RateApplicablePercent` du `ram:CategoryTradeTax` de chaque `ram:SpecifiedTradeAllowanceCharge` dont le `ram:ChargeIndicator` vaut false ; en UBL : `cbc:Percent` du `cac:TaxCategory` de chaque `cac:AllowanceCharge` dont le `cbc:ChargeIndicator` vaut false.

La facture d'exemple est entièrement en catégorie G, et sa remise garde le taux normal alors que sa catégorie est G ; la ventilation de TVA reste à 0 %. Sa version corrigée indique 0 %.

## Texte officiel

> In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Export outside the EU" the Document level allowance VAT rate (BT-96) shall be 0 (zero).

BR-G-06, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-G-05](../BR-G-05/) : dans la catégorie de TVA G (exportation hors de l'UE), le taux de TVA d'une ligne est de 0 %.
- [BR-G-07](../BR-G-07/) : dans la catégorie de TVA G (exportation hors de l'UE), le taux de TVA des frais au niveau du document est de 0 %.
- [BR-S-05](../BR-S-05/) : dans la catégorie de TVA S (taux normal), le taux de TVA d'une ligne est supérieur à zéro : un taux de 0 % relève d'une autre catégorie.
