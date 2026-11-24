# Une remise en autoliquidation exige le numéro de TVA du vendeur et un identifiant de l'acheteur

La facture a une remise globale de la catégorie de TVA AE (autoliquidation), mais le numéro de TVA du vendeur manque.

## Ce que vérifie la règle

La catégorie AE couvre les opérations dont l'acheteur, et non le vendeur, déclare la TVA : le vendeur facture sans TVA. L'acheteur paie la TVA à la place du vendeur : la facture dit qui ils sont tous deux pour la TVA. Pour chaque remise en AE, la règle vérifie que la facture identifie le vendeur et l'acheteur. Pour le vendeur : son numéro de TVA (BT-31), son identifiant d'immatriculation fiscale (BT-32) ou le numéro de TVA de son représentant fiscal (BT-63). Pour l'acheteur : son numéro de TVA (BT-48) ou son identifiant d'immatriculation légale (BT-47).

## Pourquoi c'est important

BR-AE-03 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-AE-03 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans la fiche de votre entreprise, dans votre logiciel, renseignez votre numéro de TVA.
2. Vérifiez qu'il est envoyé dans la facture électronique, et pas seulement imprimé sur le PDF.
3. Si votre logiciel ne l'envoie pas, signalez-le à l'éditeur de votre logiciel en citant BR-AE-03.

## Causes fréquentes

- **Un numéro de TVA imprimé dans le pied de page du PDF** mais absent des données de la facture électronique.
- **Une fiche entreprise incomplète** dans le logiciel de facturation.

## Détails techniques

La catégorie de TVA d'une remise au niveau du document est BT-95. Le numéro de TVA du vendeur est BT-31, son identifiant d'immatriculation fiscale BT-32, le numéro de TVA de son représentant fiscal BT-63, le numéro de TVA de l'acheteur BT-48 et son identifiant d'immatriculation légale BT-47. En CII, les numéros de TVA sont `ram:SpecifiedTaxRegistration/ram:ID` avec `schemeID` `VA` ou `FC` dans `ram:SellerTradeParty`, `ram:SellerTaxRepresentativeTradeParty` et `ram:BuyerTradeParty` ; en UBL, `cac:PartyTaxScheme/cbc:CompanyID` dans `cac:AccountingSupplierParty`, `cac:TaxRepresentativeParty` et `cac:AccountingCustomerParty`. BR-AE-02, BR-AE-03 et BR-AE-04 font le même contrôle, à partir d'une ligne, d'une remise et de frais : une facture qui échoue à cette règle échoue aussi à BR-AE-02 dès qu'une de ses lignes est en AE.

La facture d'exemple est entièrement en catégorie AE, avec une remise en AE, et le vendeur n'a pas de numéro de TVA ; sa version corrigée l'indique. Elle échoue aussi à BR-AE-02.

## Texte officiel

> An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Reverse charge" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48) and/or the Buyer legal registration identifier (BT-47).

BR-AE-03, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-AE-02](../BR-AE-02/) : une facture qui a une ligne de la catégorie de TVA AE (autoliquidation) doit indiquer le numéro de TVA du vendeur et un identifiant de l'acheteur.
- [BR-AE-04](../BR-AE-04/) : une facture qui a des frais globaux de la catégorie de TVA AE (autoliquidation) doit indiquer le numéro de TVA du vendeur et un identifiant de l'acheteur.
- [BR-S-02](../BR-S-02/) : une facture dont des lignes sont soumises à la TVA doit indiquer le numéro de TVA du vendeur dans ses données, pas seulement sur le PDF.
