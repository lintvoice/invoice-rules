# L'exonération de TVA n'a pas de motif

La facture contient une partie exonérée de TVA, mais sa ventilation de TVA n'en indique pas le motif.

## Ce que vérifie la règle

Quand des lignes, des remises ou des frais sont exonérés de TVA, la ventilation de TVA de la facture contient une ligne « exonérée ». Elle doit dire pourquoi : un motif en texte, par exemple la mention légale de l'exonération, un code de motif, ou les deux.

## Pourquoi c'est important

BR-E-10 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-E-10 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans votre logiciel, renseignez le motif d'exonération de chaque article ou prestation exonéré, par exemple la mention que vous imprimez déjà sur vos factures.
2. Si votre logiciel propose des codes de motif, choisissez celui qui correspond à votre cas.
3. Si le motif est saisi mais absent de la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-E-10.

## Causes fréquentes

- **Une mention d'exonération imprimée sur le PDF** mais absente des données de la facture électronique.
- **Un vendeur en franchise en base de TVA** dont le logiciel n'envoie pas le motif de la franchise.
- **Un article exonéré** créé sans motif dans le catalogue du logiciel.

## Détails techniques

La ventilation de TVA est le groupe BG-23 ; pour la catégorie E (« Exempt from VAT »), elle porte le motif d'exonération BT-120 (texte) ou son code BT-121. En CII : `ram:ExemptionReason` ou `ram:ExemptionReasonCode` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` dont `ram:CategoryCode` vaut `E` ; en UBL : `cbc:TaxExemptionReason` ou `cbc:TaxExemptionReasonCode` du `cac:TaxCategory` de chaque `cac:TaxSubtotal` de catégorie `E`.

Le code de motif vient de la liste VATEX, comme l'exige la règle BR-CL-22 ; elle contient des codes propres à la France, comme `VATEX-FR-FRANCHISE` pour la franchise en base. Les autres catégories sans TVA ont leur propre règle : BR-AE-10 (autoliquidation), BR-IC-10 (livraison intracommunautaire), BR-G-10 (export hors de l'Union européenne), BR-O-10 (hors du champ de la TVA).

La facture d'exemple ajoute une ligne exonérée à la facture de base et retire le motif de sa ventilation ; sa version corrigée indique le motif.

## Texte officiel

> A VAT Breakdown (BG-23) with VAT Category code (BT-118) "Exempt from VAT" shall have a VAT exemption reason code (BT-121) or a VAT exemption reason text (BT-120).

BR-E-10, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-S-02](../BR-S-02/) : des lignes soumises à la TVA exigent le numéro de TVA du vendeur.
- [BR-CO-18](../BR-CO-18/) : toute facture doit détailler sa TVA par catégorie et par taux.
