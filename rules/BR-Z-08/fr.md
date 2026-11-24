# La base du taux zéro ne correspond pas aux lignes

La base de la ventilation de la catégorie Z (taux zéro) ne correspond pas à ses lignes, remises et frais.

## Ce que vérifie la règle

La catégorie Z couvre les opérations taxées au taux de 0 %, comme les panneaux solaires vendus à leur exploitant en Allemagne. Sa TVA vaut 0, mais sa ventilation indique quand même le montant auquel elle s'applique. La règle vérifie que cette base est la somme des lignes en Z, plus les frais et moins les remises en Z.

## Pourquoi c'est important

BR-Z-08 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-Z-08 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Additionnez les montants nets des lignes en Z, ajoutez les frais et retranchez les remises en Z : c'est la base attendue.
2. Rattachez chaque remise et chaque frais à la catégorie de ce à quoi ils s'appliquent.
3. Si votre logiciel la calcule autrement, signalez-le à l'éditeur de votre logiciel en citant BR-Z-08.

## Causes fréquentes

- **Une remise sur l'ensemble de la facture** déduite du total mais pas de la base de sa catégorie.
- **Une base saisie à la main**, ou non recalculée après la modification d'une ligne.

## Détails techniques

La base d'une catégorie est BT-116 ; les montants nets des lignes sont BT-131, les remises au niveau du document BT-92 et les frais BT-99. En CII : `ram:BasisAmount` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` dont le `ram:CategoryCode` vaut `Z` ; en UBL : `cbc:TaxableAmount` de chaque `cac:TaxSubtotal` de catégorie `Z`.

En CII, la règle accepte un écart strictement inférieur à 1 (une unité de la devise) ; en UBL, elle exige une égalité exacte.

La facture d'exemple est entièrement en catégorie Z, et indique une base supérieure de 1 € à la somme de ses lignes ; sa version corrigée indique la somme.

La facture d'exemple est allemande : la France n'a pas de taux zéro pour ses opérations intérieures.

## Texte officiel

> In a VAT breakdown (BG-23) where VAT category code (BT-118) is "Zero rated" the VAT category taxable amount (BT-116) shall equal the sum of Invoice line net amount (BT-131) minus the sum of Document level allowance amounts (BT-92) plus the sum of Document level charge amounts (BT-99) where the VAT category codes (BT-151, BT-95, BT-102) are "Zero rated".

BR-Z-08, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-Z-09](../BR-Z-09/) : dans la catégorie de TVA Z (taux zéro), la facture ne facture pas de TVA : le montant de TVA de sa ventilation vaut 0.
- [BR-Z-01](../BR-Z-01/) : une facture qui a une ligne, une remise ou des frais de la catégorie de TVA Z (taux zéro) doit avoir une ventilation de TVA pour cette catégorie, et une seule.
- [BR-S-08](../BR-S-08/) : pour chaque taux, la base HT doit être la somme des lignes à ce taux, plus les frais et moins les remises au même taux.
