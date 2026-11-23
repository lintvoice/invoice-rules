# Des frais globaux n'ont pas de montant

Des frais globaux n'indiquent pas de montant.

## Ce que vérifie la règle

Des frais globaux sont un montant ajouté à l'ensemble de la facture, et non à une ligne, par exemple des frais de port. La règle vérifie qu'ils indiquent leur montant, hors TVA.

## Pourquoi c'est important

BR-36 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-36 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez que les frais globaux ont leur montant dans votre logiciel, un pourcentage étant converti en montant.
2. Vérifiez que la facture électronique écrit ce montant, et pas seulement le pourcentage.
3. Si le montant manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-36.

## Causes fréquentes

- **Un pourcentage écrit sans le montant qu'il donne.**
- **Un libellé gardé comme une ligne de texte**, sans montant.

## Détails techniques

Des frais au niveau du document forment le groupe BG-21, leur montant est BT-99. En CII, c'est le `ram:ActualAmount` de chaque `ram:SpecifiedTradeAllowanceCharge` de `ram:ApplicableHeaderTradeSettlement` dont `ram:ChargeIndicator` vaut true ; en UBL, le `cbc:Amount` de chaque `cac:AllowanceCharge` du document dont `cbc:ChargeIndicator` vaut true.

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige le montant des frais globaux, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) le laisse en revanche facultatif : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> Each Document level charge (BG-21) shall have a Document level charge amount (BT-99).

BR-36, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-37](../BR-37/) : les frais globaux doivent indiquer leur catégorie de TVA, pour que la ventilation de TVA en tienne compte.
- [BR-38](../BR-38/) : les frais globaux doivent indiquer leur motif : en texte, en code, ou les deux.
- [BR-CO-12](../BR-CO-12/) : le total des frais doit être exactement la somme des frais ajoutés à l'ensemble de la facture, au centime près.
