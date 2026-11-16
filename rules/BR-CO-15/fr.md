# Le total TTC n'est pas égal au total HT plus la TVA

Le total TTC de la facture n'est pas égal au total HT plus le total de TVA.

## Ce que vérifie la règle

La règle compare trois montants de la facture : le total HT, le total de TVA et le total TTC. Le total TTC doit être exactement la somme des deux autres, au centime près.

## Pourquoi c'est important

BR-CO-15 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme : une facture qui échoue à BR-CO-15 échoue donc aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Arrondissez le total HT et le total de TVA au centime.
2. Calculez le total TTC en additionnant ces deux montants arrondis, plutôt que de le calculer à part.
3. Si votre logiciel de facturation calcule le total TTC autrement, signalez-le à son éditeur en citant BR-CO-15.

## Causes fréquentes

- **La TVA n'est pas ajoutée :** le total TTC reprend le total HT.
- **Un écart d'arrondi d'un centime :** le total TTC est calculé sur des montants non arrondis.
- **Un total modifié à la main**, sans mettre à jour les autres.
- **Une facture en devise étrangère :** le logiciel additionne la TVA convertie en euros au lieu de la TVA dans la devise de la facture.

## Détails techniques

Les trois montants sont le total HT (BT-109), le total de TVA (BT-110) et le total TTC (BT-112). Quand la facture indique une devise de comptabilisation de la TVA (BT-6), BT-110 est le total de TVA dans la devise de la facture, pas celui exprimé dans BT-6.

En CII, la règle compare `ram:GrandTotalAmount` à `ram:TaxBasisTotalAmount` plus `ram:TaxTotalAmount` (celui dans la devise de la facture) ; en UBL, `cbc:TaxInclusiveAmount` à `cbc:TaxExclusiveAmount` plus `cac:TaxTotal/cbc:TaxAmount`.

## Texte officiel

> Invoice total amount with VAT (BT-112) = Invoice total amount without VAT (BT-109) + Invoice total VAT amount (BT-110).

BR-CO-15, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-13](../BR-CO-13/) : le total HT doit être la somme des lignes, moins les remises et plus les frais au niveau de la facture.
- [BR-CO-14](../BR-CO-14/) : le total de TVA doit être la somme de la TVA de chaque taux.
- [BR-CO-16](../BR-CO-16/) : le montant à payer doit être le total TTC, moins ce qui est déjà payé, plus l'arrondi.
