# Une remise au taux normal doit avoir un taux supérieur à zéro

Une remise au taux normal a un taux de TVA de 0 %.

## Ce que vérifie la règle

La catégorie S couvre la TVA facturée à un taux supérieur à zéro, taux réduits compris. Une opération à 0 % relève d'une autre catégorie : Z si elle est taxée au taux zéro, E si la loi l'exonère. AE, K et G servent à l'autoliquidation, aux livraisons intracommunautaires et aux exportations. La règle vérifie que le taux (BT-96) de chaque remise au niveau du document en S est supérieur à zéro.

## Pourquoi c'est important

BR-S-06 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-S-06 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Donnez à l'article son vrai taux de TVA, normal ou réduit.
2. Si aucune TVA ne s'applique, donnez-lui la catégorie qui dit pourquoi (Z, E, AE, K, G ou O), avec un motif s'il le faut.
3. Si votre logiciel écrit 0 % sous la catégorie S, signalez-le à l'éditeur de votre logiciel en citant BR-S-06.

## Causes fréquentes

- **Un article gratuit ou exonéré** laissé dans la catégorie S par défaut, avec un taux de 0 %.
- **La catégorie S utilisée pour toutes les lignes**, quel que soit le taux, par un modèle ou un export.

## Détails techniques

La catégorie de TVA d'une remise au niveau du document est BT-95, son taux BT-96. En CII : `ram:RateApplicablePercent` du `ram:CategoryTradeTax` de chaque `ram:SpecifiedTradeAllowanceCharge` dont le `ram:ChargeIndicator` vaut false ; en UBL : `cbc:Percent` du `cac:TaxCategory` de chaque `cac:AllowanceCharge` dont le `cbc:ChargeIndicator` vaut false.

La facture d'exemple donne à une remise la catégorie S et un taux de 0 %, et sa ventilation de TVA suit : une ventilation S à 0 %. Sa version corrigée applique le taux normal.

## Texte officiel

> In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Standard rated" the Document level allowance VAT rate (BT-96) shall be greater than zero.

BR-S-06, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-S-05](../BR-S-05/) : dans la catégorie de TVA S (taux normal), le taux de TVA d'une ligne est supérieur à zéro : un taux de 0 % relève d'une autre catégorie.
- [BR-S-07](../BR-S-07/) : dans la catégorie de TVA S (taux normal), le taux de TVA des frais au niveau du document est supérieur à zéro : un taux de 0 % relève d'une autre catégorie.
- [BR-Z-05](../BR-Z-05/) : dans la catégorie de TVA Z (taux zéro), le taux de TVA d'une ligne est de 0 %.
