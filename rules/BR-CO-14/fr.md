# Le total de TVA n'est pas la somme de la TVA de chaque taux

Le total de TVA de la facture n'est pas égal à la somme des montants de TVA calculés pour chaque taux.

## Ce que vérifie la règle

La facture détaille la TVA par taux, par exemple 20 % et 5,5 % : pour chacun, la base HT et le montant de TVA. C'est la ventilation de TVA. La règle vérifie que le total de TVA de la facture est exactement la somme de ces montants, au centime près.

## Pourquoi c'est important

BR-CO-14 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-14 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Calculez le montant de TVA de chaque taux, arrondi au centime.
2. Additionnez ces montants pour obtenir le total de TVA, plutôt que de calculer la TVA sur le total HT.
3. Si votre logiciel calcule le total de TVA autrement, signalez-le à son éditeur en citant BR-CO-14.

## Causes fréquentes

- **La TVA calculée sur le total HT** au lieu d'être additionnée taux par taux : les arrondis peuvent différer d'un centime.
- **La TVA calculée ligne par ligne** puis additionnée, alors que la ventilation la calcule par taux.
- **Un total de TVA dans une autre devise** (voir les détails techniques).

## Détails techniques

Le total de TVA est BT-110, le montant de TVA de chaque catégorie BT-117 (groupe BG-23). En CII, la règle compare le `ram:TaxTotalAmount` dont `currencyID` est la devise de la facture à la somme des `ram:CalculatedAmount` des `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` ; un second `ram:TaxTotalAmount`, dans la devise de comptabilisation de la TVA (BT-111), n'entre pas dans cette comparaison. En UBL, elle compare `cac:TaxTotal/cbc:TaxAmount` à la somme des `cac:TaxSubtotal/cbc:TaxAmount` du même `cac:TaxTotal`.

## Texte officiel

> Invoice total VAT amount (BT-110) = Σ VAT category tax amount (BT-117).

BR-CO-14, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-15](../BR-CO-15/) : le total TTC doit être le total HT plus la TVA.
- [BR-CO-17](../BR-CO-17/) : la TVA de chaque taux doit être sa base multipliée par le taux.
