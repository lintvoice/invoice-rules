# L'acheteur n'a pas d'adresse postale

La facture n'indique pas d'adresse postale pour l'acheteur.

## Ce que vérifie la règle

Une facture indique l'adresse postale de l'acheteur. Dans une facture électronique, l'adresse est un bloc de champs : rue, ville, code postal, pays… La règle vérifie que ce bloc est présent ; une autre règle, BR-11, vérifie qu'il donne au moins le pays.

## Pourquoi c'est important

BR-10 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-10 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez l'adresse complète de l'acheteur dans votre logiciel, pays compris.
2. Vérifiez que l'adresse imprimée sur le PDF figure aussi dans la facture électronique.
3. Si l'adresse manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-10.

## Causes fréquentes

- **Une adresse imprimée sur le PDF** mais absente des données de la facture électronique.
- **Une fiche client sans adresse**, pour un client connu seulement par e-mail.

## Détails techniques

L'adresse postale de l'acheteur est le groupe BG-8. En CII, la règle cherche `ram:PostalTradeAddress` dans `ram:BuyerTradeParty` ; en UBL, le `cac:PostalAddress` de la partie.

La facture d'exemple n'a pas d'adresse pour l'acheteur. Sans adresse, il n'y a pas non plus de code pays, donc BR-11 échoue aussi. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence de l'adresse : dans une facture Factur-X, sa règle `FX-SCH-A-000419` échoue donc à côté de BR-10, comme dans la facture d'exemple.

## Texte officiel

> An Invoice shall contain the Buyer postal address (BG-8).

BR-10, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-11](../BR-11/) : l'adresse postale de l'acheteur doit indiquer son pays, avec son code à deux lettres comme DE ou FR.
- [BR-07](../BR-07/) : toute facture doit indiquer le nom de l'acheteur.
- [BR-08](../BR-08/) : toute facture doit indiquer l'adresse postale du vendeur, avec au moins son pays.
