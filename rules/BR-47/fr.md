# Un taux de TVA n'a pas de catégorie

Une ventilation de TVA n'indique pas de catégorie de TVA.

## Ce que vérifie la règle

La ventilation de TVA donne, pour chaque catégorie et chaque taux de TVA de la facture, sa base, son montant de TVA, sa catégorie et son taux. La règle vérifie que chacune indique sa catégorie, sous forme de code : S pour un taux normal, E pour une exonération, AE pour une autoliquidation…

## Pourquoi c'est important

BR-47 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-47 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Donnez à chaque taux de TVA de votre logiciel sa catégorie, par exemple E pour une exonération.
2. Vérifiez que la facture électronique écrit la ventilation de TVA en entier, un bloc par catégorie et par taux.
3. Si il manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-47.

## Causes fréquentes

- **Un taux paramétré sans catégorie** dans le logiciel.
- **Une ventilation de TVA construite à la main** dans un export, champ par champ.

## Détails techniques

Une ventilation de TVA est le groupe BG-23, ici son code de catégorie de TVA BT-118. En CII, c'est le `ram:CategoryCode` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, le `cac:TaxCategory/cbc:ID` de chaque `cac:TaxSubtotal`.

En CII, la règle ne lit qu'une ventilation dont le type de taxe, `ram:TypeCode`, vaut VAT : une ventilation d'un autre type n'a pas de catégorie de TVA pour elle.

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige le code de catégorie de chaque ventilation de TVA, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) le laisse en revanche facultatif : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> Each VAT breakdown (BG-23) shall be defined through a VAT category code (BT-118).

BR-47, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-18](../BR-CL-18/) : la catégorie de TVA de chaque ligne et de chaque taux doit être l'un des codes qu'EN 16931 utilise, comme S.
- [BR-CO-18](../BR-CO-18/) : toute facture doit détailler sa TVA par catégorie et par taux, même quand la TVA est nulle.
- [BR-48](../BR-48/) : chaque ventilation de TVA doit indiquer son taux, 0 % compris, sauf si la facture est hors du champ de la TVA.
