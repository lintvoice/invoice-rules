# La ventilation de TVA au taux normal indique un motif d'exonération

La ventilation de TVA de la catégorie S (taux normal) indique un motif d'exonération, en texte ou sous forme de code.

## Ce que vérifie la règle

La catégorie S couvre la TVA facturée à un taux supérieur à zéro, taux réduits compris. La TVA s'applique : ce n'est pas une exonération, donc sa ventilation n'indique ni motif d'exonération (BT-120) ni code de motif (BT-121). La règle vérifie que les deux sont absents.

## Pourquoi c'est important

BR-S-10 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-S-10 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Retirez le motif d'exonération des articles de catégorie S.
2. Si l'opération est en fait exonérée, donnez-lui la catégorie E et gardez le motif.
3. Si votre logiciel écrit un motif pour chaque catégorie, signalez-le à l'éditeur de votre logiciel en citant BR-S-10.

## Causes fréquentes

- **Un motif écrit pour chaque catégorie**, le nom du taux compris.
- **Une opération exonérée mise en catégorie S**, avec son motif conservé.

## Détails techniques

Le motif d'exonération est BT-120 (texte), son code BT-121, de la liste VATEX (BR-CL-22). En CII : `ram:ExemptionReason` ou `ram:ExemptionReasonCode` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` dont le `ram:CategoryCode` vaut `S` ; en UBL : `cbc:TaxExemptionReason` ou `cbc:TaxExemptionReasonCode` du `cac:TaxCategory` de chaque `cac:TaxSubtotal` de catégorie `S`.

La facture d'exemple, dans sa ventilation au taux normal, indique le nom de son taux comme motif d'exonération ; sa version corrigée n'en indique pas.

## Texte officiel

> A VAT Breakdown (BG-23) with VAT Category code (BT-118) "Standard rate" shall not have a VAT exemption reason code (BT-121) or VAT exemption reason text (BT-120).

BR-S-10, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-E-10](../BR-E-10/) : quand une partie de la facture est exonérée de TVA, la ventilation de TVA doit en donner le motif, en texte ou sous forme de code.
- [BR-Z-10](../BR-Z-10/) : un motif d'exonération est propre aux catégories sans TVA ; la ventilation de TVA de la catégorie Z (taux zéro) n'en indique pas.
- [BR-CL-22](../BR-CL-22/) : quand une facture indique le motif d'une exonération de TVA par un code, ce code doit venir de la liste VATEX.
