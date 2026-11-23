# Un attribut d'article n'a pas de nom ou de valeur

Un attribut d'article indique son nom sans sa valeur, ou sa valeur sans son nom.

## Ce que vérifie la règle

Une ligne peut décrire son article par des attributs, chacun un nom et une valeur : « Couleur : bleu », « Taille : M ». La règle vérifie que chaque attribut a les deux.

## Pourquoi c'est important

BR-54 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-54 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez le nom et la valeur de chaque attribut d'article dans votre logiciel.
2. Supprimez les attributs restés vides.
3. Si la facture électronique en manque encore un, signalez-le à l'éditeur de votre logiciel en citant BR-54.

## Causes fréquentes

- **Un champ d'attribut resté vide** dans la fiche de l'article.
- **Un attribut écrit comme un seul texte**, « bleu », sans son nom.

## Détails techniques

Un attribut d'article est le groupe BG-32, avec son nom BT-160 et sa valeur BT-161. En CII, la règle lit `ram:Description` et `ram:Value` de chaque `ram:ApplicableProductCharacteristic` du `ram:SpecifiedTradeProduct` d'une ligne ; en UBL, `cbc:Name` et `cbc:Value` de chaque `cac:AdditionalItemProperty`.

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige à la fois le nom et la valeur de chaque attribut d'article, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) le laisse en revanche facultatif : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> Each Item attribute (BG-32) shall contain an Item attribute name (BT-160) and an Item attribute value (BT-161).

BR-54, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-FR-27](../BR-FR-27/) : chaque caractéristique d'article doit avoir un nom ou un code, et aucun des deux ne doit être vide.
- [BR-25](../BR-25/) : chaque ligne de facture doit nommer ce qu'elle facture.
