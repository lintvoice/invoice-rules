# Le montant de TVA d'un taux a plus de 2 décimales

Le montant de TVA d'un taux est écrit avec plus de 2 décimales.

## Ce que vérifie la règle

Dans la ventilation de TVA, chaque taux a son montant de TVA, la base HT multipliée par le taux. La règle vérifie que le montant de TVA de chaque taux est écrit avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-20 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-20 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Arrondissez le montant de TVA de chaque taux au centime.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop.
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-20.

## Causes fréquentes

- **Un montant de TVA calculé comme la base HT multipliée par le taux**, sans arrondi.
- **Un export qui écrit chaque montant avec 3 décimales**, même arrondi.

## Détails techniques

Le montant de TVA d'un taux est BT-117, dans le groupe BG-23. En CII, la règle lit `ram:CalculatedAmount` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, `cbc:TaxAmount` de chaque `cac:TaxSubtotal`. Elle compte les décimales telles qu'elles sont écrites après le point.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the VAT category tax amount (BT-117) is 2.

BR-DEC-20, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-19](../BR-DEC-19/) : la base HT d'un taux, 2 décimales au plus.
- [BR-CO-17](../BR-CO-17/) : la TVA de chaque taux doit être sa base multipliée par le taux.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
