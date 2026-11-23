# Le type d'un identifiant d'entreprise n'est pas un code valide

Le code qui dit de quel registre vient un identifiant n'est pas dans la liste officielle.

## Ce que vérifie la règle

Les identifiants viennent de nombreux registres : un GLN, un SIRET, un numéro DUNS… Un code à quatre chiffres de la liste ISO 6523 dit de quel registre vient un identifiant : 0088 pour un GLN, 0009 pour un SIRET, 0002 pour un SIREN. La règle vérifie que l'identifiant du vendeur, de l'acheteur ou du bénéficiaire utilise un tel code, et non le nom du registre.

## Pourquoi c'est important

BR-CL-10 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-10 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le type d'identifiant dans la liste de votre logiciel, plutôt que de le saisir.
2. Vérifiez que la facture électronique écrit le code à quatre chiffres à côté de l'identifiant.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-10.

## Causes fréquentes

- **Le nom du registre au lieu de son code**, comme GLN, SIRET ou EAN.
- **Un code sans ses zéros de tête**, 88 pour 0088.

## Détails techniques

La règle lit le schéma de l'identifiant du vendeur (BT-29-1), de l'acheteur (BT-46-1) et du bénéficiaire (BT-60-1). En CII, c'est le `schemeID` de chaque `ram:GlobalID`, sauf ceux d'un article et du lieu de livraison, que contrôlent BR-CL-21 et BR-CL-26 ; en UBL, le `schemeID` de `cbc:ID` dans chaque `cac:PartyIdentification`. La liste est la liste ISO 6523 ICD.

La facture d'exemple écrit le schéma du SIRET du vendeur `SIRET` au lieu de `0009`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000579`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Any identifier identification scheme identifier MUST be coded using one of the ISO 6523 ICD list.

BR-CL-10, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-11](../BR-CL-11/) : quand le numéro d'immatriculation légale d'une partie indique le registre dont il vient, ce code doit être dans la liste ISO 6523, comme 0002 pour un SIREN.
- [BR-CL-21](../BR-CL-21/) : le code qui dit de quel type est l'identifiant standard d'un article doit être dans la liste ISO 6523, comme 0160 pour un GTIN.
- [BR-CL-26](../BR-CL-26/) : le code qui dit de quel type est l'identifiant du lieu de livraison doit être dans la liste ISO 6523, comme 0088 pour un GLN.
- [BR-FR-CO-10](../BR-FR-CO-10/) : chaque identifiant d'une partie doit dire de quel type il est (SIRET, GLN…), et une partie ne peut pas avoir deux identifiants du même type.
