# Une ligne n'a pas de catégorie de TVA

Une ligne de la facture n'indique pas sa catégorie de TVA.

## Ce que vérifie la règle

Chaque ligne doit indiquer sa catégorie de TVA : taux normal, taux zéro, exonération, autoliquidation… C'est ce qui permet de ventiler la TVA par catégorie et de vérifier les totaux. La règle vérifie que chaque ligne porte une catégorie de TVA.

## Pourquoi c'est important

BR-CO-04 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-04 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans votre logiciel, vérifiez que chaque article ou prestation a une catégorie de TVA, le plus souvent le taux normal.
2. Vérifiez aussi que la taxe de la ligne est déclarée comme de la TVA, et non comme une autre taxe.
3. Si votre logiciel n'envoie pas la catégorie de TVA des lignes, signalez-le à son éditeur en citant BR-CO-04.

## Causes fréquentes

- **Un article créé sans catégorie de TVA** dans le logiciel.
- **Une taxe de ligne déclarée sous un autre type que la TVA**, si bien que sa catégorie n'est pas lue comme une catégorie de TVA.

## Détails techniques

La catégorie de TVA d'une ligne est BT-151. En CII, la règle cherche `ram:CategoryCode` dans le `ram:ApplicableTradeTax` de `ram:SpecifiedLineTradeSettlement` dont `ram:TypeCode` vaut `VAT` ; en UBL, `cbc:ID` de `cac:Item/cac:ClassifiedTaxCategory` dont le schéma fiscal est `VAT`.

Une ligne sans aucune catégorie ne passe pas le schéma XML de Factur-X. La facture d'exemple déclare donc la taxe de la ligne avec le type `GST` au lieu de `VAT`, ce qui fait aussi échouer la règle de syntaxe CII-DT-037 et une règle du profil Factur-X.

## Texte officiel

> Each Invoice line (BG-25) shall be categorized with an Invoiced item VAT category code (BT-151).

BR-CO-04, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-18](../BR-CO-18/) : la facture doit avoir au moins une ventilation de TVA.
- [BR-CO-17](../BR-CO-17/) : la TVA de chaque taux doit être sa base multipliée par le taux.
