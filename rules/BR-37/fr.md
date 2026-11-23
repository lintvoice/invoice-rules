# Des frais globaux n'ont pas de catégorie de TVA

Des frais globaux n'indiquent pas de catégorie de TVA.

## Ce que vérifie la règle

Des frais globaux augmentent la TVA de la facture, donc ils indiquent à quelle catégorie de TVA ils appartiennent (taux normal, exonération, autoliquidation…) et à quel taux. La ventilation de TVA les compte dans cette catégorie. La règle vérifie que la catégorie est indiquée.

## Pourquoi c'est important

BR-37 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-37 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Donnez aux frais globaux la catégorie et le taux de TVA de ce à quoi ils s'appliquent, dans votre logiciel.
2. Vérifiez que la facture électronique les écrit, et pas seulement le montant.
3. Si la catégorie manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-37.

## Causes fréquentes

- **Des frais globaux saisis comme un simple montant**, sans TVA.
- **Une facture à plusieurs taux de TVA**, où le logiciel ne sait pas lequel s'applique.

## Détails techniques

Des frais au niveau du document forment le groupe BG-21, leur code de catégorie de TVA est BT-102. En CII, la règle lit le `ram:CategoryCode` du `ram:CategoryTradeTax` dont le `ram:TypeCode` vaut VAT, dans chaque `ram:SpecifiedTradeAllowanceCharge` de `ram:ApplicableHeaderTradeSettlement` dont `ram:ChargeIndicator` vaut true ; en UBL, le `cbc:ID` du `cac:TaxCategory` des frais.

La facture d'exemple donne des frais sans leur catégorie de TVA. Les frais ne s'ajoutent alors à aucune ventilation de TVA, donc la base du taux normal ne correspond plus à ses lignes plus ses frais, et BR-S-08 échoue aussi. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence de la catégorie : dans une facture Factur-X, sa règle `FX-SCH-A-000479` échoue donc à côté de BR-37, comme dans la facture d'exemple.

## Texte officiel

> Each Document level charge (BG-21) shall have a Document level charge VAT category code (BT-102).

BR-37, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-36](../BR-36/) : des frais globaux doivent toujours indiquer leur montant.
- [BR-38](../BR-38/) : les frais globaux doivent indiquer leur motif : en texte, en code, ou les deux.
- [BR-S-08](../BR-S-08/) : pour chaque taux, la base HT doit être la somme des lignes à ce taux, plus les frais et moins les remises au même taux.
- [BR-CL-17](../BR-CL-17/) : la catégorie de TVA d'une remise ou de frais globaux doit être l'un des codes qu'EN 16931 utilise, comme S.
