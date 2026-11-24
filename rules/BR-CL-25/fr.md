# Le type d'une adresse électronique n'est pas un code valide

Le code qui dit de quel type est l'adresse électronique d'une partie n'est pas dans la liste EAS.

## Ce que vérifie la règle

Une facture électronique peut indiquer l'adresse électronique où le vendeur et l'acheteur reçoivent leurs factures. Un code de la liste EAS dit de quel type d'adresse il s'agit : EM pour une adresse e-mail, 0088 pour un GLN, 0225 pour une adresse de facturation de la réforme française… La règle vérifie que ce code vient de cette liste, et non un mot comme « EMAIL ».

## Pourquoi c'est important

BR-CL-25 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-25 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le type d'adresse électronique dans la liste de votre logiciel.
2. Vérifiez que la facture électronique en écrit le code, 0225 pour une adresse de facturation de la réforme française.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-25.

## Causes fréquentes

- **Un mot au lieu du code**, comme SIREN ou EMAIL.
- **Un code d'une autre liste**, un schéma de la liste ISO 6523 qu'EAS n'a pas.

## Détails techniques

Les adresses électroniques du vendeur et de l'acheteur sont BT-34 et BT-49, leurs identifiants de schéma BT-34-1 et BT-49-1. En CII, la règle lit le `schemeID` de chaque `ram:URIID` dans un `ram:URIUniversalCommunication` ; en UBL, le `schemeID` de chaque `cbc:EndpointID`. La liste est la liste CEF EAS, version 17 dans les fichiers 1.3.17. Le réseau Peppol tient une liste plus courte, sans EM.

La facture d'exemple indique l'adresse électronique du vendeur avec le schéma `SIREN` au lieu de `0225`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000582`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Endpoint identifier scheme identifier MUST belong to the CEF EAS code list

BR-CL-25, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-62](../BR-62/) : l'adresse électronique du vendeur doit dire, avec un code normalisé, de quel type d'adresse il s'agit.
- [BR-63](../BR-63/) : l'adresse électronique de l'acheteur doit dire, avec un code normalisé, de quel type d'adresse il s'agit.
- [BR-FR-21](../BR-FR-21/) : sur une facture entre entreprises, l'adresse électronique de l'acheteur doit commencer par son SIREN et être déclarée comme adresse de la réforme française.
