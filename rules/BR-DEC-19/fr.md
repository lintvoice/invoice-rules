# La base HT d'un taux a plus de 2 décimales

La base HT d'un taux est écrite avec plus de 2 décimales.

## Ce que vérifie la règle

Dans la ventilation de TVA, chaque taux a sa base HT, le total hors taxe de ce qui est facturé à ce taux. La règle vérifie que la base HT de chaque taux est écrite avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-19 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-19 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Calculez la base HT de chaque taux à partir des lignes, remises et frais à ce taux, arrondis au centime.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop (`1230.50`, pas `1230.500`).
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-19.

## Causes fréquentes

- **Une base HT calculée à partir de montants de lignes non arrondis.**
- **Un export qui écrit les montants avec 3 décimales ou plus** (`1230.500`), même arrondis.

## Détails techniques

La base HT d'un taux est BT-116, dans le groupe BG-23. En CII, la règle lit `ram:BasisAmount` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, `cbc:TaxableAmount` de chaque `cac:TaxSubtotal`. Elle compte les décimales écrites après le point, donc un zéro final compte aussi, et `10.250` échoue bien qu'il vaille `10.25`.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the VAT category taxable amount (BT-116) is 2.

BR-DEC-19, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-20](../BR-DEC-20/) : le montant de TVA d'un taux, 2 décimales au plus.
- [BR-S-08](../BR-S-08/) : la base HT d'un taux doit être la somme de ses lignes, frais et remises.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
