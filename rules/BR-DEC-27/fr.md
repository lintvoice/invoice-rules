# Le montant de frais sur ligne a plus de 2 décimales

Le montant de frais sur ligne est écrit avec plus de 2 décimales.

## Ce que vérifie la règle

Des frais sur ligne sont un montant ajouté à une seule ligne de la facture, par exemple un emballage. La règle vérifie que le montant de chacun des frais sur ligne est écrit avec au plus 2 décimales. Par exemple, `1230.50` passe et `1230.505` échoue. Les zéros à la fin comptent aussi, donc `1230.500` échoue, bien que ce soit le même montant.

## Pourquoi c'est important

BR-DEC-27 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-27 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Si les frais sur ligne sont un pourcentage, arrondissez leur montant au centime.
2. Vérifiez que la facture électronique écrit ce montant avec au plus 2 décimales, sans zéros en trop.
3. Si votre logiciel écrit plus de décimales, signalez-le à son éditeur en citant BR-DEC-27.

## Causes fréquentes

- **Des frais en pourcentage non arrondis** (1,5 % de 1 234,50 font 18,5175).
- **Un export qui écrit chaque montant avec 3 décimales**, même arrondi.

## Détails techniques

Le montant de frais sur ligne est BT-141, dans le groupe BG-28. En CII, la règle lit `ram:ActualAmount` de chaque `ram:SpecifiedTradeAllowanceCharge` du `ram:SpecifiedLineTradeSettlement` d'une ligne dont `ram:ChargeIndicator` vaut `true` ; en UBL, `cbc:Amount` de chaque `cac:AllowanceCharge` d'une `cac:InvoiceLine` (ou `cac:CreditNoteLine`) dont `cbc:ChargeIndicator` vaut `true`. Elle compte les décimales telles qu'elles sont écrites après le point.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> The allowed maximum number of decimals for the Invoice line charge amount (BT-141) is 2.

BR-DEC-27, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-28](../BR-DEC-28/) : l'assiette de frais sur ligne, 2 décimales au plus.
- [BR-CO-24](../BR-CO-24/) : les frais sur ligne doivent avoir un motif, en texte ou en code.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
