# Un pays n'est pas écrit sous forme de code pays

Un pays de la facture n'est pas un code pays.

## Ce que vérifie la règle

Les pays s'écrivent avec leur code ISO 3166-1 à deux lettres : DE pour l'Allemagne, FR pour la France, BE pour la Belgique… La règle vérifie que le pays de chaque adresse de la facture est un tel code, et non le nom du pays ou une autre abréviation.

## Pourquoi c'est important

BR-CL-14 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-14 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le pays dans la liste de votre logiciel, plutôt que de le saisir.
2. Vérifiez que la facture électronique écrit le code à deux lettres, FR pour la France.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-14.

## Causes fréquentes

- **Le nom du pays au lieu de son code**, comme France ou Deutschland.
- **Un code qui n'est pas celui de l'ISO**, comme UK pour le Royaume-Uni, là où l'ISO 3166-1 a GB.

## Détails techniques

La règle lit chaque code pays d'une adresse : celui du vendeur (BT-40), de l'acheteur (BT-55), du représentant fiscal (BT-69) et de l'adresse de livraison (BT-80). En CII, c'est chaque `ram:CountryID` ; en UBL, le `cbc:IdentificationCode` de chaque `cac:Country`. La liste est celle des codes à deux lettres de l'ISO 3166-1. Le pays d'origine d'un article a sa propre règle, BR-CL-15.

La facture d'exemple écrit le pays de l'acheteur `France` au lieu de `FR`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000568`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Country codes in an invoice MUST be coded using ISO code list 3166-1

BR-CL-14, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-09](../BR-09/) : l'adresse postale du vendeur doit indiquer son pays, avec son code à deux lettres comme DE ou FR.
- [BR-11](../BR-11/) : l'adresse postale de l'acheteur doit indiquer son pays, avec son code à deux lettres comme DE ou FR.
- [BR-57](../BR-57/) : quand la facture indique une adresse de livraison, elle doit en indiquer le pays, avec son code à deux lettres.
- [BR-CL-15](../BR-CL-15/) : le pays d'origine d'un article doit être un code ISO 3166-1 à deux lettres, comme DE ou FR.
