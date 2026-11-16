# Le total des lignes HT n'est pas la somme des lignes

Le total des lignes HT de la facture n'est pas égal à la somme des montants HT de chaque ligne.

## Ce que vérifie la règle

Chaque ligne de la facture a un montant HT : la quantité multipliée par le prix, après les remises et les frais de la ligne. La facture donne aussi le total de ces montants. La règle vérifie que ce total est exactement la somme des lignes, au centime près.

## Pourquoi c'est important

BR-CO-10 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-10 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Additionnez les montants HT de toutes les lignes, chacun arrondi au centime, et reportez le résultat comme total des lignes.
2. Vérifiez qu'aucune ligne n'a été ajoutée, retirée ou modifiée après le calcul des totaux.
3. Si votre logiciel calcule ce total autrement, signalez-le à son éditeur en citant BR-CO-10.

## Causes fréquentes

- **Une ligne modifiée, ajoutée ou retirée après le calcul des totaux.**
- **Des arrondis différents :** le total est calculé sur des montants non arrondis, alors que chaque ligne est arrondie.

## Détails techniques

Le total des lignes est BT-106, le montant net de chaque ligne BT-131. La règle compare BT-106 à la somme des BT-131, arrondie au centime. En CII, elle compare le `ram:LineTotalAmount` de `ram:SpecifiedTradeSettlementHeaderMonetarySummation` à ceux des `ram:SpecifiedTradeSettlementLineMonetarySummation` ; en UBL, `cac:LegalMonetaryTotal/cbc:LineExtensionAmount` au `cbc:LineExtensionAmount` de chaque `cac:InvoiceLine` (ou `cac:CreditNoteLine`).

## Texte officiel

> Sum of Invoice line net amount (BT-106) = Σ Invoice line net amount (BT-131).

BR-CO-10, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-13](../BR-CO-13/) : le total HT doit être le total des lignes, moins les remises, plus les frais.
- [BR-CO-15](../BR-CO-15/) : le total TTC doit être le total HT plus la TVA.
