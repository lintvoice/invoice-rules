# La date de facture manque

La date d'émission de la facture manque, ou n'est pas écrite comme une date.

## Ce que vérifie la règle

Toute facture indique la date à laquelle elle a été émise. La facture électronique l'écrit sous une forme fixe : année, mois et jour, sans rien d'autre. La règle vérifie que la facture indique sa date d'émission sous cette forme.

## Pourquoi c'est important

BR-03 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-03 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez que chaque facture a sa date d'émission dans votre logiciel.
2. Vérifiez que la facture électronique l'écrit comme une date seule, sans heure.
3. Si la date manque ou est écrite avec une heure, signalez-le à l'éditeur de votre logiciel en citant BR-03.

## Causes fréquentes

- **Une date écrite avec une heure**, comme un horodatage tiré d'une base de données.
- **Une date laissée vide** dans un brouillon envoyé trop tôt.

## Détails techniques

La date d'émission est BT-2. En CII, la règle lit le `udt:DateTimeString` de `ram:IssueDateTime` dans `rsm:ExchangedDocument`, et seulement avec l'attribut `format="102"`, la forme AAAAMMJJ. En UBL, elle lit `cbc:IssueDate`.

La facture d'exemple écrit la date et l'heure `202610201430` au format 203. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi le format de la date : dans une facture Factur-X, sa règle `FX-SCH-A-000554` échoue donc à côté de BR-03, comme dans la facture d'exemple.

## Texte officiel

> An Invoice shall have an Invoice issue date (BT-2).

BR-03, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-02](../BR-02/) : toute facture doit avoir un numéro.
- [BR-FR-03](../BR-FR-03/) : chaque date de la facture doit être une vraie date, avec une année comprise entre 2000 et 2099.
