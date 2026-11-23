# Le total TTC a plus de 2 décimales

Le total TTC est écrit avec plus de 2 décimales.

## Ce que vérifie la règle

Le total TTC est le total HT plus le total de TVA. La règle vérifie que le total TTC est écrit avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-14 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-14 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Calculez le total TTC à partir du total HT et du total de TVA, arrondis au centime.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop (`1230.50`, pas `1230.500`).
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-14.

## Causes fréquentes

- **Un total calculé à partir de montants non arrondis**, sans arrondi final.
- **Un export qui écrit les montants avec 3 décimales ou plus** (`1230.500`), même arrondis.

## Détails techniques

Le total TTC est BT-112, dans le groupe BG-22. En CII, la règle lit `ram:GrandTotalAmount` de `ram:SpecifiedTradeSettlementHeaderMonetarySummation` ; en UBL, `cbc:TaxInclusiveAmount` de `cac:LegalMonetaryTotal`. Elle compte les décimales écrites après le point, donc un zéro final compte aussi, et `10.250` échoue bien qu'il vaille `10.25`.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant. La facture d'exemple française écrit aussi le net à payer avec 3 décimales, donc elle échoue à BR-FR-DEC-01, BR-DEC-14 et BR-DEC-18.

## Texte officiel

> The allowed maximum number of decimals for the Invoice total amount with VAT (BT-112) is 2.

BR-DEC-14, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-12](../BR-DEC-12/) : le total HT, 2 décimales au plus.
- [BR-DEC-13](../BR-DEC-13/) : le total de TVA, 2 décimales au plus.
- [BR-CO-15](../BR-CO-15/) : le total TTC doit être le total HT plus le total de TVA.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
