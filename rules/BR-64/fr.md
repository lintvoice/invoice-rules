# L'identifiant standard d'un article ne dit pas de quel type d'identifiant il s'agit

L'identifiant standard d'un article est indiqué sans le code qui dit de quel type d'identifiant il s'agit.

## Ce que vérifie la règle

Une ligne peut identifier son article par un identifiant standard, comme le GTIN imprimé sous un code-barres. Un code dit de quel type d'identifiant il s'agit : 0160 pour un GTIN, par exemple. La règle vérifie qu'un identifiant standard est toujours accompagné de ce code.

## Pourquoi c'est important

BR-64 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-64 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le type d'identifiant dans votre logiciel, s'il le demande.
2. Vérifiez que la facture électronique en écrit le code à côté de la valeur.
3. Si le code manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-64.

## Causes fréquentes

- **L'identifiant standard d'un article recopié comme une simple valeur**, sans son code.
- **Un export qui écrit la valeur et laisse tomber ses attributs.**

## Détails techniques

L'identifiant standard de l'article est BT-157, son identifiant de schéma BT-157-1. En CII, la règle lit le `schemeID` de `ram:GlobalID` dans le `ram:SpecifiedTradeProduct` d'une ligne ; en UBL, le `schemeID` de `cbc:ID` dans `cac:StandardItemIdentification`. Ses codes viennent de la liste ISO 6523 ICD, comme l'exige la règle BR-CL-21.

La facture d'exemple indique l'identifiant standard d'un article sans son schéma. La règle de syntaxe CII `CII-SR-046`, qui exige le même schéma, échoue aussi. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence du schéma : dans une facture Factur-X, sa règle `FX-SCH-A-000551` échoue donc à côté de BR-64, comme dans la facture d'exemple.

## Texte officiel

> The Item standard identifier (BT-157) shall have a Scheme identifier.

BR-64, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-21](../BR-CL-21/) : le code qui dit de quel type est l'identifiant standard d'un article doit être dans la liste ISO 6523, comme 0160 pour un GTIN.
- [BR-65](../BR-65/) : la classification d'un article doit dire, avec un code normalisé, de quel type de classification il s'agit.
