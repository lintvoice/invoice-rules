# Le montant net d'une ligne a plus de 2 décimales

Le montant net d'une ligne est écrit avec plus de 2 décimales.

## Ce que vérifie la règle

Chaque ligne de la facture a un montant net, la quantité multipliée par le prix, moins les remises de la ligne et plus ses frais. La règle vérifie que le montant net de chaque ligne est écrit avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-23 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-23 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Arrondissez le montant net de chaque ligne au centime, après avoir multiplié la quantité par le prix.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop (`1230.50`, pas `1230.500`).
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-23.

## Causes fréquentes

- **Une quantité multipliée par un prix sans arrondi** (2,5 heures à 33,33 font 83,325).
- **Un export qui écrit les montants avec 3 décimales ou plus** (`1230.500`), même arrondis.

## Détails techniques

Le montant net d'une ligne est BT-131, dans le groupe BG-25. En CII, la règle lit `ram:LineTotalAmount` du `ram:SpecifiedTradeSettlementLineMonetarySummation` de chaque ligne ; en UBL, `cbc:LineExtensionAmount` de chaque `cac:InvoiceLine` (ou `cac:CreditNoteLine`). Elle compte les décimales écrites après le point, donc un zéro final compte aussi, et `10.250` échoue bien qu'il vaille `10.25`.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the Invoice line net amount (BT-131) is 2.

BR-DEC-23, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-09](../BR-DEC-09/) : le total des lignes HT, 2 décimales au plus.
- [BR-CO-10](../BR-CO-10/) : le total des lignes HT doit être la somme des lignes.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
