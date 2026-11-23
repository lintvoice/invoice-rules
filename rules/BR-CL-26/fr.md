# Le type de l'identifiant du lieu de livraison n'est pas un code valide

Le code qui dit de quel type est l'identifiant du lieu de livraison n'est pas dans la liste officielle.

## Ce que vérifie la règle

Une facture peut identifier le lieu de livraison, un entrepôt ou un site, par un identifiant comme un GLN ou un SIRET. Un code à quatre chiffres de la liste ISO 6523 dit de quel type il s'agit : 0088 pour un GLN, 0009 pour un SIRET. La règle vérifie que ce code vient de cette liste, et non un nom comme « GLN ».

## Pourquoi c'est important

BR-CL-26 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-26 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le type d'identifiant dans la liste de votre logiciel, plutôt que de le saisir.
2. Vérifiez que la facture électronique écrit le code à quatre chiffres à côté de l'identifiant.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-26.

## Causes fréquentes

- **Le nom du registre au lieu de son code**, comme GLN, SIRET ou EAN.
- **Un code sans ses zéros de tête**, 88 pour 0088.

## Détails techniques

L'identifiant du lieu de livraison est BT-71, son identifiant de schéma BT-71-1. En CII, c'est le `schemeID` de `ram:GlobalID` dans `ram:ShipToTradeParty` ; en UBL, le `schemeID` de `cbc:ID` dans `cac:DeliveryLocation`. La liste est la liste ISO 6523 ICD.

La facture d'exemple indique un lieu de livraison dont le GLN a le schéma `GLN` au lieu de `0088`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000585`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Delivery location identifier scheme identifier MUST belong to the ISO 6523 ICD code list

BR-CL-26, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-10](../BR-CL-10/) : le code qui dit de quel registre vient l'identifiant d'une partie doit être dans la liste ISO 6523, comme 0088 pour un GLN.
- [BR-57](../BR-57/) : quand la facture indique une adresse de livraison, elle doit en indiquer le pays, avec son code à deux lettres.
