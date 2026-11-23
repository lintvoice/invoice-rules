# L'adresse électronique du vendeur ne dit pas de quel type d'adresse il s'agit

L'adresse électronique du vendeur est indiquée sans le code qui dit de quel type d'adresse il s'agit.

## Ce que vérifie la règle

Une facture électronique peut indiquer l'adresse électronique où le vendeur reçoit ses factures : une adresse e-mail, un identifiant de routage sur un réseau comme Peppol, une adresse sur une plateforme nationale… Un code dit de quel type d'adresse il s'agit, pour que le logiciel qui envoie sache où livrer. La règle vérifie que l'adresse du vendeur donne ce code.

## Pourquoi c'est important

BR-62 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-62 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le type d'adresse dans votre logiciel, s'il le demande.
2. Vérifiez que la facture électronique en écrit le code à côté de la valeur.
3. Si le code manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-62.

## Causes fréquentes

- **L'adresse électronique du vendeur recopiée comme une simple valeur**, sans son code.
- **Un export qui écrit la valeur et laisse tomber ses attributs.**

## Détails techniques

L'adresse électronique du vendeur est BT-34, son identifiant de schéma BT-34-1. En CII, la règle lit le `schemeID` de `ram:URIID` dans le `ram:URIUniversalCommunication` du vendeur ; en UBL, le `schemeID` du `cbc:EndpointID` du vendeur. Ses codes viennent de la liste EAS, comme l'exige la règle BR-CL-25 : `EM` pour une adresse e-mail, `0088` pour un GLN, `0225` pour une adresse des plateformes de la réforme française…

La facture d'exemple indique l'adresse électronique du vendeur sans son schéma. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence du schéma : dans une facture Factur-X, sa règle `FX-SCH-A-000446` échoue donc à côté de BR-62, comme dans la facture d'exemple.

## Texte officiel

> The Seller electronic address (BT-34) shall have a Scheme identifier.

BR-62, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-63](../BR-63/) : l'adresse électronique de l'acheteur doit dire, avec un code normalisé, de quel type d'adresse il s'agit.
- [BR-CL-25](../BR-CL-25/) : le code qui dit de quel type est l'adresse électronique d'une partie doit être dans la liste EAS, comme EM pour une adresse e-mail.
- [BR-FR-21](../BR-FR-21/) : sur une facture entre entreprises, l'adresse électronique de l'acheteur doit commencer par son SIREN et être déclarée comme adresse de la réforme française.
