# Le représentant fiscal n'a pas de nom

La facture indique un représentant fiscal du vendeur, mais son nom est vide.

## Ce que vérifie la règle

Certains vendeurs agissent par un représentant fiscal, une société qui gère leur TVA dans un pays où ils ne sont pas établis. Quand la facture en indique un, la règle vérifie qu'elle donne le nom du représentant.

## Pourquoi c'est important

BR-18 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-18 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez le nom du représentant fiscal dans votre logiciel.
2. Vérifiez que la facture électronique donne le nom du représentant, son adresse postale avec son pays, et son numéro de TVA.
3. S'ils manquent dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-18.

## Causes fréquentes

- **Le nom du représentant présent seulement dans un en-tête**, pas dans les données du logiciel.
- **Un représentant saisi avec son seul numéro de TVA**, ses autres coordonnées restées dans un autre outil.

## Détails techniques

Le représentant fiscal du vendeur est le groupe BG-11, son nom BT-62. En CII, c'est le `ram:Name` de `ram:SellerTaxRepresentativeTradeParty`, dans `ram:ApplicableHeaderTradeAgreement` ; en UBL, le `cbc:Name` du `cac:PartyName` de `cac:TaxRepresentativeParty`.

La facture d'exemple indique un représentant fiscal au nom vide, donc elle échoue à BR-18 seule.

## Texte officiel

> The Seller tax representative name (BT-62) shall be provided in the Invoice, if the Seller (BG-4) has a Seller tax representative party (BG-11).

BR-18, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-19](../BR-19/) : quand le vendeur a un représentant fiscal, la facture doit en indiquer l'adresse postale.
- [BR-20](../BR-20/) : quand le vendeur a un représentant fiscal, son adresse postale doit indiquer son pays, avec son code à deux lettres.
- [BR-56](../BR-56/) : quand le vendeur a un représentant fiscal, la facture doit indiquer le numéro de TVA du représentant.
