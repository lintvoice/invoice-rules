# L'assiette d'une remise sur ligne a plus de 2 décimales

L'assiette d'une remise sur ligne est écrite avec plus de 2 décimales.

## Ce que vérifie la règle

Quand une remise sur ligne est un pourcentage, la facture peut indiquer le montant sur lequel elle se calcule, son assiette. La règle vérifie que l'assiette de chaque remise sur ligne est écrite avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-25 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-25 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Arrondissez l'assiette de la remise sur ligne au centime.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop (`1230.50`, pas `1230.500`).
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-25.

## Causes fréquentes

- **Une assiette reprise d'un total non arrondi.**
- **Un export qui écrit les montants avec 3 décimales ou plus** (`1230.500`), même arrondis.

## Détails techniques

L'assiette d'une remise sur ligne est BT-137, dans le groupe BG-27. En CII, la règle lit `ram:BasisAmount` de chaque `ram:SpecifiedTradeAllowanceCharge` du `ram:SpecifiedLineTradeSettlement` d'une ligne dont `ram:ChargeIndicator` vaut `false` ; en UBL, `cbc:BaseAmount` de chaque `cac:AllowanceCharge` d'une `cac:InvoiceLine` (ou `cac:CreditNoteLine`) dont `cbc:ChargeIndicator` vaut `false`. Elle compte les décimales écrites après le point, donc un zéro final compte aussi, et `10.250` échoue bien qu'il vaille `10.25`.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the Invoice line allowance base amount (BT-137) is 2.

BR-DEC-25, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-24](../BR-DEC-24/) : le montant d'une remise sur ligne, 2 décimales au plus.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
