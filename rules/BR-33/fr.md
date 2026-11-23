# Une remise globale n'a pas de motif

Une remise globale de la facture n'indique ni motif ni code de motif.

## Ce que vérifie la règle

Chaque remise globale doit dire pourquoi elle existe : un motif en texte (« Remise commerciale »), un code de motif, ou les deux. La règle vérifie qu'il y a au moins l'un des deux.

## Pourquoi c'est important

BR-33 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-33 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans votre logiciel de facturation, renseignez le motif de chaque remise globale, par exemple « Remise commerciale ».
2. Si votre logiciel propose des codes de motif, choisissez celui qui correspond.
3. Si le motif est saisi mais absent de la facture électronique, signalez-le à l'éditeur du logiciel en citant BR-33.

## Causes fréquentes

- **Une remise globale saisie sans libellé.**
- **Un libellé imprimé sur le PDF** mais absent des données de la facture électronique.

## Détails techniques

Une remise au niveau du document forme le groupe BG-20, avec un motif BT-97 et un code de motif BT-98. En CII, la règle lit `ram:Reason` et `ram:ReasonCode` de chaque `ram:SpecifiedTradeAllowanceCharge` de `ram:ApplicableHeaderTradeSettlement` dont `ram:ChargeIndicator` vaut false ; en UBL, `cbc:AllowanceChargeReason` et `cbc:AllowanceChargeReasonCode` de chaque `cac:AllowanceCharge` du document dont `cbc:ChargeIndicator` vaut false.

La règle BR-CO-21 exige la même chose : une remise globale sans motif échoue donc aux deux règles, et la facture d'exemple aussi, qui est celle de BR-CO-21.

## Texte officiel

> Each Document level allowance (BG-20) shall have a Document level allowance reason (BT-97) or a Document level allowance reason code (BT-98).

BR-33, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-21](../BR-CO-21/) : chaque remise globale doit indiquer son motif : en texte, en code, ou les deux.
- [BR-31](../BR-31/) : chaque remise globale doit indiquer son montant.
- [BR-32](../BR-32/) : chaque remise globale doit indiquer sa catégorie de TVA, pour que la ventilation de TVA en tienne compte.
