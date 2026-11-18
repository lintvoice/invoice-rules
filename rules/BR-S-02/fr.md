# Le numéro de TVA du vendeur manque

Des lignes de la facture sont soumises à la TVA, mais la facture n'indique pas le numéro de TVA du vendeur.

## Ce que vérifie la règle

Dès qu'une ligne est soumise à la TVA à un taux supérieur à zéro, la facture doit identifier le vendeur pour la TVA : son numéro de TVA intracommunautaire, ou celui de son représentant fiscal s'il en a un.

## Pourquoi c'est important

BR-S-02 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-S-02 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans la fiche de votre entreprise, renseignez votre numéro de TVA intracommunautaire.
2. Vérifiez qu'il est envoyé dans la facture électronique, et pas seulement imprimé sur le PDF.
3. Si votre entreprise ne facture pas de TVA (franchise en base, par exemple), vos lignes ne doivent pas être déclarées soumises à la TVA : elles sont exonérées, avec le motif de la franchise (voir BR-E-10).
4. Si votre logiciel n'envoie pas votre numéro de TVA, signalez-le à son éditeur en citant BR-S-02.

## Causes fréquentes

- **Un numéro de TVA imprimé dans le pied de page du PDF** mais absent des données de la facture électronique.
- **Une fiche entreprise incomplète** dans le logiciel de facturation.
- **Un vendeur en franchise en base de TVA**, sans numéro de TVA, dont le logiciel déclare les lignes soumises à la TVA.

## Détails techniques

La catégorie de TVA d'une ligne est BT-151. La catégorie S (« Standard rated ») est celle de tout taux supérieur à zéro, taux réduits compris (BR-S-05 exige un taux positif). Le numéro de TVA du vendeur est BT-31, son identifiant fiscal BT-32, le numéro de TVA de son représentant fiscal BT-63.

En CII, la règle part de chaque `ram:ApplicableTradeTax` de ligne dont `ram:CategoryCode` vaut `S`, et cherche `ram:SpecifiedTaxRegistration/ram:ID` avec `schemeID` à `VA` ou `FC` dans `ram:SellerTradeParty`, ou avec `schemeID` à `VA` dans `ram:SellerTaxRepresentativeTradeParty` ; en UBL, `cac:PartyTaxScheme/cbc:CompanyID` dans `cac:AccountingSupplierParty/cac:Party`, ou celui de `cac:TaxRepresentativeParty`. BR-S-03 et BR-S-04 font le même contrôle pour une remise ou des frais au niveau de la facture.

Pour une franchise en base, la liste VATEX des codes de motif d'exonération (BT-121) contient `VATEX-FR-FRANCHISE`. Une facture sans aucun identifiant du vendeur échoue aussi à BR-CO-26 et, en France, à BR-FR-10 ; la facture d'exemple garde le SIREN et le SIRET du vendeur et n'échoue qu'à BR-S-02.

## Texte officiel

> An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Standard rated" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63).

BR-S-02, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-26](../BR-CO-26/) : le vendeur doit avoir au moins un identifiant.
- [BR-CO-09](../BR-CO-09/) : un numéro de TVA doit commencer par un code pays.
- [BR-E-10](../BR-E-10/) : une exonération de TVA doit indiquer son motif.
