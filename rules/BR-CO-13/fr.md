# Le total HT n'est pas égal aux lignes, moins les remises, plus les frais

Le total HT de la facture n'est pas égal au total des lignes, moins les remises globales, plus les frais globaux.

## Ce que vérifie la règle

Le total HT se calcule à partir de trois montants : le total des lignes HT, le total des remises accordées sur l'ensemble de la facture et le total des frais ajoutés à l'ensemble de la facture. La règle vérifie que le total HT est exactement le total des lignes, moins les remises, plus les frais, au centime près.

## Pourquoi c'est important

BR-CO-13 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-13 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Calculez le total HT à partir des totaux déjà arrondis : total des lignes, moins total des remises, plus total des frais.
2. Vérifiez qu'aucune remise ni aucun frais n'a été ajouté après le calcul du total HT.
3. Si votre logiciel calcule le total HT autrement, signalez-le à son éditeur en citant BR-CO-13.

## Causes fréquentes

- **Une remise ou des frais oubliés** dans le calcul du total HT, ou comptés deux fois.
- **Un acompte retiré du total HT**, alors qu'un montant déjà payé se retire du net à payer.
- **Un écart d'arrondi :** le total HT est calculé sur des montants non arrondis.

## Détails techniques

Le total HT est BT-109, le total des lignes BT-106, le total des remises BT-107 et le total des frais BT-108 ; quand ces deux derniers sont absents, la règle ne les compte pas. Le message officiel parle de la somme des lignes (BT-131), mais le test utilise le total des lignes (BT-106), que [BR-CO-10](../BR-CO-10/) relie à cette somme. En CII : `ram:TaxBasisTotalAmount`, `ram:LineTotalAmount`, `ram:AllowanceTotalAmount` et `ram:ChargeTotalAmount` de `ram:SpecifiedTradeSettlementHeaderMonetarySummation` ; en UBL : `cbc:TaxExclusiveAmount`, `cbc:LineExtensionAmount`, `cbc:AllowanceTotalAmount` et `cbc:ChargeTotalAmount` de `cac:LegalMonetaryTotal`.

## Texte officiel

> Invoice total amount without VAT (BT-109) = Σ Invoice line net amount (BT-131) - Sum of allowances on document level (BT-107) + Sum of charges on document level (BT-108).

BR-CO-13, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-10](../BR-CO-10/) : le total des lignes doit être la somme des montants HT de chaque ligne.
- [BR-CO-11](../BR-CO-11/) : le total des remises doit être la somme des remises globales.
- [BR-CO-12](../BR-CO-12/) : le total des frais doit être la somme des frais globaux.
- [BR-CO-15](../BR-CO-15/) : le total TTC doit être le total HT plus la TVA.
