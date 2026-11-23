# Le numéro de facture manque

Le numéro de facture est vide.

## Ce que vérifie la règle

Toute facture a un numéro qui l'identifie, attribué par le vendeur et unique parmi ses factures. La règle vérifie que la facture électronique en indique un.

## Pourquoi c'est important

BR-02 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-02 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Donnez à chaque facture son numéro dans votre logiciel avant de l'émettre.
2. Vérifiez que le numéro imprimé sur le PDF figure aussi dans la facture électronique.
3. Si le numéro manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-02.

## Causes fréquentes

- **Une facture envoyée encore à l'état de brouillon**, avant que le logiciel ne la numérote.
- **Un numéro imprimé sur le PDF** mais absent des données de la facture électronique.

## Détails techniques

Le numéro de facture est BT-1. En CII, c'est le `ram:ID` de `rsm:ExchangedDocument` ; en UBL, le `cbc:ID` de la facture.

La facture d'exemple laisse le numéro vide. Sur une facture française, la règle BR-FR-02, sur les caractères admis dans un numéro, échoue aussi, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> An Invoice shall have an Invoice number (BT-1).

BR-02, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-FR-01](../BR-FR-01/) : le numéro de la facture, et celui d'une facture qu'elle cite, ne doivent pas dépasser 35 caractères.
- [BR-FR-02](../BR-FR-02/) : le numéro de facture ne doit contenir que des lettres, des chiffres et les signes + - _ /, sans espace.
- [BR-03](../BR-03/) : toute facture doit indiquer sa date d'émission, écrite comme une date.
