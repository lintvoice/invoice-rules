# L'assiette de frais globaux a plus de 2 décimales

L'assiette de frais globaux est écrite avec plus de 2 décimales.

## Ce que vérifie la règle

Quand des frais globaux sont un pourcentage, la facture peut indiquer le montant sur lequel ils se calculent, leur assiette. La règle vérifie que l'assiette de chacun des frais globaux est écrite avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-06 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-06 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Arrondissez l'assiette des frais au centime.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop.
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-06.

## Causes fréquentes

- **Une assiette reprise d'un total non arrondi.**
- **Un export qui écrit chaque montant avec 3 décimales**, même arrondi.

## Détails techniques

L'assiette de frais globaux est BT-100, dans le groupe BG-21. En CII, la règle lit `ram:BasisAmount` de chaque `ram:SpecifiedTradeAllowanceCharge` de `ram:ApplicableHeaderTradeSettlement` dont `ram:ChargeIndicator` vaut `true` ; en UBL, `cbc:BaseAmount` de chaque `cac:AllowanceCharge` du document dont `cbc:ChargeIndicator` vaut `true`. Elle compte les décimales telles qu'elles sont écrites après le point.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the Document level charge base amount (BT-100) is 2.

BR-DEC-06, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-05](../BR-DEC-05/) : le montant de frais globaux, 2 décimales au plus.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
