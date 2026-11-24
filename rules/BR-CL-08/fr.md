# Le sujet d'une note n'est pas un code valide

Le code qui indique le sujet d'une note n'est pas dans la liste officielle.

## Ce que vérifie la règle

Une facture peut porter des notes, et chaque note peut indiquer son sujet par un code : AAI pour une information générale, PMT pour une information de paiement, AAB pour des conditions de paiement… Certains pays s'en servent pour des mentions obligatoires : en France, PMT et PMD portent les mentions que la loi exige sur les retards de paiement, et AAB celle sur l'escompte pour paiement anticipé. La règle vérifie que le code d'une note vient de la liste officielle, et non un mot comme « INFO ».

## Pourquoi c'est important

BR-CL-08 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-08 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le sujet de chaque note dans la liste de votre logiciel, ou ne l'indiquez pas.
2. Vérifiez que la facture électronique écrit un code de la liste, comme AAI.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-08.

## Causes fréquentes

- **Un mot au lieu du code**, comme INFO ou NOTE.
- **Un code en minuscules**, alors que les codes de la liste sont en majuscules.

## Détails techniques

Le code du sujet de la note est BT-21. En CII, c'est le `ram:SubjectCode` de chaque `ram:IncludedNote` de `rsm:ExchangedDocument`. En UBL, une note n'a pas d'élément pour lui : la règle lit un code écrit entre les deux premiers `#` de `cbc:Note`, comme dans `#AAI#Merci`, et laisse passer une note sans ce motif. La liste est une partie de l'UNTDID 4451.

La facture d'exemple ajoute une note avec le code sujet `INFO` ; sa version corrigée indique `AAI`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000553`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Subject Code MUST be coded using a restriction of UNTDID 4451.

BR-CL-08, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-FR-05](../BR-FR-05/) : la facture doit porter trois mentions, chacune dans une note codée : l'indemnité forfaitaire pour frais de recouvrement (PMT), les pénalités de retard (PMD) et l'escompte ou son absence (AAB).
