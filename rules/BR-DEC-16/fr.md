# Le montant déjà payé a plus de 2 décimales

Le montant déjà payé est écrit avec plus de 2 décimales.

## Ce que vérifie la règle

Le montant déjà payé est ce que l'acheteur a réglé avant cette facture, par exemple un acompte versé à la commande. La règle vérifie que le montant déjà payé est écrit avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-16 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-16 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Saisissez le montant déjà payé tel qu'il a été réglé, au centime.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop (`1230.50`, pas `1230.500`).
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-16.

## Causes fréquentes

- **Un montant déjà payé calculé plutôt que saisi**, par exemple en pourcentage du total, sans arrondi.
- **Un export qui écrit les montants avec 3 décimales ou plus** (`1230.500`), même arrondis.

## Détails techniques

Le montant déjà payé est BT-113, dans le groupe BG-22. En CII, la règle lit `ram:TotalPrepaidAmount` de `ram:SpecifiedTradeSettlementHeaderMonetarySummation` ; en UBL, `cbc:PrepaidAmount` de `cac:LegalMonetaryTotal`. Elle compte les décimales écrites après le point, donc un zéro final compte aussi, et `10.250` échoue bien qu'il vaille `10.25`.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the Paid amount (BT-113) is 2.

BR-DEC-16, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-18](../BR-DEC-18/) : le net à payer, 2 décimales au plus.
- [BR-CO-16](../BR-CO-16/) : le net à payer doit être le total TTC, moins le montant déjà payé, plus l'arrondi.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
