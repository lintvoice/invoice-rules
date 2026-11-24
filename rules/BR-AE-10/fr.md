# La mention d'autoliquidation manque

La facture utilise la catégorie de TVA AE (autoliquidation), mais sa ventilation ne dit pas pourquoi il n'y a pas de TVA.

## Ce que vérifie la règle

La catégorie AE couvre les opérations dont l'acheteur, et non le vendeur, déclare la TVA : le vendeur facture sans TVA. Sa ventilation dit pourquoi la facture ne porte pas de TVA. Ici, c'est la mention que la loi exige sur la facture, comme « Autoliquidation » (le code VATEX `VATEX-EU-AE`). La règle vérifie qu'elle indique un motif en texte (BT-120), un code de motif (BT-121), ou les deux.

## Pourquoi c'est important

BR-AE-10 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-AE-10 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez le motif de chaque article de cette catégorie, par exemple la mention que vous imprimez sur vos factures.
2. Si votre logiciel propose les codes de motif VATEX, choisissez celui qui correspond à votre cas.
3. Si le motif est saisi mais manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-AE-10.

## Causes fréquentes

- **Une mention imprimée sur le PDF** mais absente des données de la facture électronique.
- **Un article ou un client créé sans motif** dans le logiciel.

## Détails techniques

Le motif d'exonération est BT-120 (texte), son code BT-121, de la liste VATEX (BR-CL-22). En CII : `ram:ExemptionReason` ou `ram:ExemptionReasonCode` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` dont le `ram:CategoryCode` vaut `AE` ; en UBL : `cbc:TaxExemptionReason` ou `cbc:TaxExemptionReasonCode` du `cac:TaxCategory` de chaque `cac:TaxSubtotal` de catégorie `AE`.

La facture d'exemple est entièrement en catégorie AE, et sa ventilation n'indique ni motif ni code ; sa version corrigée indique les deux.

## Texte officiel

> A VAT Breakdown (BG-23) with VAT Category code (BT-118) "Reverse charge" shall have a VAT exemption reason code (BT-121), meaning "Reverse charge" or the VAT exemption reason text (BT-120) "Reverse charge" (or the equivalent standard text in another language).

BR-AE-10, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-E-10](../BR-E-10/) : quand une partie de la facture est exonérée de TVA, la ventilation de TVA doit en donner le motif, en texte ou sous forme de code.
- [BR-AE-01](../BR-AE-01/) : une facture qui a une ligne, une remise ou des frais de la catégorie de TVA AE (autoliquidation) doit avoir une ventilation de TVA pour cette catégorie, et une seule.
- [BR-CL-22](../BR-CL-22/) : quand une facture indique le motif d'une exonération de TVA par un code, ce code doit venir de la liste VATEX.
