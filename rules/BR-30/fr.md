# La période d'une ligne finit avant de commencer

La date de fin de la période d'une ligne précède sa date de début.

## Ce que vérifie la règle

Une ligne peut indiquer la période qu'elle couvre, un mois de service par exemple, avec une date de début et une date de fin. Quand les deux sont indiquées, la règle vérifie que la fin tombe le même jour que le début ou après.

## Pourquoi c'est important

BR-30 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-30 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez les deux dates de la période dans votre logiciel : elles sont peut-être inversées.
2. Pour un seul jour, indiquez la même date en début et en fin.
3. Si les dates sortent inversées, signalez-le à l'éditeur de votre logiciel en citant BR-30.

## Causes fréquentes

- **Des dates inversées**, la fin saisie dans le champ du début.
- **Une date lue dans le mauvais ordre**, jour et mois inversés lors d'un import.

## Détails techniques

La période de la ligne est le groupe BG-26, avec une date de début BT-134 et une date de fin BT-135. En CII, la règle compare `ram:StartDateTime` et `ram:EndDateTime` du `ram:BillingSpecifiedPeriod` du `ram:SpecifiedLineTradeSettlement` de la ligne, toutes deux au format 102 ; en UBL, `cbc:StartDate` et `cbc:EndDate` du `cac:InvoicePeriod` de la ligne.

La facture d'exemple donne à sa première ligne une période aux deux dates inversées, donc elle échoue à BR-30 seule.

## Texte officiel

> If both Invoice line period start date (BT-134) and Invoice line period end date (BT-135) are given then the Invoice line period end date (BT-135) shall be later or equal to the Invoice line period start date (BT-134).

BR-30, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-29](../BR-29/) : quand la période de facturation indique ses deux dates, la date de fin ne doit pas précéder la date de début.
- [BR-CO-20](../BR-CO-20/) : si une ligne de la facture indique une période, donnez au moins sa date de début ou sa date de fin.
