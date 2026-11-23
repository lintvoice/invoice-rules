# Une ligne n'a pas de numéro

Une ligne de la facture a un identifiant vide.

## Ce que vérifie la règle

Chaque ligne d'une facture électronique a un identifiant, en général son numéro : 1, 2, 3… Le logiciel de l'acheteur s'en sert pour désigner une ligne, dans une contestation ou un avoir par exemple. La règle vérifie que chaque ligne en a un.

## Pourquoi c'est important

BR-21 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-21 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez que votre logiciel numérote les lignes de chaque facture.
2. Vérifiez que la facture électronique écrit le numéro de chaque ligne, y compris les lignes ajoutées à la main.
3. Si une ligne n'a pas de numéro dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-21.

## Causes fréquentes

- **Une ligne ajoutée à la main**, un commentaire ou une ligne de remise, que le logiciel ne numérote pas.
- **Des lignes numérotées sur le PDF seulement.**

## Détails techniques

L'identifiant de ligne est BT-126. En CII, c'est le `ram:LineID` du `ram:AssociatedDocumentLineDocument` de la ligne ; en UBL, le `cbc:ID` de `cac:InvoiceLine` (`cac:CreditNoteLine` dans un avoir).

La facture d'exemple laisse vide l'identifiant de sa première ligne, donc elle échoue à BR-21 seule.

## Texte officiel

> Each Invoice line (BG-25) shall have an Invoice line identifier (BT-126).

BR-21, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-25](../BR-25/) : chaque ligne de facture doit nommer ce qu'elle facture.
- [BR-16](../BR-16/) : toute facture doit contenir au moins une ligne, avoirs compris : pour un montant global, une seule ligne suffit.
