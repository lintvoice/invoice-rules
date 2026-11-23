# Une remise globale n'a pas de montant

Une remise globale n'indique pas de montant.

## Ce que vérifie la règle

Une remise globale est une remise accordée sur l'ensemble de la facture, et non sur une ligne, par exemple une remise commerciale. La règle vérifie que chacune indique son montant, hors TVA.

## Pourquoi c'est important

BR-31 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-31 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez que chaque remise globale a son montant dans votre logiciel, un pourcentage étant converti en montant.
2. Vérifiez que la facture électronique écrit ce montant, et pas seulement le pourcentage.
3. Si le montant manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-31.

## Causes fréquentes

- **Un pourcentage écrit sans le montant qu'il donne.**
- **Un libellé gardé comme une ligne de texte**, sans montant.

## Détails techniques

Une remise au niveau du document est le groupe BG-20, son montant BT-92. En CII, c'est le `ram:ActualAmount` de chaque `ram:SpecifiedTradeAllowanceCharge` de `ram:ApplicableHeaderTradeSettlement` dont `ram:ChargeIndicator` vaut false ; en UBL, le `cbc:Amount` de chaque `cac:AllowanceCharge` du document dont `cbc:ChargeIndicator` vaut false.

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige le montant d'une remise globale, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) le laisse en revanche facultatif : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> Each Document level allowance (BG-20) shall have a Document level allowance amount (BT-92).

BR-31, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-32](../BR-32/) : chaque remise globale doit indiquer sa catégorie de TVA, pour que la ventilation de TVA en tienne compte.
- [BR-33](../BR-33/) : chaque remise globale doit indiquer son motif : en texte, en code, ou les deux.
- [BR-CO-11](../BR-CO-11/) : le total des remises doit être exactement la somme des remises accordées sur l'ensemble de la facture, au centime près.
