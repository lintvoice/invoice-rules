# L'adresse de livraison n'a pas de pays

Le pays de l'adresse de livraison est vide.

## Ce que vérifie la règle

Une facture peut indiquer l'adresse où les biens ont été livrés ou la prestation réalisée, quand elle diffère de celle de l'acheteur. Le pays de livraison peut changer la TVA applicable. Quand la facture indique une adresse de livraison, la règle vérifie qu'elle en donne le pays, par un code à deux lettres comme DE ou FR.

## Pourquoi c'est important

BR-57 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-57 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez le pays de chaque adresse de livraison dans votre logiciel.
2. Vérifiez que la facture électronique en écrit le code à deux lettres, et non le nom du pays.
3. Si le pays reste vide, signalez-le à l'éditeur de votre logiciel en citant BR-57.

## Causes fréquentes

- **Une adresse de livraison saisie sans pays**, en texte libre.
- **Un site de livraison importé d'un autre outil** sans son pays.

## Détails techniques

L'adresse de livraison est le groupe BG-15, son code pays BT-80. En CII, c'est le `ram:CountryID` de `ram:PostalTradeAddress` dans `ram:ShipToTradeParty` ; en UBL, le `cbc:IdentificationCode` du `cac:Country` de `cac:Address` dans `cac:DeliveryLocation`. Son code vient de l'ISO 3166-1, comme l'exige la règle BR-CL-14.

La facture d'exemple indique une adresse de livraison au code pays vide. Un code vide n'est pas dans l'ISO 3166-1, donc BR-CL-14 échoue aussi, et l'exemple échoue aux deux règles. Le contrôle propre au profil Factur-X sur les codes pays ne lit qu'un code présent.

## Texte officiel

> Each Deliver to address (BG-15) shall contain a Deliver to country code (BT-80).

BR-57, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-14](../BR-CL-14/) : chaque pays des adresses de la facture doit être un code ISO 3166-1 à deux lettres, comme DE ou FR.
- [BR-09](../BR-09/) : l'adresse postale du vendeur doit indiquer son pays, avec son code à deux lettres comme DE ou FR.
- [BR-11](../BR-11/) : l'adresse postale de l'acheteur doit indiquer son pays, avec son code à deux lettres comme DE ou FR.
