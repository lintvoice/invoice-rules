# Un taux de TVA n'a pas de base

Une ventilation de TVA n'indique pas de base.

## Ce que vérifie la règle

La ventilation de TVA donne, pour chaque catégorie et chaque taux de TVA de la facture, sa base, son montant de TVA, sa catégorie et son taux. La règle vérifie que chacune indique sa base.

## Pourquoi c'est important

BR-45 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-45 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez que votre logiciel calcule la base de chaque catégorie de TVA, y compris les exonérées et celles à 0 %.
2. Vérifiez que la facture électronique écrit la ventilation de TVA en entier, un bloc par catégorie et par taux.
3. Si ille manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-45.

## Causes fréquentes

- **Une catégorie sans TVA oubliée dans le calcul**, une ligne exonérée par exemple.
- **Une ventilation de TVA construite à la main** dans un export, champ par champ.

## Détails techniques

Une ventilation de TVA est le groupe BG-23, ici son base BT-116. En CII, c'est le `ram:BasisAmount` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, le `cbc:TaxableAmount` de chaque `cac:TaxSubtotal`.

La facture d'exemple a une ligne exonérée dont la ventilation de TVA n'indique pas de base. La règle BR-E-08, qui compare ce montant aux lignes exonérées, échoue aussi. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence du montant : dans une facture Factur-X, sa règle `FX-SCH-A-000177` échoue donc à côté de BR-45, comme dans la facture d'exemple.

## Texte officiel

> Each VAT breakdown (BG-23) shall have a VAT category taxable amount (BT-116).

BR-45, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-46](../BR-46/) : chaque ventilation de TVA doit indiquer son montant de TVA, même nul.
- [BR-S-08](../BR-S-08/) : pour chaque taux, la base HT doit être la somme des lignes à ce taux, plus les frais et moins les remises au même taux.
