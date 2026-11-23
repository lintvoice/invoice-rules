# Le total HT a plus de 2 décimales

Le total HT est écrit avec plus de 2 décimales.

## Ce que vérifie la règle

Le total HT est le total des lignes, moins les remises et plus les frais globaux. La règle vérifie que le total HT est écrit avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-12 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-12 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Calculez le total HT à partir de montants arrondis au centime : les lignes, les remises et les frais.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop.
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-12.

## Causes fréquentes

- **Un total calculé à partir de montants non arrondis**, sans arrondi final.
- **Un export qui écrit chaque montant avec 3 décimales**, même arrondi.

## Détails techniques

Le total HT est BT-109, dans le groupe BG-22. En CII, la règle lit `ram:TaxBasisTotalAmount` de `ram:SpecifiedTradeSettlementHeaderMonetarySummation` ; en UBL, `cbc:TaxExclusiveAmount` de `cac:LegalMonetaryTotal`. Elle compte les décimales telles qu'elles sont écrites après le point.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the Invoice total amount without VAT (BT-109) is 2.

BR-DEC-12, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-09](../BR-DEC-09/) : le total des lignes HT, 2 décimales au plus.
- [BR-CO-13](../BR-CO-13/) : le total HT doit être les lignes, moins les remises, plus les frais.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
