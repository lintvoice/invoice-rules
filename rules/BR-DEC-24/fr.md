# Le montant d'une remise sur ligne a plus de 2 décimales

Le montant d'une remise sur ligne est écrit avec plus de 2 décimales.

## Ce que vérifie la règle

Une remise sur ligne est une remise accordée sur une seule ligne de la facture. La règle vérifie que le montant de chaque remise sur ligne est écrit avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-24 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-24 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Si la remise sur ligne est un pourcentage, arrondissez son montant au centime.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop.
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-24.

## Causes fréquentes

- **Une remise en pourcentage non arrondie** (1,5 % de 1 234,50 font 18,5175).
- **Un export qui écrit chaque montant avec 3 décimales**, même arrondi.

## Détails techniques

Le montant d'une remise sur ligne est BT-136, dans le groupe BG-27. En CII, la règle lit `ram:ActualAmount` de chaque `ram:SpecifiedTradeAllowanceCharge` du `ram:SpecifiedLineTradeSettlement` d'une ligne dont `ram:ChargeIndicator` vaut `false` ; en UBL, `cbc:Amount` de chaque `cac:AllowanceCharge` d'une `cac:InvoiceLine` (ou `cac:CreditNoteLine`) dont `cbc:ChargeIndicator` vaut `false`. Elle compte les décimales telles qu'elles sont écrites après le point.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the Invoice line allowance amount (BT-136) is 2.

BR-DEC-24, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-25](../BR-DEC-25/) : l'assiette d'une remise sur ligne, 2 décimales au plus.
- [BR-CO-23](../BR-CO-23/) : chaque remise sur ligne doit avoir un motif, en texte ou en code.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
