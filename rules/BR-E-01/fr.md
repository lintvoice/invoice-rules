# Les lignes exonérées doivent avoir une ventilation de TVA, une seule

La facture utilise la catégorie de TVA E (exonération), mais sa ventilation de TVA l'omet, ou la donne deux fois.

## Ce que vérifie la règle

La ventilation de TVA récapitule la TVA de la facture : pour chaque catégorie et chaque taux, sa base et son montant de TVA. La catégorie E couvre les opérations que la loi exonère de TVA, comme le transport de marchandises exportées. Sa TVA vaut 0, mais elle a quand même une ventilation, une seule pour toutes ses lignes, remises et frais. La règle vérifie que la facture en a exactement une.

## Pourquoi c'est important

BR-E-01 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-E-01 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Laissez votre logiciel calculer la ventilation de TVA à partir des lignes : une par catégorie et par taux, même quand la TVA vaut 0.
2. Vérifiez que la ventilation est écrite une fois par catégorie, et non une fois par ligne.
3. Si la ventilation manque ou se répète, signalez-le à l'éditeur de votre logiciel en citant BR-E-01.

## Causes fréquentes

- **Une ventilation écrite seulement pour les catégories qui portent de la TVA**, sans celles à 0.
- **Une ventilation par ligne** au lieu d'une par catégorie et par taux.

## Détails techniques

La ventilation de TVA est le groupe BG-23, son code de catégorie BT-118 ; la catégorie d'une ligne, d'une remise et de frais est BT-151, BT-95 et BT-102. En CII : chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` dont le `ram:CategoryCode` vaut `E` ; en UBL : chaque `cac:TaxSubtotal` dont le `cac:TaxCategory/cbc:ID` vaut `E`.

En CII, la règle refuse aussi une ventilation de la catégorie quand aucune ligne, remise ni frais ne l'utilise ; UBL ne contrôle pas ce sens ([ticket n° 538](https://github.com/ConnectingEurope/eInvoicing-EN16931/issues/538), ouvert).

La facture d'exemple a deux lignes de catégorie E et une au taux normal, et omet la ventilation en E ; sa version corrigée la contient. La TVA de la catégorie vaut 0 : aucun total ne change, et l'exemple n'échoue qu'à cette règle.

## Texte officiel

> An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Exempt from VAT" shall contain exactly one VAT breakdown (BG-23) with the VAT category code (BT-118) equal to "Exempt from VAT".

BR-E-01, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-E-08](../BR-E-08/) : dans la ventilation de TVA, la base de la catégorie E (exonération) est la somme de ses lignes, plus ses frais, moins ses remises.
- [BR-CO-18](../BR-CO-18/) : toute facture doit détailler sa TVA par catégorie et par taux, même quand la TVA est nulle.
- [BR-E-02](../BR-E-02/) : une facture qui a une ligne de la catégorie de TVA E (exonération) doit indiquer le numéro de TVA du vendeur, ou celui de son représentant fiscal.
