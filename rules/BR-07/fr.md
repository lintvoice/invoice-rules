# Le nom de l'acheteur manque

Le nom de l'acheteur est vide.

## Ce que vérifie la règle

Une facture nomme son acheteur : le nom de la société, ou celui de la personne pour un entrepreneur individuel. La règle vérifie que la facture électronique l'indique.

## Pourquoi c'est important

BR-07 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-07 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez le nom de l'acheteur dans la fiche client de votre logiciel.
2. Vérifiez que le nom imprimé sur le PDF figure aussi dans la facture électronique.
3. Si le nom manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-07.

## Causes fréquentes

- **Une fiche client créée à partir d'une adresse e-mail**, sans nom.
- **Un nom imprimé sur le PDF** mais absent des données de la facture électronique.

## Détails techniques

Le nom de l'acheteur est BT-44. En CII, c'est le `ram:Name` de `ram:BuyerTradeParty` ; en UBL, le `cbc:RegistrationName` du `cac:PartyLegalEntity` de la partie.

La facture d'exemple laisse le nom de l'acheteur vide.

## Texte officiel

> An Invoice shall contain the Buyer name (BT-44).

BR-07, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-06](../BR-06/) : toute facture doit indiquer le nom du vendeur.
- [BR-10](../BR-10/) : toute facture doit indiquer l'adresse postale de l'acheteur, avec au moins son pays.
