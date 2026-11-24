# Le type d'un fichier joint n'est pas admis

Un fichier joint à la facture déclare un type qui n'est pas admis.

## Ce que vérifie la règle

Une facture électronique peut porter des fichiers en elle : une feuille de temps, un bon de livraison… Chaque fichier déclare son type, son code MIME. Seuls six types sont admis : application/pdf, image/png, image/jpeg, text/csv, et les types des tableurs XLSX et ODS. La règle vérifie que chaque fichier joint déclare l'un d'eux.

## Pourquoi c'est important

BR-CL-24 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-24 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Joignez vos justificatifs en PDF, PNG, JPEG, CSV, XLSX ou ODS ; convertissez les autres.
2. Vérifiez que la facture électronique déclare le type exact du fichier, text/csv pour un fichier CSV.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-24.

## Causes fréquentes

- **Un document Word ou une archive ZIP** joints tels quels.
- **Un type générique**, text/plain pour un fichier CSV.

## Détails techniques

Le document joint est BT-125, son code MIME BT-125-1. En CII, c'est le `mimeCode` de `ram:AttachmentBinaryObject` dans un `ram:AdditionalReferencedDocument` ; en UBL, le `mimeCode` de `cbc:EmbeddedDocumentBinaryObject`. La liste est la même dans les deux syntaxes : `application/pdf`, `image/png`, `image/jpeg`, `text/csv`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` et `application/vnd.oasis.opendocument.spreadsheet`.

La facture d'exemple joint une feuille de temps CSV déclarée en `text/plain` ; sa version corrigée déclare `text/csv`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000287`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> For Mime code in attribute use MIMEMediaType.

BR-CL-24, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-52](../BR-52/) : chaque justificatif auquel une facture fait référence doit indiquer sa référence.
- [BR-FR-17](../BR-FR-17/) : chaque pièce jointe doit être décrite par un des 12 codes de la liste française, par exemple RIB, BON_COMMANDE ou LISIBLE.
