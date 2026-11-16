# La période de facturation n'a ni date de début ni date de fin

La facture indique une période de facturation, mais sans date de début ni date de fin.

## Ce que vérifie la règle

Une facture peut indiquer la période qu'elle couvre, par exemple un abonnement du 1er au 31 octobre. Quand elle le fait, la règle vérifie que la période a au moins une date : celle de début, celle de fin, ou les deux.

## Pourquoi c'est important

BR-CO-19 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-19 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Si la facture couvre une période, renseignez sa date de début, sa date de fin, ou les deux.
2. Si elle ne couvre pas de période, retirez la période de facturation plutôt que de la laisser vide.
3. Si votre logiciel crée une période vide, signalez-le à son éditeur en citant BR-CO-19.

## Causes fréquentes

- **Une période créée vide par le logiciel**, quand aucune date n'est saisie.
- **Des dates écrites ailleurs**, dans un texte libre par exemple, au lieu des champs de la période.

## Détails techniques

La période de facturation est le groupe BG-14, avec sa date de début BT-73 et sa date de fin BT-74. En CII : `ram:BillingSpecifiedPeriod` de `ram:ApplicableHeaderTradeSettlement`, avec `ram:StartDateTime` et `ram:EndDateTime` ; en UBL : `cac:InvoicePeriod`, avec `cbc:StartDate` et `cbc:EndDate`. En UBL, une période qui ne porte que le code de date d'exigibilité de la TVA (BT-8, `cbc:DescriptionCode`) passe aussi.

## Texte officiel

> If Invoicing period (BG-14) is used, the Invoicing period start date (BT-73) or the Invoicing period end date (BT-74) shall be filled, or both.

BR-CO-19, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-20](../BR-CO-20/) : la période d'une ligne doit avoir une date de début ou de fin.
- [BR-FR-03](../BR-FR-03/) : les dates de la période, comme les autres dates de la facture, doivent avoir une année entre 2000 et 2099.
