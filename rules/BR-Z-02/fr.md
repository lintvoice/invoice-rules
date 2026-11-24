# Les lignes au taux zéro exigent le numéro de TVA du vendeur

La facture a une ligne de la catégorie de TVA Z (taux zéro), mais le numéro de TVA du vendeur manque.

## Ce que vérifie la règle

La catégorie Z couvre les opérations taxées au taux de 0 %, comme les panneaux solaires vendus à leur exploitant en Allemagne. Une entreprise qui réalise des opérations de catégorie Z est identifiée à la TVA, et sa facture l'indique. Pour chaque ligne en Z, la règle vérifie que la facture identifie le vendeur pour la TVA. L'un de ces numéros suffit : son numéro de TVA (BT-31), son identifiant d'immatriculation fiscale (BT-32), le numéro de TVA de son représentant fiscal (BT-63).

## Pourquoi c'est important

BR-Z-02 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-Z-02 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans la fiche de votre entreprise, dans votre logiciel, renseignez votre numéro de TVA.
2. Vérifiez qu'il est envoyé dans la facture électronique, et pas seulement imprimé sur le PDF.
3. Si votre logiciel ne l'envoie pas, signalez-le à l'éditeur de votre logiciel en citant BR-Z-02.

## Causes fréquentes

- **Un numéro de TVA imprimé dans le pied de page du PDF** mais absent des données de la facture électronique.
- **Une fiche entreprise incomplète** dans le logiciel de facturation.

## Détails techniques

La catégorie de TVA d'une ligne est BT-151. Le numéro de TVA du vendeur est BT-31, son identifiant d'immatriculation fiscale BT-32, le numéro de TVA de son représentant fiscal BT-63, le numéro de TVA de l'acheteur BT-48 et son identifiant d'immatriculation légale BT-47. En CII, les numéros de TVA sont `ram:SpecifiedTaxRegistration/ram:ID` avec `schemeID` `VA` ou `FC` dans `ram:SellerTradeParty`, `ram:SellerTaxRepresentativeTradeParty` et `ram:BuyerTradeParty` ; en UBL, `cac:PartyTaxScheme/cbc:CompanyID` dans `cac:AccountingSupplierParty`, `cac:TaxRepresentativeParty` et `cac:AccountingCustomerParty`.

La facture d'exemple est entièrement en catégorie Z, et le vendeur n'a pas de numéro de TVA ; sa version corrigée l'indique.

La facture d'exemple est allemande : la France n'a pas de taux zéro pour ses opérations intérieures.

## Texte officiel

> An Invoice that contains an Invoice line where the Invoiced item VAT category code (BT-151) is "Zero rated" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63).

BR-Z-02, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-Z-03](../BR-Z-03/) : une facture qui a une remise globale de la catégorie de TVA Z (taux zéro) doit indiquer le numéro de TVA du vendeur, ou celui de son représentant fiscal.
- [BR-Z-04](../BR-Z-04/) : une facture qui a des frais globaux de la catégorie de TVA Z (taux zéro) doit indiquer le numéro de TVA du vendeur, ou celui de son représentant fiscal.
- [BR-S-02](../BR-S-02/) : une facture dont des lignes sont soumises à la TVA doit indiquer le numéro de TVA du vendeur dans ses données, pas seulement sur le PDF.
