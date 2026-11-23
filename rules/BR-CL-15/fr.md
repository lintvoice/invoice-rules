# Le pays d'origine d'un article n'est pas un code pays

Le pays d'origine d'un article n'est pas un code pays.

## Ce que vérifie la règle

Une ligne peut indiquer d'où vient son article. Les pays s'écrivent avec leur code ISO 3166-1 à deux lettres : DE pour l'Allemagne, FR pour la France, BE pour la Belgique… La règle vérifie que ce pays d'origine est un tel code, et non le nom du pays ou une autre abréviation.

## Pourquoi c'est important

BR-CL-15 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-15 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le pays dans la liste de votre logiciel, plutôt que de le saisir.
2. Vérifiez que la facture électronique écrit le code à deux lettres, FR pour la France.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-15.

## Causes fréquentes

- **Le nom du pays au lieu de son code**, comme France ou Deutschland.
- **Un code qui n'est pas celui de l'ISO**, comme UK pour le Royaume-Uni, là où l'ISO 3166-1 a GB.

## Détails techniques

Le pays d'origine de l'article est BT-159. En CII, c'est le `ram:ID` de `ram:OriginTradeCountry` dans le `ram:SpecifiedTradeProduct` d'une ligne ; en UBL, le `cbc:IdentificationCode` du `cac:OriginCountry` de l'article. La liste est celle des codes à deux lettres de l'ISO 3166-1.

La facture d'exemple écrit le pays d'origine de sa première ligne `France` au lieu de `FR`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000628`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Country codes in an invoice MUST be coded using ISO code list 3166-1

BR-CL-15, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-14](../BR-CL-14/) : chaque pays des adresses de la facture doit être un code ISO 3166-1 à deux lettres, comme DE ou FR.
