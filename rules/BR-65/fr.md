# La classification d'un article ne dit pas de quel type de classification il s'agit

La classification d'un article est indiquée sans le code qui dit de quel type de classification il s'agit.

## Ce que vérifie la règle

Une ligne peut classer son article dans un système de classification, comme UNSPSC ou le vocabulaire commun pour les marchés publics de l'UE (CPV). Un code dit de quel système vient la classification : TST pour UNSPSC, STI pour CPV. La règle vérifie qu'une classification est toujours accompagnée de ce code.

## Pourquoi c'est important

BR-65 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-65 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le type de classification dans votre logiciel, s'il le demande.
2. Vérifiez que la facture électronique en écrit le code à côté de la valeur.
3. Si le code manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-65.

## Causes fréquentes

- **La classification d'un article recopiée comme une simple valeur**, sans son code.
- **Un export qui écrit la valeur et laisse tomber ses attributs.**

## Détails techniques

L'identifiant de classification de l'article est BT-158, son identifiant de schéma BT-158-1. En CII, la règle lit le `listID` de `ram:ClassCode` dans le `ram:DesignatedProductClassification` d'une ligne ; en UBL, le `listID` de `cbc:ItemClassificationCode` dans `cac:CommodityClassification`. Ses codes viennent de la liste UNTDID 7143, comme l'exige la règle BR-CL-13.

La facture d'exemple indique la classification d'un article sans son schéma. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence du schéma : dans une facture Factur-X, sa règle `FX-SCH-A-000296` échoue donc à côté de BR-65, comme dans la facture d'exemple.

## Texte officiel

> The Item classification identifier (BT-158) shall have a Scheme identifier.

BR-65, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-13](../BR-CL-13/) : le code qui dit de quel système de classification vient la classe d'un article doit être dans la liste officielle, comme TST pour UNSPSC.
- [BR-64](../BR-64/) : l'identifiant standard d'un article doit dire, avec un code normalisé, de quel type d'identifiant il s'agit.
