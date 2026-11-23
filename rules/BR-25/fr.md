# Une ligne n'a pas de désignation

La désignation de ce que facture une ligne est vide.

## Ce que vérifie la règle

Chaque ligne d'une facture nomme l'article ou la prestation qu'elle facture : « Atelier de formation », « Support de cours »… La règle vérifie que chaque ligne en donne la désignation.

## Pourquoi c'est important

BR-25 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-25 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Donnez une désignation à chaque article et prestation du catalogue de votre logiciel.
2. Pour une ligne saisie à la main, écrivez ce qu'elle facture.
3. Si la désignation manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-25.

## Causes fréquentes

- **Un article connu seulement par sa référence** dans le catalogue.
- **Une description gardée dans un champ à part** que la facture électronique n'utilise pas comme désignation.

## Détails techniques

La désignation de l'article est BT-153. En CII, c'est le `ram:Name` du `ram:SpecifiedTradeProduct` de la ligne ; en UBL, le `cbc:Name` du `cac:Item` de la ligne.

La facture d'exemple laisse vide la désignation de sa première ligne, donc elle échoue à BR-25 seule.

## Texte officiel

> Each Invoice line (BG-25) shall contain the Item name (BT-153).

BR-25, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-21](../BR-21/) : chaque ligne de facture doit avoir son identifiant, un numéro de ligne par exemple.
- [BR-16](../BR-16/) : toute facture doit contenir au moins une ligne, avoirs compris : pour un montant global, une seule ligne suffit.
