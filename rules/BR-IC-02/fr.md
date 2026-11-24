# Les livraisons intracommunautaires exigent les deux numéros de TVA

La facture a une ligne de la catégorie de TVA K (livraison intracommunautaire), mais le numéro de TVA de l'acheteur manque.

## Ce que vérifie la règle

La catégorie K couvre les biens vendus et expédiés à une entreprise d'un autre pays de l'UE, qui y déclare la TVA. L'exonération repose sur le numéro de TVA de l'acheteur dans un autre pays de l'UE. Il montre que l'acheteur est une entreprise qui déclarera la TVA. Pour chaque ligne en K, la règle vérifie que la facture indique les deux numéros de TVA. Pour le vendeur : le sien (BT-31) ou celui de son représentant fiscal (BT-63). Pour l'acheteur : son numéro de TVA (BT-48).

## Pourquoi c'est important

BR-IC-02 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-IC-02 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Demandez à l'acheteur son numéro de TVA dans son pays, et vérifiez-le dans le service VIES de la Commission européenne.
2. Renseignez-le dans la fiche de l'acheteur dans votre logiciel, pour que chaque facture à cet acheteur le porte.
3. Si le numéro est saisi mais manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-IC-02.

## Causes fréquentes

- **Une fiche acheteur sans numéro de TVA**, créée avant la première vente à l'étranger.
- **Le numéro de TVA de l'acheteur imprimé sur le PDF** mais absent des données de la facture électronique.

## Détails techniques

La catégorie de TVA d'une ligne est BT-151. Le numéro de TVA du vendeur est BT-31, son identifiant d'immatriculation fiscale BT-32, le numéro de TVA de son représentant fiscal BT-63, le numéro de TVA de l'acheteur BT-48 et son identifiant d'immatriculation légale BT-47. En CII, les numéros de TVA sont `ram:SpecifiedTaxRegistration/ram:ID` avec `schemeID` `VA` dans `ram:SellerTradeParty`, `ram:SellerTaxRepresentativeTradeParty` et `ram:BuyerTradeParty` ; en UBL, `cac:PartyTaxScheme/cbc:CompanyID` dans `cac:AccountingSupplierParty`, `cac:TaxRepresentativeParty` et `cac:AccountingCustomerParty`.

La facture d'exemple est entièrement en catégorie K, et l'acheteur n'a pas de numéro de TVA ; sa version corrigée l'indique.

## Texte officiel

> An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Intra-community supply" shall contain the Seller VAT Identifier (BT-31) or the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48).

BR-IC-02, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-IC-03](../BR-IC-03/) : une facture qui a une remise globale de la catégorie de TVA K (livraison intracommunautaire) doit indiquer les numéros de TVA du vendeur et de l'acheteur.
- [BR-IC-04](../BR-IC-04/) : une facture qui a des frais globaux de la catégorie de TVA K (livraison intracommunautaire) doit indiquer les numéros de TVA du vendeur et de l'acheteur.
- [BR-S-02](../BR-S-02/) : une facture dont des lignes sont soumises à la TVA doit indiquer le numéro de TVA du vendeur dans ses données, pas seulement sur le PDF.
