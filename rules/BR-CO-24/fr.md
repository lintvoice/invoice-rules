# Des frais sur ligne n'ont pas de motif

Des frais sur ligne de la facture n'indiquent ni motif ni code de motif.

## Ce que vérifie la règle

Les frais sur ligne doivent dire pourquoi ils existent : un motif en texte (« Emballage »), un code de motif, ou les deux. La règle vérifie qu'il y a au moins l'un des deux.

## Pourquoi c'est important

BR-CO-24 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-24 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans votre logiciel de facturation, renseignez le motif de des frais sur ligne, par exemple « Emballage ».
2. Si votre logiciel propose des codes de motif, choisissez celui qui correspond.
3. Si le motif est saisi mais absent de la facture électronique, signalez-le à l'éditeur du logiciel en citant BR-CO-24.

## Causes fréquentes

- **Des frais sur ligne saisis sans libellé.**
- **Un libellé imprimé sur le PDF** mais absent des données de la facture électronique.

## Détails techniques

Des frais sur ligne forment le groupe BG-28, avec un motif BT-144 et un code de motif BT-145. En CII, la règle lit `ram:Reason` et `ram:ReasonCode` de chaque `ram:SpecifiedTradeAllowanceCharge` de `ram:SpecifiedLineTradeSettlement` dont `ram:ChargeIndicator` vaut true ; en UBL, `cbc:AllowanceChargeReason` et `cbc:AllowanceChargeReasonCode` de chaque `cac:AllowanceCharge` de `cac:InvoiceLine` (ou `cac:CreditNoteLine`) dont `cbc:ChargeIndicator` vaut true.

La règle EN 16931 BR-44 exige la même chose : des frais sur ligne sans motif échouent donc aux deux règles, et la facture d'exemple aussi.

## Texte officiel

> Each Invoice line charge (BG-28) shall contain an Invoice line charge reason (BT-144) or an Invoice line charge reason code (BT-145), or both.

BR-CO-24, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-23](../BR-CO-23/) : chaque remise sur ligne doit avoir un motif, en texte ou en code.
- [BR-44](../BR-44/) : la règle de base qui exige le motif de frais sur ligne.
- [BR-CO-22](../BR-CO-22/) : chaque frais global doit avoir un motif, en texte ou en code.
