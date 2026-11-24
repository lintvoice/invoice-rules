# Les lignes au taux normal doivent avoir une ventilation de TVA

La facture utilise la catégorie de TVA S (taux normal), mais sa ventilation de TVA l'omet.

## Ce que vérifie la règle

La ventilation de TVA récapitule la TVA de la facture : pour chaque catégorie et chaque taux, sa base et son montant de TVA. La catégorie S couvre la TVA facturée à un taux supérieur à zéro, taux réduits compris. La règle vérifie qu'une facture qui utilise S pour une ligne, une remise ou des frais a une ventilation en S, une par taux.

## Pourquoi c'est important

BR-S-01 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-S-01 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Laissez votre logiciel calculer la ventilation de TVA à partir des lignes : une par catégorie et par taux.
2. Vérifiez que la ventilation est écrite une fois par catégorie, et non une fois par ligne.
3. Si la ventilation manque ou se répète, signalez-le à l'éditeur de votre logiciel en citant BR-S-01.

## Causes fréquentes

- **Une ventilation perdue par un export ou une conversion**, alors que les totaux comptent encore sa TVA.
- **Une ventilation par ligne** au lieu d'une par catégorie et par taux.

## Détails techniques

La ventilation de TVA est le groupe BG-23, son code de catégorie BT-118 ; la catégorie d'une ligne, d'une remise et de frais est BT-151, BT-95 et BT-102. En CII : chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` dont le `ram:CategoryCode` vaut `S` ; en UBL : chaque `cac:TaxSubtotal` dont le `cac:TaxCategory/cbc:ID` vaut `S`.

En CII, le test additionne les lignes (ou remises et frais) au taux normal et les ventilations au taux normal, et en demande au moins deux : une facture qui a deux lignes au taux normal et aucune ventilation au taux normal la passe. UBL demande une ventilation dès qu'une ligne, une remise ou des frais sont en S.

La facture d'exemple a une ligne au taux normal et une ligne exonérée, et aucune ventilation pour le taux normal. Son total de TVA compte toujours la TVA de la ligne, comme l'écrirait un logiciel qui le calcule à partir des lignes : BR-CO-14, qui compare le total de TVA aux ventilations, échoue aussi.

## Texte officiel

> An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is "Standard rated" shall contain in the VAT breakdown (BG-23) at least one VAT category code (BT-118) equal with "Standard rated".

BR-S-01, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-S-08](../BR-S-08/) : pour chaque taux, la base HT doit être la somme des lignes à ce taux, plus les frais et moins les remises au même taux.
- [BR-CO-18](../BR-CO-18/) : toute facture doit détailler sa TVA par catégorie et par taux, même quand la TVA est nulle.
- [BR-CO-14](../BR-CO-14/) : le total de TVA doit être exactement la somme des montants de TVA calculés pour chaque taux, au centime près.
