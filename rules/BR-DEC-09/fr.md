# Le total des lignes HT a plus de 2 décimales

Le total des lignes HT est écrit avec plus de 2 décimales.

## Ce que vérifie la règle

Le total des lignes HT est la somme des montants nets des lignes de la facture, avant les remises et frais globaux. La règle vérifie que le total des lignes HT est écrit avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-09 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-09 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Calculez le total des lignes à partir des montants des lignes arrondis au centime.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop.
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-09.

## Causes fréquentes

- **Un total calculé à partir de montants non arrondis**, sans arrondi final.
- **Un export qui écrit chaque montant avec 3 décimales**, même arrondi.

## Détails techniques

Le total des lignes HT est BT-106, dans le groupe BG-22. En CII, la règle lit `ram:LineTotalAmount` de `ram:SpecifiedTradeSettlementHeaderMonetarySummation` ; en UBL, `cbc:LineExtensionAmount` de `cac:LegalMonetaryTotal`. Elle compte les décimales telles qu'elles sont écrites après le point.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the Sum of Invoice line net amount (BT-106) is 2.

BR-DEC-09, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-23](../BR-DEC-23/) : le montant net d'une ligne, 2 décimales au plus.
- [BR-CO-10](../BR-CO-10/) : le total des lignes HT doit être la somme des lignes.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
