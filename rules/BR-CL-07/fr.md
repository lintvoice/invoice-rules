# Le type d'objet facturé n'est pas un code valide

Le code qui dit de quel type d'identifiant est l'objet facturé n'est pas dans la liste officielle.

## Ce que vérifie la règle

Une facture peut identifier l'objet qu'elle facture : un contrat, un compteur, un abonnement… Un code dit de quel type d'identifiant il s'agit, AVV pour un numéro d'accord-cadre par exemple. La règle vérifie que ce code vient de la liste officielle, et non un mot comme « ORDER ».

## Pourquoi c'est important

BR-CL-07 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-07 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le type d'identifiant dans la liste de votre logiciel.
2. Vérifiez que la facture électronique écrit un code de la liste à côté de l'identifiant.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-07.

## Causes fréquentes

- **Un mot au lieu du code**, comme ORDER ou CONTRACT.
- **Un numéro de commande écrit comme objet facturé**, avec un code inventé.

## Détails techniques

L'identifiant de l'objet facturé est BT-18, son identifiant de schéma BT-18-1. En CII, c'est le `ram:ReferenceTypeCode` du `ram:AdditionalReferencedDocument` dont le `ram:TypeCode` vaut 130 ; en UBL, le `schemeID` de `cbc:ID` dans le `cac:AdditionalDocumentReference` dont le `cbc:DocumentTypeCode` vaut 130. La liste est une partie de l'UNTDID 1153.

La facture d'exemple indique un objet facturé avec le code `ORDER` ; sa version corrigée indique `AVV`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000282`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Object identifier identification scheme identifier MUST be coded using a restriction of UNTDID 1153.

BR-CL-07, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-FR-29](../BR-FR-29/) : la facture peut donner au plus une référence d'objet facturé de type AFL et une de type AVV, et aucune ne doit être vide.
- [BR-52](../BR-52/) : chaque justificatif auquel une facture fait référence doit indiquer sa référence.
