# Une ligne au taux zéro doit avoir un taux de 0 %

Une ligne au taux zéro a un taux de TVA autre que 0 %.

## Ce que vérifie la règle

La catégorie Z couvre les opérations taxées au taux de 0 %, comme les panneaux solaires vendus à leur exploitant en Allemagne. La facture ne porte pas de TVA, donc le taux est de 0 %. La règle vérifie que le taux (BT-152) de chaque ligne en Z vaut 0.

## Pourquoi c'est important

BR-Z-05 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-Z-05 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Mettez le taux de TVA à 0 % sur les articles de catégorie Z.
2. Si la TVA s'applique à un autre taux, la catégorie n'est pas Z : donnez à l'article sa bonne catégorie.
3. Si votre logiciel garde le taux normal, signalez-le à l'éditeur de votre logiciel en citant BR-Z-05.

## Causes fréquentes

- **La catégorie changée mais pas le taux** : le taux normal d'un article conservé quand il passe dans une autre catégorie.
- **Un taux repris de la fiche article du catalogue**, quelle que soit la catégorie de la facture.

## Détails techniques

La catégorie de TVA d'une ligne est BT-151, son taux BT-152. En CII : `ram:RateApplicablePercent` du `ram:ApplicableTradeTax` ; en UBL : `cbc:Percent` de `cac:Item/cac:ClassifiedTaxCategory`.

La facture d'exemple est entièrement en catégorie Z, et sa première ligne garde le taux normal alors que sa catégorie est Z ; la ventilation de TVA reste à 0 %. Sa version corrigée indique 0 %.

La facture d'exemple est allemande : la France n'a pas de taux zéro pour ses opérations intérieures.

## Texte officiel

> In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Zero rated" the Invoiced item VAT rate (BT-152) shall be 0 (zero).

BR-Z-05, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-Z-06](../BR-Z-06/) : dans la catégorie de TVA Z (taux zéro), le taux de TVA d'une remise au niveau du document est de 0 %.
- [BR-Z-07](../BR-Z-07/) : dans la catégorie de TVA Z (taux zéro), le taux de TVA des frais au niveau du document est de 0 %.
- [BR-S-05](../BR-S-05/) : dans la catégorie de TVA S (taux normal), le taux de TVA d'une ligne est supérieur à zéro : un taux de 0 % relève d'une autre catégorie.
