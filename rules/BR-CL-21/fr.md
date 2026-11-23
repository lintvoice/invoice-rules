# Le type de l'identifiant d'un article n'est pas un code valide

Le code qui dit de quel type est l'identifiant standard d'un article n'est pas dans la liste officielle.

## Ce que vérifie la règle

Une ligne peut identifier son article par un identifiant standard, comme le GTIN imprimé sous un code-barres. Un code à quatre chiffres de la liste ISO 6523 dit de quel type il s'agit : 0160 pour un GTIN. La règle vérifie que ce code vient de cette liste, et non un nom comme « EAN ».

## Pourquoi c'est important

BR-CL-21 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-21 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le type d'identifiant dans la liste de votre logiciel.
2. Vérifiez que la facture électronique écrit 0160 à côté d'un GTIN.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-21.

## Causes fréquentes

- **Le nom du code-barres au lieu du code**, comme EAN ou GTIN.
- **Un code sans son zéro de tête**, 160 pour 0160.

## Détails techniques

L'identifiant standard de l'article est BT-157, son identifiant de schéma BT-157-1. En CII, c'est le `schemeID` de `ram:GlobalID` dans le `ram:SpecifiedTradeProduct` d'une ligne ; en UBL, le `schemeID` de `cbc:ID` dans `cac:StandardItemIdentification`. La liste est la liste ISO 6523 ICD.

La facture d'exemple donne à l'article de sa première ligne un GTIN avec le schéma `EAN` au lieu de `0160`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000626`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Item standard identifier scheme identifier MUST belong to the ISO 6523 ICD code list

BR-CL-21, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-64](../BR-64/) : l'identifiant standard d'un article doit dire, avec un code normalisé, de quel type d'identifiant il s'agit.
- [BR-CL-10](../BR-CL-10/) : le code qui dit de quel registre vient l'identifiant d'une partie doit être dans la liste ISO 6523, comme 0088 pour un GLN.
