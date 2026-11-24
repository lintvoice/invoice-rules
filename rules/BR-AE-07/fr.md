# Des frais en autoliquidation doivent avoir un taux de 0 %

Des frais en autoliquidation ont un taux de TVA autre que 0 %.

## Ce que vérifie la règle

La catégorie AE couvre les opérations dont l'acheteur, et non le vendeur, déclare la TVA : le vendeur facture sans TVA. La facture ne porte pas de TVA, donc le taux est de 0 %. La règle vérifie que le taux (BT-103) de chacun des frais au niveau du document en AE vaut 0.

## Pourquoi c'est important

BR-AE-07 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-AE-07 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Mettez le taux de TVA à 0 % sur les articles de catégorie AE.
2. Si la TVA s'applique à un autre taux, la catégorie n'est pas AE : donnez à l'article sa bonne catégorie.
3. Si votre logiciel garde le taux normal, signalez-le à l'éditeur de votre logiciel en citant BR-AE-07.

## Causes fréquentes

- **La catégorie changée mais pas le taux** : le taux normal d'un article conservé quand il passe dans une autre catégorie.
- **Un taux repris de la fiche article du catalogue**, quelle que soit la catégorie de la facture.

## Détails techniques

La catégorie de TVA des frais au niveau du document est BT-102, son taux BT-103. En CII : `ram:RateApplicablePercent` du `ram:CategoryTradeTax` de chaque `ram:SpecifiedTradeAllowanceCharge` dont le `ram:ChargeIndicator` vaut true ; en UBL : `cbc:Percent` du `cac:TaxCategory` de chaque `cac:AllowanceCharge` dont le `cbc:ChargeIndicator` vaut true.

La facture d'exemple est entièrement en catégorie AE, et ses frais gardent le taux normal alors que sa catégorie est AE ; la ventilation de TVA reste à 0 %. Sa version corrigée indique 0 %.

## Texte officiel

> In a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Reverse charge" the Document level charge VAT rate (BT-103) shall be 0 (zero).

BR-AE-07, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-AE-05](../BR-AE-05/) : dans la catégorie de TVA AE (autoliquidation), le taux de TVA d'une ligne est de 0 %.
- [BR-AE-06](../BR-AE-06/) : dans la catégorie de TVA AE (autoliquidation), le taux de TVA d'une remise au niveau du document est de 0 %.
- [BR-S-05](../BR-S-05/) : dans la catégorie de TVA S (taux normal), le taux de TVA d'une ligne est supérieur à zéro : un taux de 0 % relève d'une autre catégorie.
