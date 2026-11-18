# La quantité d'une ligne n'a pas d'unité

La quantité facturée d'une ligne n'indique pas son unité de mesure.

## Ce que vérifie la règle

Chaque quantité facturée doit être accompagnée de son unité de mesure : unité, heure, jour, kilogramme… La facture électronique ne l'écrit pas en toutes lettres mais sous forme de code normalisé, que votre logiciel choisit d'après l'unité que vous sélectionnez.

## Pourquoi c'est important

BR-23 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-23 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez une unité pour chaque article ou prestation dans votre logiciel, par exemple « unité », « heure » ou « jour ».
2. Pour une prestation au forfait, choisissez l'unité « unité ».
3. Si l'unité est choisie mais absente de la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-23.

## Causes fréquentes

- **Une ligne au forfait** sans unité.
- **Une unité saisie en texte libre** (« forfait », « lot ») que le logiciel ne traduit pas en code.
- **Un article créé sans unité** dans le catalogue du logiciel.

## Détails techniques

L'unité est BT-130, un attribut de la quantité BT-129 : `unitCode` de `ram:BilledQuantity` en CII, de `cbc:InvoicedQuantity` (ou `cbc:CreditedQuantity`) en UBL. Le code vient des recommandations 20 et 21 de la CEE-ONU, comme l'exige la règle BR-CL-23 : par exemple `C62` (unité), `HUR` (heure), `DAY` (jour), `KGM` (kilogramme).

Le schéma XML de Factur-X laisse cet attribut facultatif : c'est BR-23 qui le rend obligatoire. La facture d'exemple retire l'unité de la quantité de sa première ligne.

## Texte officiel

> An Invoice line (BG-25) shall have an Invoiced quantity unit of measure code (BT-130).

BR-23, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-22](../BR-22/) : chaque ligne doit indiquer une quantité.
