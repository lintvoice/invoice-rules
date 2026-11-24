# L'adresse du représentant fiscal n'a pas de pays

Le pays de l'adresse du représentant fiscal est vide.

## Ce que vérifie la règle

Certains vendeurs agissent par un représentant fiscal, une société qui gère leur TVA dans un pays où ils ne sont pas établis. Quand la facture en indique un, la règle vérifie que l'adresse du représentant donne son pays, par un code à deux lettres comme DE ou FR.

## Pourquoi c'est important

BR-20 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-20 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez le pays de l'adresse du représentant fiscal dans votre logiciel.
2. Vérifiez que la facture électronique donne le nom du représentant, son adresse postale avec son pays, et son numéro de TVA.
3. S'ils manquent dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-20.

## Causes fréquentes

- **Une adresse saisie sans pays.**
- **Un représentant saisi avec son seul numéro de TVA**, ses autres coordonnées restées dans un autre outil.

## Détails techniques

Le code pays de l'adresse du représentant fiscal est BT-69. En CII, c'est le `ram:CountryID` de `ram:PostalTradeAddress` dans `ram:SellerTaxRepresentativeTradeParty` ; en UBL, le `cbc:IdentificationCode` du `cac:Country` de l'adresse. Son code vient de l'ISO 3166-1, comme l'exige la règle BR-CL-14.

La facture d'exemple laisse le code pays vide. Un code vide n'est pas dans l'ISO 3166-1, donc BR-CL-14 échoue aussi, et l'exemple échoue aux deux règles. Le contrôle propre au profil Factur-X sur les codes pays ne lit qu'un code présent.

## Texte officiel

> The Seller tax representative postal address (BG-12) shall contain a Tax representative country code (BT-69), if the Seller (BG-4) has a Seller tax representative party (BG-11).

BR-20, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-19](../BR-19/) : quand le vendeur a un représentant fiscal, la facture doit en indiquer l'adresse postale.
- [BR-CL-14](../BR-CL-14/) : chaque pays des adresses de la facture doit être un code ISO 3166-1 à deux lettres, comme DE ou FR.
- [BR-56](../BR-56/) : quand le vendeur a un représentant fiscal, la facture doit indiquer le numéro de TVA du représentant.
