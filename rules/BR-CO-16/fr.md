# Le net à payer n'est pas le total TTC, moins ce qui est payé, plus l'arrondi

Le net à payer de la facture n'est pas égal au total TTC, moins le montant déjà payé, plus l'arrondi.

## Ce que vérifie la règle

Le net à payer est ce que l'acheteur doit encore régler. Il part du total TTC, retire ce qui a déjà été payé, un acompte par exemple, et ajoute un éventuel arrondi. La règle vérifie ce calcul exactement.

## Pourquoi c'est important

BR-CO-16 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-16 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Partez du total TTC, retirez le montant déjà payé s'il y en a un et ajoutez l'arrondi s'il y en a un : le résultat est le net à payer.
2. Si un acompte a été versé, indiquez-le comme montant déjà payé, plutôt que de le retirer du total TTC.
3. Si votre logiciel calcule le net à payer autrement, signalez-le à son éditeur en citant BR-CO-16.

## Causes fréquentes

- **Un acompte retiré du net à payer** sans être indiqué comme montant déjà payé.
- **Un arrondi appliqué au net à payer** sans être indiqué comme montant d'arrondi.
- **Un net à payer mis à zéro** pour une facture déjà réglée, sans indiquer le montant déjà payé.

## Détails techniques

Le net à payer est BT-115, le total TTC BT-112, le montant déjà payé BT-113 et l'arrondi BT-114 ; quand ces deux derniers sont absents, la règle ne les compte pas. En CII : `ram:DuePayableAmount`, `ram:GrandTotalAmount`, `ram:TotalPrepaidAmount` et `ram:RoundingAmount` de `ram:SpecifiedTradeSettlementHeaderMonetarySummation` ; en UBL : `cbc:PayableAmount`, `cbc:TaxInclusiveAmount`, `cbc:PrepaidAmount` et `cbc:PayableRoundingAmount` de `cac:LegalMonetaryTotal`.

## Texte officiel

> Amount due for payment (BT-115) = Invoice total amount with VAT (BT-112) -Paid amount (BT-113) +Rounding amount (BT-114).

BR-CO-16, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-15](../BR-CO-15/) : le total TTC doit être le total HT plus la TVA.
