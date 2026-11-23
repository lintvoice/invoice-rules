# Le système de classification d'un article n'est pas un code valide

Le code qui dit de quel système de classification vient la classe d'un article n'est pas dans la liste officielle.

## Ce que vérifie la règle

Une ligne peut classer son article dans un système de classification, comme UNSPSC ou le vocabulaire commun pour les marchés publics de l'UE (CPV). Un code de la liste officielle dit de quel système il s'agit : TST pour UNSPSC, STI pour CPV. La règle vérifie que ce code vient de cette liste, et non le nom du système.

## Pourquoi c'est important

BR-CL-13 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-13 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le système de classification dans la liste de votre logiciel.
2. Vérifiez que la facture électronique en écrit le code, TST pour UNSPSC ou STI pour CPV.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-13.

## Causes fréquentes

- **Le nom du système au lieu de son code**, comme UNSPSC ou CPV.
- **Un code inventé pour un catalogue interne.**

## Détails techniques

L'identifiant de classification de l'article est BT-158, son identifiant de schéma BT-158-1. En CII, c'est le `listID` de `ram:ClassCode` dans le `ram:DesignatedProductClassification` d'une ligne ; en UBL, le `listID` de `cbc:ItemClassificationCode`. La liste est une partie de l'UNTDID 7143.

La facture d'exemple classe l'article de sa première ligne sous UNSPSC 86101700, les services de formation professionnelle non scientifique, avec le schéma écrit `UNSPSC` au lieu de `TST`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000297`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Item classification identifier identification scheme identifier MUST be coded using one of the UNTDID 7143 list.

BR-CL-13, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-65](../BR-65/) : la classification d'un article doit dire, avec un code normalisé, de quel type de classification il s'agit.
- [BR-CL-21](../BR-CL-21/) : le code qui dit de quel type est l'identifiant standard d'un article doit être dans la liste ISO 6523, comme 0160 pour un GTIN.
