# Le représentant fiscal n'a pas d'adresse postale

La facture indique un représentant fiscal du vendeur, sans son adresse postale.

## Ce que vérifie la règle

Certains vendeurs agissent par un représentant fiscal, une société qui gère leur TVA dans un pays où ils ne sont pas établis. Quand la facture en indique un, la règle vérifie qu'elle donne l'adresse postale du représentant.

## Pourquoi c'est important

BR-19 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-19 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez l'adresse postale du représentant fiscal dans votre logiciel, pays compris.
2. Vérifiez que la facture électronique donne le nom du représentant, son adresse postale avec son pays, et son numéro de TVA.
3. S'ils manquent dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-19.

## Causes fréquentes

- **Un représentant saisi avec son seul nom.**
- **Un représentant saisi avec son seul numéro de TVA**, ses autres coordonnées restées dans un autre outil.

## Détails techniques

L'adresse postale du représentant fiscal est le groupe BG-12. En CII, la règle cherche `ram:PostalTradeAddress` dans `ram:SellerTaxRepresentativeTradeParty` ; en UBL, `cac:PostalAddress` dans `cac:TaxRepresentativeParty`.

La facture d'exemple indique un représentant fiscal sans adresse. Sans adresse, il n'y a pas non plus de code pays, donc BR-20 échoue aussi. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence de l'adresse : dans une facture Factur-X, sa règle `FX-SCH-A-000432` échoue donc à côté de BR-19, comme dans la facture d'exemple.

## Texte officiel

> The Seller tax representative postal address (BG-12) shall be provided in the Invoice, if the Seller (BG-4) has a Seller tax representative party (BG-11).

BR-19, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-18](../BR-18/) : quand le vendeur a un représentant fiscal, la facture doit en indiquer le nom.
- [BR-20](../BR-20/) : quand le vendeur a un représentant fiscal, son adresse postale doit indiquer son pays, avec son code à deux lettres.
- [BR-56](../BR-56/) : quand le vendeur a un représentant fiscal, la facture doit indiquer le numéro de TVA du représentant.
