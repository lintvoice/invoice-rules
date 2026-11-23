# La catégorie de TVA d'une remise ou de frais n'est pas un code valide

Une remise ou des frais globaux ont une catégorie de TVA qui n'est pas dans la liste officielle.

## Ce que vérifie la règle

La catégorie de TVA est un code d'une ou deux lettres d'une liste qu'EN 16931 garde courte : S pour un taux normal, Z pour un taux zéro, E pour une exonération, AE pour une autoliquidation, K pour une livraison intracommunautaire, G pour une exportation, O pour une opération hors du champ de la TVA, et L, M et B pour des cas locaux. EN 16931 n'a pas de code pour un taux réduit : sa catégorie S admet tout taux supérieur à zéro. La règle vérifie que la catégorie de chaque remise et de chaque frais global est l'un de ces codes.

## Pourquoi c'est important

BR-CL-17 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-17 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Donnez à chaque remise et à chaque frais la catégorie de TVA de ce à quoi ils s'appliquent, S pour un taux normal.
2. Vérifiez que la facture électronique écrit la catégorie, et non le type de taxe VAT ni le taux.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-17.

## Causes fréquentes

- **Le type de taxe au lieu de la catégorie**, VAT là où S est attendu.
- **Le taux écrit comme catégorie**, comme 20.

## Détails techniques

Le code de catégorie de TVA d'une remise au niveau du document est BT-95, de frais BT-102. En CII, c'est le `ram:CategoryCode` du `ram:CategoryTradeTax` de chaque `ram:SpecifiedTradeAllowanceCharge` ; en UBL, le `cbc:ID` du `cac:TaxCategory` de chaque `cac:AllowanceCharge`. La liste est la partie EN 16931 de l'UNCL 5305 : `AE`, `L`, `M`, `E`, `S`, `Z`, `G`, `O`, `K`, `B`.

La facture d'exemple donne à une remise la catégorie `VAT`, le type de taxe. La remise ne réduit alors aucune ventilation de TVA, donc la base du taux normal ne correspond plus à ses lignes moins ses remises, et BR-S-08 échoue aussi. Sur une facture française, la règle BR-FR-15, sur les catégories admises en France, échoue en plus. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000599`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Invoice tax categories MUST be coded using UNCL 5305 code list

BR-CL-17, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-32](../BR-32/) : chaque remise globale doit indiquer sa catégorie de TVA, pour que la ventilation de TVA en tienne compte.
- [BR-37](../BR-37/) : les frais globaux doivent indiquer leur catégorie de TVA, pour que la ventilation de TVA en tienne compte.
- [BR-CL-18](../BR-CL-18/) : la catégorie de TVA de chaque ligne et de chaque taux doit être l'un des codes qu'EN 16931 utilise, comme S.
- [BR-FR-15](../BR-FR-15/) : chaque montant soumis à TVA doit utiliser une des catégories S, E, AE, K, G, O ou Z ; les catégories L et M (îles Canaries, Ceuta et Melilla) ne s'appliquent pas en France.
