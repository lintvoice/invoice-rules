# Une remise sur ligne n'a pas de montant

Une remise sur ligne n'indique pas de montant.

## Ce que vérifie la règle

Une remise sur ligne est une remise accordée sur une seule ligne de la facture. La règle vérifie que chacune indique son montant, hors TVA.

## Pourquoi c'est important

BR-41 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-41 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez que chaque remise sur ligne a son montant dans votre logiciel, un pourcentage étant converti en montant.
2. Vérifiez que la facture électronique écrit ce montant, et pas seulement le pourcentage.
3. Si le montant manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-41.

## Causes fréquentes

- **Un pourcentage écrit sans le montant qu'il donne.**
- **Un libellé gardé comme une ligne de texte**, sans montant.

## Détails techniques

Une remise sur ligne est le groupe BG-27, son montant BT-136. En CII, c'est le `ram:ActualAmount` de chaque `ram:SpecifiedTradeAllowanceCharge` du `ram:SpecifiedLineTradeSettlement` d'une ligne dont `ram:ChargeIndicator` vaut false ; en UBL, le `cbc:Amount` de chaque `cac:AllowanceCharge` d'une `cac:InvoiceLine` dont `cbc:ChargeIndicator` vaut false.

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige le montant d'une remise sur ligne, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) le laisse en revanche facultatif : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> Each Invoice line allowance (BG-27) shall have an Invoice line allowance amount (BT-136).

BR-41, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-42](../BR-42/) : chaque remise sur ligne doit indiquer son motif : en texte, en code, ou les deux.
- [BR-43](../BR-43/) : des frais sur ligne doivent toujours indiquer leur montant.
