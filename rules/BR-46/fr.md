# Un taux de TVA n'a pas de montant de TVA

Une ventilation de TVA n'indique pas de montant de TVA.

## Ce que vérifie la règle

La ventilation de TVA donne, pour chaque catégorie et chaque taux de TVA de la facture, sa base, son montant de TVA, sa catégorie et son taux. La règle vérifie que chacune indique son montant de TVA, 0 pour une catégorie sans TVA.

## Pourquoi c'est important

BR-46 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-46 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Pour une catégorie exonérée, ou un taux de 0 %, écrivez un montant de TVA de 0.
2. Vérifiez que la facture électronique écrit la ventilation de TVA en entier, un bloc par catégorie et par taux.
3. Si il manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-46.

## Causes fréquentes

- **Un montant de TVA omis parce qu'il est nul**, pour une ligne exonérée.
- **Une ventilation de TVA construite à la main** dans un export, champ par champ.

## Détails techniques

Une ventilation de TVA est le groupe BG-23, ici son montant de TVA BT-117. En CII, c'est le `ram:CalculatedAmount` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, le `cbc:TaxAmount` de chaque `cac:TaxSubtotal`.

La facture d'exemple a une ligne exonérée dont la ventilation de TVA n'indique pas de montant de TVA, bien qu'il soit nul. Les règles BR-CO-17 et BR-E-09, qui contrôlent ce montant, échouent aussi. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence du montant : dans une facture Factur-X, sa règle `FX-SCH-A-000176` échoue donc à côté de BR-46, comme dans la facture d'exemple.

## Texte officiel

> Each VAT breakdown (BG-23) shall have a VAT category tax amount (BT-117).

BR-46, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-45](../BR-45/) : chaque ventilation de TVA doit indiquer sa base, le total hors TVA de ce qui est facturé dans sa catégorie et à son taux.
- [BR-CO-17](../BR-CO-17/) : pour chaque taux, le montant de TVA doit être la base HT multipliée par le taux, arrondie au centime.
