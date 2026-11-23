# L'adresse électronique de l'acheteur ne dit pas de quel type d'adresse il s'agit

L'adresse électronique de l'acheteur est indiquée sans le code qui dit de quel type d'adresse il s'agit.

## Ce que vérifie la règle

Une facture électronique peut indiquer l'adresse électronique où l'acheteur reçoit ses factures : une adresse e-mail, un identifiant de routage sur un réseau comme Peppol, une adresse sur une plateforme nationale… Un code dit de quel type d'adresse il s'agit, pour que le logiciel qui envoie sache où livrer. La règle vérifie que l'adresse de l'acheteur donne ce code.

## Pourquoi c'est important

BR-63 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-63 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le type d'adresse dans votre logiciel, s'il le demande.
2. Vérifiez que la facture électronique en écrit le code à côté de la valeur.
3. Si le code manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-63.

## Causes fréquentes

- **L'adresse électronique de l'acheteur recopiée comme une simple valeur**, sans son code.
- **Un export qui écrit la valeur et laisse tomber ses attributs.**

## Détails techniques

L'adresse électronique de l'acheteur est BT-49, son identifiant de schéma BT-49-1. En CII, la règle lit le `schemeID` de `ram:URIID` dans le `ram:URIUniversalCommunication` de l'acheteur ; en UBL, le `schemeID` du `cbc:EndpointID` de l'acheteur. Ses codes viennent de la liste EAS, comme l'exige la règle BR-CL-25 pour celle du vendeur.

La facture d'exemple indique l'adresse électronique de l'acheteur sans son schéma. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence du schéma : dans une facture Factur-X, sa règle `FX-SCH-A-000428` échoue donc à côté de BR-63, comme dans la facture d'exemple.

## Texte officiel

> The Buyer electronic address (BT-49) shall have a Scheme identifier.

BR-63, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-62](../BR-62/) : l'adresse électronique du vendeur doit dire, avec un code normalisé, de quel type d'adresse il s'agit.
- [BR-CL-25](../BR-CL-25/) : le code qui dit de quel type est l'adresse électronique d'une partie doit être dans la liste EAS, comme EM pour une adresse e-mail.
- [BR-FR-22](../BR-FR-22/) : sur une autofacture entre entreprises, l'adresse électronique du vendeur doit commencer par son SIREN et être déclarée comme adresse de la réforme française.
