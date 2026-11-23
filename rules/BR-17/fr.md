# Le bénéficiaire n'a pas de nom, ou c'est le vendeur lui-même

La facture indique un bénéficiaire qui n'a pas de nom, ou qui est le vendeur lui-même.

## Ce que vérifie la règle

Une facture peut indiquer que le paiement va à quelqu'un d'autre que le vendeur, une société d'affacturage par exemple : le bénéficiaire. Dans ce cas, la règle vérifie que le bénéficiaire a un nom, et qu'il est différent du vendeur : ni le nom du vendeur, ni son identifiant, ni son numéro d'immatriculation légale.

## Pourquoi c'est important

BR-17 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-17 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Si c'est le vendeur qui est payé, n'indiquez pas de bénéficiaire.
2. Si quelqu'un d'autre est payé, indiquez le nom de ce bénéficiaire et ses propres identifiants.
3. Si votre logiciel remplit le bénéficiaire avec les coordonnées du vendeur, signalez-le à l'éditeur de votre logiciel en citant BR-17.

## Causes fréquentes

- **Les coordonnées du vendeur recopiées dans le bénéficiaire** par un logiciel qui le remplit toujours.
- **Un bénéficiaire donné par son seul identifiant**, sans son nom.

## Détails techniques

Le bénéficiaire est le groupe BG-10, son nom BT-59. En CII, la règle lit `ram:Name`, `ram:ID` et `ram:SpecifiedLegalOrganization/ram:ID` de `ram:PayeeTradeParty`, dans `ram:ApplicableHeaderTradeSettlement`, et les compare à ceux du vendeur ; en UBL, `cac:PayeeParty`.

La facture d'exemple reprend le vendeur comme bénéficiaire, avec son propre nom, donc elle échoue à BR-17 seule.

## Texte officiel

> The Payee name (BT-59) shall be provided in the Invoice, if the Payee (BG-10) is different from the Seller (BG-4).

BR-17, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-FR-CO-10](../BR-FR-CO-10/) : chaque identifiant d'une partie doit dire de quel type il est (SIRET, GLN…), et une partie ne peut pas avoir deux identifiants du même type.
- [BR-06](../BR-06/) : toute facture doit indiquer le nom du vendeur.
