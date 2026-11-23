# Le code d'exigibilité de la TVA n'est pas un code valide

Le code qui dit quand la TVA devient exigible n'est pas l'un des codes admis.

## Ce que vérifie la règle

Une facture peut dire, par un code, quelle date rend la TVA exigible : la date de facture, la date de livraison ou la date de paiement. Les codes diffèrent entre les deux syntaxes de factures électroniques, CII (celle de Factur-X et ZUGFeRD) et UBL (celle de Peppol). La règle vérifie que le code est l'un des trois de la syntaxe de la facture.

## Pourquoi c'est important

BR-CL-06 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-06 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez quelle date rend votre TVA exigible, et choisissez-la dans votre logiciel.
2. Vérifiez qu'une facture CII écrit 5, 29 ou 72, et une facture UBL 3, 35 ou 432.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-06.

## Causes fréquentes

- **Un code UBL dans une facture CII**, ou l'inverse, par un logiciel qui écrit les deux syntaxes.
- **Un code saisi à la main** dans un champ libre.

## Détails techniques

Le code de date d'exigibilité de la TVA est BT-8. En CII, c'est le `ram:DueDateTypeCode` de `ram:ApplicableTradeTax` dans `ram:ApplicableHeaderTradeSettlement`, de l'UNTDID 2475 : `5` la date de facture, `29` la date de livraison, `72` la date de paiement. En UBL, c'est le `cbc:DescriptionCode` de `cac:InvoicePeriod`, de l'UNTDID 2005 : `3` la date de facture, `35` la date de livraison effective, `432` la date de paiement. La règle BR-CO-03 interdit d'indiquer à la fois ce code et une date d'exigibilité (BT-7).

La facture d'exemple, en CII, indique le code `35`, le code UBL de la date de livraison. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000588`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Value added tax point date code MUST be coded using a restriction of UNTDID 2475.

BR-CL-06, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-03](../BR-CO-03/) : indiquez soit la date d'exigibilité de la TVA, soit son code, jamais les deux.
