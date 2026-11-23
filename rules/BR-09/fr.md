# L'adresse du vendeur n'a pas de pays

Le pays de l'adresse du vendeur est vide.

## Ce que vérifie la règle

Une facture électronique indique le pays de chaque adresse par un code à deux lettres : DE pour l'Allemagne, FR pour la France, BE pour la Belgique… Le pays dit quelles règles et quelle TVA s'appliquent, donc le logiciel qui reçoit la facture en a besoin. La règle vérifie que l'adresse du vendeur l'indique.

## Pourquoi c'est important

BR-09 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-09 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez le pays de l'adresse du vendeur dans votre logiciel.
2. Vérifiez que la facture électronique en écrit le code à deux lettres, et non le nom du pays.
3. Si le pays reste vide, signalez-le à l'éditeur de votre logiciel en citant BR-09.

## Causes fréquentes

- **Une adresse saisie sans pays**, parce que l'entreprise ne travaille que dans son pays.
- **Un champ pays resté vide** dans une fiche importée d'un autre outil.

## Détails techniques

Le code pays de l'adresse du vendeur est BT-40. En CII, c'est le `ram:CountryID` de `ram:PostalTradeAddress` dans `ram:SellerTradeParty` ; en UBL, le `cbc:IdentificationCode` du `cac:Country` de l'adresse. Son code vient de l'ISO 3166-1, comme l'exige la règle BR-CL-14.

La facture d'exemple laisse le code pays vide. Un code vide n'est pas dans l'ISO 3166-1, donc BR-CL-14 échoue aussi, et l'exemple échoue aux deux règles. Le contrôle propre au profil Factur-X sur les codes pays ne lit qu'un code présent.

## Texte officiel

> The Seller postal address (BG-5) shall contain a Seller country code (BT-40).

BR-09, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-08](../BR-08/) : toute facture doit indiquer l'adresse postale du vendeur, avec au moins son pays.
- [BR-CL-14](../BR-CL-14/) : chaque pays des adresses de la facture doit être un code ISO 3166-1 à deux lettres, comme DE ou FR.
- [BR-11](../BR-11/) : l'adresse postale de l'acheteur doit indiquer son pays, avec son code à deux lettres comme DE ou FR.
