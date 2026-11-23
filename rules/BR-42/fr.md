# Une remise sur ligne n'a pas de motif

Une remise sur ligne de la facture n'indique ni motif ni code de motif.

## Ce que vérifie la règle

Chaque remise sur ligne doit dire pourquoi elle existe : un motif en texte (« Remise quantité »), un code de motif, ou les deux. La règle vérifie qu'il y a au moins l'un des deux.

## Pourquoi c'est important

BR-42 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-42 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans votre logiciel de facturation, renseignez le motif de chaque remise sur ligne, par exemple « Remise quantité ».
2. Si votre logiciel propose des codes de motif, choisissez celui qui correspond.
3. Si le motif est saisi mais absent de la facture électronique, signalez-le à l'éditeur du logiciel en citant BR-42.

## Causes fréquentes

- **Une remise sur ligne saisie sans libellé.**
- **Un libellé imprimé sur le PDF** mais absent des données de la facture électronique.

## Détails techniques

Une remise sur ligne forme le groupe BG-27, avec un motif BT-139 et un code de motif BT-140. En CII, la règle lit `ram:Reason` et `ram:ReasonCode` de chaque `ram:SpecifiedTradeAllowanceCharge` de `ram:SpecifiedLineTradeSettlement` dont `ram:ChargeIndicator` vaut false ; en UBL, `cbc:AllowanceChargeReason` et `cbc:AllowanceChargeReasonCode` de chaque `cac:AllowanceCharge` de `cac:InvoiceLine` (ou `cac:CreditNoteLine`) dont `cbc:ChargeIndicator` vaut false.

La règle BR-CO-23 exige la même chose : une remise sur ligne sans motif échoue donc aux deux règles, et la facture d'exemple aussi, qui est celle de BR-CO-23.

## Texte officiel

> Each Invoice line allowance (BG-27) shall have an Invoice line allowance reason (BT-139) or an Invoice line allowance reason code (BT-140).

BR-42, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-23](../BR-CO-23/) : chaque remise sur ligne doit indiquer son motif : en texte, en code, ou les deux.
- [BR-41](../BR-41/) : chaque remise sur ligne doit indiquer son montant.
