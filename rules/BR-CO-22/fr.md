# Des frais globaux n'ont pas de motif

Des frais globaux de la facture n'indiquent ni motif ni code de motif.

## Ce que vérifie la règle

Les frais globaux doivent dire pourquoi ils existent : un motif en texte (« Frais de port »), un code de motif, ou les deux. La règle vérifie qu'il y a au moins l'un des deux.

## Pourquoi c'est important

BR-CO-22 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-22 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans votre logiciel de facturation, renseignez le motif de des frais globaux, par exemple « Frais de port ».
2. Si votre logiciel propose des codes de motif, choisissez celui qui correspond.
3. Si le motif est saisi mais absent de la facture électronique, signalez-le à l'éditeur du logiciel en citant BR-CO-22.

## Causes fréquentes

- **Des frais globaux saisis sans libellé.**
- **Un libellé imprimé sur le PDF** mais absent des données de la facture électronique.

## Détails techniques

Des frais au niveau du document forment le groupe BG-21, avec un motif BT-104 et un code de motif BT-105. En CII, la règle lit `ram:Reason` et `ram:ReasonCode` de chaque `ram:SpecifiedTradeAllowanceCharge` de `ram:ApplicableHeaderTradeSettlement` dont `ram:ChargeIndicator` vaut true ; en UBL, `cbc:AllowanceChargeReason` et `cbc:AllowanceChargeReasonCode` de chaque `cac:AllowanceCharge` du document dont `cbc:ChargeIndicator` vaut true.

La règle EN 16931 BR-38 exige la même chose : des frais globaux sans motif échouent donc aux deux règles, et la facture d'exemple aussi.

## Texte officiel

> Each Document level charge (BG-21) shall contain a Document level charge reason (BT-104) or a Document level charge reason code (BT-105), or both.

BR-CO-22, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-12](../BR-CO-12/) : le total des frais doit être la somme des frais globaux.
- [BR-38](../BR-38/) : la règle de base qui exige le motif de frais globaux.
- [BR-CO-21](../BR-CO-21/) : chaque remise globale doit avoir un motif, en texte ou en code.
