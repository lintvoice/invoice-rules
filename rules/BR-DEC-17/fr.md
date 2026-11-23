# L'arrondi a plus de 2 décimales

L'arrondi est écrit avec plus de 2 décimales.

## Ce que vérifie la règle

L'arrondi est le montant ajouté au total, ou retiré, pour arrondir le net à payer. La règle vérifie que l'arrondi est écrit avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-17 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-17 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Saisissez l'arrondi en centimes, par exemple `0.02`.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop (`1230.50`, pas `1230.500`).
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-17.

## Causes fréquentes

- **Un arrondi calculé comme l'écart avec des montants non arrondis.**
- **Un export qui écrit les montants avec 3 décimales ou plus** (`1230.500`), même arrondis.

## Détails techniques

L'arrondi est BT-114, dans le groupe BG-22. En CII, la règle lit `ram:RoundingAmount` de `ram:SpecifiedTradeSettlementHeaderMonetarySummation` ; en UBL, `cbc:PayableRoundingAmount` de `cac:LegalMonetaryTotal`. Elle compte les décimales écrites après le point, donc un zéro final compte aussi, et `10.250` échoue bien qu'il vaille `10.25`.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the Rounding amount (BT-114) is 2.

BR-DEC-17, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-18](../BR-DEC-18/) : le net à payer, 2 décimales au plus.
- [BR-CO-16](../BR-CO-16/) : le net à payer doit être le total TTC, moins le montant déjà payé, plus l'arrondi.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
