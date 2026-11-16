# La période d'une ligne n'a ni date de début ni date de fin

Une ligne de la facture indique une période, mais sans date de début ni date de fin.

## Ce que vérifie la règle

Chaque ligne peut indiquer sa propre période, par exemple pour une ligne d'abonnement ou de location. Quand elle le fait, la règle vérifie que la période a au moins une date : celle de début, celle de fin, ou les deux.

## Pourquoi c'est important

BR-CO-20 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-20 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Si la ligne couvre une période, renseignez sa date de début, sa date de fin, ou les deux.
2. Si elle ne couvre pas de période, retirez la période de la ligne plutôt que de la laisser vide.
3. Si votre logiciel crée une période de ligne vide, signalez-le à son éditeur en citant BR-CO-20.

## Causes fréquentes

- **Une période de ligne créée vide par le logiciel**, quand aucune date n'est saisie.
- **Des dates écrites dans la désignation de la ligne** au lieu des champs de la période.

## Détails techniques

La période de ligne est le groupe BG-26, avec sa date de début BT-134 et sa date de fin BT-135. En CII : `ram:BillingSpecifiedPeriod` de `ram:SpecifiedLineTradeSettlement`, avec `ram:StartDateTime` et `ram:EndDateTime` ; en UBL : `cac:InvoicePeriod` de `cac:InvoiceLine` (ou `cac:CreditNoteLine`), avec `cbc:StartDate` et `cbc:EndDate`.

## Texte officiel

> If Invoice line period (BG-26) is used, the Invoice line period start date (BT-134) or the Invoice line period end date (BT-135) shall be filled, or both.

BR-CO-20, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-19](../BR-CO-19/) : la période de facturation doit avoir une date de début ou de fin.
- [BR-FR-03](../BR-FR-03/) : les dates de la période, comme les autres dates de la facture, doivent avoir une année entre 2000 et 2099.
