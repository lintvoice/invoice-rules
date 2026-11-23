# Le net à payer a plus de 2 décimales

Le net à payer est écrit avec plus de 2 décimales.

## Ce que vérifie la règle

Le net à payer est ce que l'acheteur doit encore payer, soit le total TTC moins le montant déjà payé, plus l'éventuel arrondi. La règle vérifie que le net à payer est écrit avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-18 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-18 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Calculez le net à payer à partir de montants arrondis au centime : le total TTC, le montant déjà payé et l'arrondi.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop (`1230.50`, pas `1230.500`).
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-18.

## Causes fréquentes

- **Un total calculé à partir de montants non arrondis**, sans arrondi final.
- **Un export qui écrit les montants avec 3 décimales ou plus** (`1230.500`), même arrondis.

## Détails techniques

Le net à payer est BT-115, dans le groupe BG-22. En CII, la règle lit `ram:DuePayableAmount` de `ram:SpecifiedTradeSettlementHeaderMonetarySummation` ; en UBL, `cbc:PayableAmount` de `cac:LegalMonetaryTotal`. Elle compte les décimales écrites après le point, donc un zéro final compte aussi, et `10.250` échoue bien qu'il vaille `10.25`.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant. La facture d'exemple française écrit aussi le total TTC avec 3 décimales, donc elle échoue à BR-FR-DEC-01, BR-DEC-14 et BR-DEC-18.

## Texte officiel

> The allowed maximum number of decimals for the Amount due for payment (BT-115) is 2.

BR-DEC-18, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-14](../BR-DEC-14/) : le total TTC, 2 décimales au plus.
- [BR-CO-16](../BR-CO-16/) : le net à payer doit être le total TTC, moins le montant déjà payé, plus l'arrondi.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
