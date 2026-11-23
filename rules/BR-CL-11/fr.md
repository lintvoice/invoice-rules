# Le type d'un numéro d'immatriculation n'est pas un code valide

Le code qui dit de quel registre vient un numéro d'immatriculation légale n'est pas dans la liste officielle.

## Ce que vérifie la règle

Les identifiants viennent de nombreux registres : un GLN, un SIRET, un numéro DUNS… Un code à quatre chiffres de la liste ISO 6523 dit de quel registre vient un identifiant : 0088 pour un GLN, 0009 pour un SIRET, 0002 pour un SIREN. La règle vérifie que le numéro d'immatriculation légale du vendeur, de l'acheteur ou du bénéficiaire, quand il indique son registre, utilise un tel code, et non le nom du registre.

## Pourquoi c'est important

BR-CL-11 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-11 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le registre dans la liste de votre logiciel, ou n'indiquez pas de code s'il n'y en a pas pour votre registre.
2. Vérifiez que la facture électronique écrit le code à quatre chiffres, ou aucun code.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-11.

## Causes fréquentes

- **Le nom du registre au lieu de son code**, comme SIREN ou HRB.
- **Un registre national sans code ISO 6523**, auquel on en invente un.

## Détails techniques

La règle lit le schéma des identifiants d'immatriculation légale : celui du vendeur (BT-30-1), de l'acheteur (BT-47-1) et du bénéficiaire (BT-61-1). En CII, c'est le `schemeID` de chaque `ram:ID` hors d'un `ram:SpecifiedTaxRegistration`, comme le `ram:ID` de `ram:SpecifiedLegalOrganization` ; en UBL, le `schemeID` de `cbc:CompanyID` dans chaque `cac:PartyLegalEntity`. La liste est la liste ISO 6523 ICD. Le schéma est facultatif : un numéro sans schéma passe.

La facture d'exemple écrit le schéma du SIREN du vendeur `SIREN` au lieu de `0002`. Les règles françaises BR-FR-10 et BR-FR-09 ne lisent le SIREN que sous le code 0002 : elles ne le trouvent plus, et échouent aussi. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000581`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Any registration identifier identification scheme identifier MUST be coded using one of the ISO 6523 ICD list.

BR-CL-11, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-10](../BR-CL-10/) : le code qui dit de quel registre vient l'identifiant d'une partie doit être dans la liste ISO 6523, comme 0088 pour un GLN.
- [BR-FR-10](../BR-FR-10/) : la facture doit porter le SIREN du vendeur : 9 chiffres, sans espace.
- [BR-FR-09](../BR-FR-09/) : quand une partie de la facture a un SIRET, il doit compter 14 chiffres et commencer par son SIREN.
