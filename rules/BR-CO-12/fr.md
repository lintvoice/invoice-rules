# Le total des frais n'est pas la somme des frais

Le total des frais de la facture n'est pas égal à la somme des frais ajoutés à l'ensemble de la facture.

## Ce que vérifie la règle

Une facture peut ajouter des frais à son montant global, en plus des frais sur une ligne : par exemple des frais de port ou d'emballage. Chacun a son montant, et la facture en donne le total. La règle vérifie que ce total est exactement la somme de ces frais, au centime près. Une facture sans frais globaux ne doit pas indiquer de total des frais différent de zéro.

## Pourquoi c'est important

BR-CO-12 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-12 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Additionnez les frais ajoutés à l'ensemble de la facture, sans les frais des lignes, et reportez le résultat comme total des frais.
2. Si la facture n'a pas de frais globaux, laissez le total des frais vide ou à zéro.
3. Si votre logiciel calcule ce total autrement, signalez-le à son éditeur en citant BR-CO-12.

## Causes fréquentes

- **Les frais des lignes comptés dans le total des frais**, alors que ce total ne concerne que les frais sur l'ensemble de la facture.
- **Des frais ajoutés, modifiés ou retirés après le calcul des totaux.**

## Détails techniques

Le total des frais au niveau du document est BT-108, le montant de chaque frais BT-99 (groupe BG-21). En CII, la règle compare `ram:ChargeTotalAmount` à la somme des `ram:ActualAmount` des `ram:SpecifiedTradeAllowanceCharge` de `ram:ApplicableHeaderTradeSettlement` dont `ram:ChargeIndicator` vaut true ; en UBL, `cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` à la somme des `cac:AllowanceCharge/cbc:Amount` dont `cbc:ChargeIndicator` vaut true. Les frais des lignes (BG-28) n'entrent pas dans ce total.

## Texte officiel

> Sum of charges on document level (BT-108) = Σ Document level charge amount (BT-99).

BR-CO-12, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-11](../BR-CO-11/) : le total des remises doit être la somme des remises accordées sur l'ensemble de la facture.
- [BR-CO-13](../BR-CO-13/) : le total HT doit être le total des lignes, moins les remises, plus les frais.
- [BR-CO-22](../BR-CO-22/) : chaque frais global doit avoir un motif, en texte ou en code.
