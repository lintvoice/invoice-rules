# Une remise globale n'a pas de catégorie de TVA

Une remise globale n'indique pas de catégorie de TVA.

## Ce que vérifie la règle

Une remise globale réduit la TVA de la facture, donc elle indique à quelle catégorie de TVA elle appartient (taux normal, exonération, autoliquidation…) et à quel taux. La ventilation de TVA la compte dans cette catégorie. La règle vérifie que la catégorie est indiquée.

## Pourquoi c'est important

BR-32 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-32 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Donnez à chaque remise globale la catégorie et le taux de TVA de ce à quoi elle s'applique, dans votre logiciel.
2. Vérifiez que la facture électronique les écrit, et pas seulement le montant.
3. Si la catégorie manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-32.

## Causes fréquentes

- **Une remise globale saisie comme un simple montant**, sans TVA.
- **Une facture à plusieurs taux de TVA**, où le logiciel ne sait pas lequel s'applique.

## Détails techniques

Une remise au niveau du document est le groupe BG-20, son code de catégorie de TVA BT-95. En CII, la règle lit le `ram:CategoryCode` du `ram:CategoryTradeTax` dont le `ram:TypeCode` vaut VAT, dans chaque `ram:SpecifiedTradeAllowanceCharge` de `ram:ApplicableHeaderTradeSettlement` dont `ram:ChargeIndicator` vaut false ; en UBL, le `cbc:ID` du `cac:TaxCategory` de la remise.

La facture d'exemple donne une remise sans sa catégorie de TVA. La remise ne réduit alors aucune ventilation de TVA, donc la base du taux normal ne correspond plus à ses lignes moins ses remises, et BR-S-08 échoue aussi. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence de la catégorie : dans une facture Factur-X, sa règle `FX-SCH-A-000185` échoue donc à côté de BR-32, comme dans la facture d'exemple.

## Texte officiel

> Each Document level allowance (BG-20) shall have a Document level allowance VAT category code (BT-95).

BR-32, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-31](../BR-31/) : chaque remise globale doit indiquer son montant.
- [BR-33](../BR-33/) : chaque remise globale doit indiquer son motif : en texte, en code, ou les deux.
- [BR-S-08](../BR-S-08/) : pour chaque taux, la base HT doit être la somme des lignes à ce taux, plus les frais et moins les remises au même taux.
- [BR-CL-17](../BR-CL-17/) : la catégorie de TVA d'une remise ou de frais globaux doit être l'un des codes qu'EN 16931 utilise, comme S.
