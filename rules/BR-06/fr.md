# Le nom du vendeur manque

Le nom du vendeur est vide.

## Ce que vérifie la règle

Une facture nomme son vendeur : le nom de la société, ou celui de la personne pour un entrepreneur individuel. La règle vérifie que la facture électronique l'indique.

## Pourquoi c'est important

BR-06 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-06 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez le nom du vendeur dans les paramètres de votre logiciel.
2. Vérifiez que le nom imprimé sur le PDF figure aussi dans la facture électronique.
3. Si le nom manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-06.

## Causes fréquentes

- **Un logo à la place du nom** sur le PDF, sans nom dans les paramètres.
- **Un nom imprimé sur le PDF** mais absent des données de la facture électronique.

## Détails techniques

Le nom du vendeur est BT-27. En CII, c'est le `ram:Name` de `ram:SellerTradeParty` ; en UBL, le `cbc:RegistrationName` du `cac:PartyLegalEntity` de la partie.

La facture d'exemple laisse le nom du vendeur vide.

## Texte officiel

> An Invoice shall contain the Seller name (BT-27).

BR-06, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-07](../BR-07/) : toute facture doit indiquer le nom de l'acheteur.
- [BR-08](../BR-08/) : toute facture doit indiquer l'adresse postale du vendeur, avec au moins son pays.
