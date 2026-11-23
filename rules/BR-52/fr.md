# Un justificatif n'a pas de référence

Un justificatif de la facture a une référence vide.

## Ce que vérifie la règle

Une facture peut faire référence à des justificatifs : une feuille de temps, un bon de livraison, un fichier joint… Chacun est désigné par sa référence, le numéro ou le nom qui l'identifie. La règle vérifie que chaque justificatif en a une.

## Pourquoi c'est important

BR-52 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-52 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Donnez à chaque justificatif sa référence dans votre logiciel, son numéro ou son nom de fichier par exemple.
2. Vérifiez que la facture électronique l'écrit.
3. Si elle manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-52.

## Causes fréquentes

- **Un fichier joint sans référence.**
- **Une référence gardée dans la description du fichier** au lieu de son propre champ.

## Détails techniques

Un justificatif additionnel est le groupe BG-24, sa référence BT-122. En CII, c'est le `ram:IssuerAssignedID` de chaque `ram:AdditionalReferencedDocument` de `ram:ApplicableHeaderTradeAgreement`, quel que soit son type : en CII, le même élément porte aussi l'identifiant de l'objet facturé, BT-18, avec le code type 130. En UBL, le `cbc:ID` de chaque `cac:AdditionalDocumentReference`.

La facture d'exemple française indique un objet facturé de type AFL dont la référence est vide : la règle française BR-FR-29, sur ce type de référence, échoue donc avec BR-52.

## Texte officiel

> Each Additional supporting document (BG-24) shall contain a Supporting document reference (BT-122).

BR-52, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-FR-29](../BR-FR-29/) : la facture peut donner au plus une référence d'objet facturé de type AFL et une de type AVV, et aucune ne doit être vide.
- [BR-CL-24](../BR-CL-24/) : un fichier joint à la facture doit être un PDF, une image PNG ou JPEG, un fichier CSV ou un tableur (XLSX, ODS), déclaré avec son type.
