# La période de facturation finit avant de commencer

La date de fin de la période de facturation précède sa date de début.

## Ce que vérifie la règle

Une facture peut indiquer la période qu'elle couvre, un mois de service par exemple, avec une date de début et une date de fin. Quand les deux sont indiquées, la règle vérifie que la fin tombe le même jour que le début ou après.

## Pourquoi c'est important

BR-29 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-29 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez les deux dates de la période dans votre logiciel : elles sont peut-être inversées.
2. Pour un seul jour, indiquez la même date en début et en fin.
3. Si les dates sortent inversées, signalez-le à l'éditeur de votre logiciel en citant BR-29.

## Causes fréquentes

- **Des dates inversées**, la fin saisie dans le champ du début.
- **Une date lue dans le mauvais ordre**, jour et mois inversés lors d'un import.

## Détails techniques

La période de facturation est le groupe BG-14, avec une date de début BT-73 et une date de fin BT-74. En CII, la règle compare `ram:StartDateTime` et `ram:EndDateTime` de `ram:BillingSpecifiedPeriod`, dans `ram:ApplicableHeaderTradeSettlement`, toutes deux au format 102 ; en UBL, `cbc:StartDate` et `cbc:EndDate` de `cac:InvoicePeriod`.

La facture d'exemple indique une période de facturation aux deux dates inversées, donc elle échoue à BR-29 seule.

## Texte officiel

> If both Invoicing period start date (BT-73) and Invoicing period end date (BT-74) are given then the Invoicing period end date (BT-74) shall be later or equal to the Invoicing period start date (BT-73).

BR-29, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-30](../BR-30/) : quand la période d'une ligne indique ses deux dates, la date de fin ne doit pas précéder la date de début.
- [BR-CO-19](../BR-CO-19/) : si la facture indique une période de facturation, donnez au moins sa date de début ou sa date de fin.
