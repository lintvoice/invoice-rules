# La date et le code d'exigibilité de la TVA sont tous deux indiqués

La facture indique à la fois la date d'exigibilité de la TVA et un code qui la désigne, alors qu'un seul des deux est permis.

## Ce que vérifie la règle

La TVA devient exigible à une date précise. La facture peut l'indiquer de deux façons : par la date elle-même, ou par un code qui renvoie à une date déjà connue de la facture. La règle vérifie que la facture n'utilise qu'une seule de ces deux façons.

## Pourquoi c'est important

BR-CO-03 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-03 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans votre logiciel de facturation, choisissez une seule façon d'indiquer l'exigibilité de la TVA : une date, ou un code.
2. N'indiquez pas les deux sur une même facture, même s'ils désignent le même jour.
3. Si votre logiciel remplit les deux automatiquement, signalez-le à son éditeur en citant BR-CO-03.

## Causes fréquentes

- **Un code ajouté par défaut** par le logiciel, alors qu'une date est saisie en plus.
- **Une facture convertie depuis un autre format** qui portait les deux informations.

## Détails techniques

La date d'exigibilité de la TVA est BT-7, son code BT-8. En CII, la règle cherche `ram:TaxPointDate` et `ram:DueDateTypeCode` dans la facture (dans la ventilation de TVA, `ram:ApplicableTradeTax`) ; en UBL, `cbc:TaxPointDate` et `cac:InvoicePeriod/cbc:DescriptionCode`.

## Texte officiel

> Value added tax point date (BT-7) and Value added tax point date code (BT-8) are mutually exclusive.

BR-CO-03, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-FR-03](../BR-FR-03/) : les dates de la facture, dont la date d'exigibilité de la TVA, doivent avoir une année entre 2000 et 2099.
