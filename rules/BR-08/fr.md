# Le vendeur n'a pas d'adresse postale

La facture n'indique pas d'adresse postale pour le vendeur.

## Ce que vérifie la règle

Une facture indique l'adresse postale du vendeur. Dans une facture électronique, l'adresse est un bloc de champs : rue, ville, code postal, pays… La règle vérifie que ce bloc est présent ; une autre règle, BR-09, vérifie qu'il donne au moins le pays.

## Pourquoi c'est important

BR-08 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-08 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez l'adresse complète du vendeur dans votre logiciel, pays compris.
2. Vérifiez que l'adresse imprimée sur le PDF figure aussi dans la facture électronique.
3. Si l'adresse manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-08.

## Causes fréquentes

- **Une adresse imprimée sur le PDF** mais absente des données de la facture électronique.
- **Des paramètres remplis sans adresse**, le PDF la montrant depuis une image d'en-tête.

## Détails techniques

L'adresse postale du vendeur est le groupe BG-5. En CII, la règle cherche `ram:PostalTradeAddress` dans `ram:SellerTradeParty` ; en UBL, le `cac:PostalAddress` de la partie.

La facture d'exemple n'a pas d'adresse pour le vendeur. Sans adresse, il n'y a pas non plus de code pays, donc BR-09 échoue aussi. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence de l'adresse : dans une facture Factur-X, sa règle `FX-SCH-A-000032` échoue donc à côté de BR-08, comme dans la facture d'exemple.

## Texte officiel

> An Invoice shall contain the Seller postal address (BG-5).

BR-08, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-09](../BR-09/) : l'adresse postale du vendeur doit indiquer son pays, avec son code à deux lettres comme DE ou FR.
- [BR-06](../BR-06/) : toute facture doit indiquer le nom du vendeur.
- [BR-10](../BR-10/) : toute facture doit indiquer l'adresse postale de l'acheteur, avec au moins son pays.
