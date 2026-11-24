# Une catégorie de TVA n'a pas de taux

Une ventilation de TVA n'indique pas de taux.

## Ce que vérifie la règle

La ventilation de TVA donne, pour chaque catégorie et chaque taux de TVA de la facture, sa base, son montant de TVA, sa catégorie et son taux. La règle vérifie que chacune indique son taux, 0 pour une catégorie exonérée ; seule la catégorie O, hors du champ de la TVA, n'en a pas.

## Pourquoi c'est important

BR-48 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-48 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Pour une catégorie exonérée, ou un taux de 0 %, écrivez le taux 0.
2. Vérifiez que la facture électronique écrit la ventilation de TVA en entier, un bloc par catégorie et par taux.
3. S'il manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-48.

## Causes fréquentes

- **Un taux omis parce qu'il est nul**, pour une ligne exonérée.
- **Une ventilation de TVA construite à la main** dans un export, champ par champ.

## Détails techniques

Une ventilation de TVA est le groupe BG-23, ici son taux de TVA BT-119. En CII, c'est le `ram:RateApplicablePercent` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, le `cac:TaxCategory/cbc:Percent` de chaque `cac:TaxSubtotal`.

La règle fait une exception : la catégorie O, opérations hors du champ de la TVA, qui n'a pas de taux. Une catégorie exonérée, E, en a un : 0.

La facture d'exemple a une ligne exonérée dont la ventilation de TVA n'indique pas de taux, donc elle échoue à BR-48 seule.

## Texte officiel

> Each VAT breakdown (BG-23) shall have a VAT category rate (BT-119), except if the Invoice is not subject to VAT.

BR-48, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-47](../BR-47/) : chaque ventilation de TVA doit indiquer sa catégorie de TVA : taux normal, exonération, autoliquidation…
