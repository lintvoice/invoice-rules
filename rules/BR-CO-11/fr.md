# Le total des remises n'est pas la somme des remises

Le total des remises de la facture n'est pas égal à la somme des remises accordées sur l'ensemble de la facture.

## Ce que vérifie la règle

Une facture peut accorder des remises sur son montant global, en plus des remises sur une ligne : par exemple une remise commerciale sur toute la commande. Chacune a son montant, et la facture en donne le total. La règle vérifie que ce total est exactement la somme de ces remises, au centime près. Une facture sans remise globale ne doit pas indiquer de total des remises différent de zéro.

## Pourquoi c'est important

BR-CO-11 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-11 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Additionnez les remises accordées sur l'ensemble de la facture, sans les remises des lignes, et reportez le résultat comme total des remises.
2. Si la facture n'a pas de remise globale, laissez le total des remises vide ou à zéro.
3. Si votre logiciel calcule ce total autrement, signalez-le à son éditeur en citant BR-CO-11.

## Causes fréquentes

- **Les remises des lignes comptées dans le total des remises**, alors que ce total ne concerne que les remises sur l'ensemble de la facture.
- **Une remise ajoutée, modifiée ou retirée après le calcul des totaux.**
- **Une remise en pourcentage arrondie différemment** dans le total et dans la remise elle-même.

## Détails techniques

Le total des remises au niveau du document est BT-107, le montant de chaque remise BT-92 (groupe BG-20). En CII, la règle compare `ram:AllowanceTotalAmount` à la somme des `ram:ActualAmount` des `ram:SpecifiedTradeAllowanceCharge` de `ram:ApplicableHeaderTradeSettlement` dont `ram:ChargeIndicator` vaut false ; en UBL, `cac:LegalMonetaryTotal/cbc:AllowanceTotalAmount` à la somme des `cac:AllowanceCharge/cbc:Amount` dont `cbc:ChargeIndicator` vaut false. Les remises des lignes (BG-27) n'entrent pas dans ce total.

## Texte officiel

> Sum of allowances on document level (BT-107) = Σ Document level allowance amount (BT-92).

BR-CO-11, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-12](../BR-CO-12/) : le total des frais doit être la somme des frais ajoutés à l'ensemble de la facture.
- [BR-CO-13](../BR-CO-13/) : le total HT doit être le total des lignes, moins les remises, plus les frais.
- [BR-CO-21](../BR-CO-21/) : chaque remise globale doit avoir un motif, en texte ou en code.
