# Les lignes hors du champ de la TVA, avec pourtant un numéro de TVA sur la facture

La facture a une ligne hors du champ de la TVA, mais elle indique un numéro de TVA.

## Ce que vérifie la règle

La catégorie O couvre les opérations auxquelles aucune TVA ne s'applique, comme un service rendu à une entreprise hors de l'UE. Hors du champ de la TVA, la facture ne parle pas de TVA. Elle n'indique aucun numéro de TVA : ni du vendeur, ni de son représentant fiscal, ni de l'acheteur. La règle le vérifie à partir de chaque ligne en O.

## Pourquoi c'est important

BR-O-02 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-O-02 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez que l'opération est vraiment hors du champ de la TVA. Si c'est une opération taxée, exonérée ou au taux zéro, donnez-lui cette catégorie plutôt que O.
2. Si elle est hors du champ de la TVA, retirez de cette facture les numéros de TVA, celui du vendeur compris. Un identifiant d'immatriculation fiscale (BT-32), comme le numéro fiscal allemand, reste permis.
3. Si votre logiciel écrit quand même le numéro de TVA du vendeur, signalez-le à l'éditeur de votre logiciel en citant BR-O-02.

## Causes fréquentes

- **Le numéro de TVA du vendeur écrit sur chaque facture** par le logiciel, depuis la fiche de l'entreprise.
- **La catégorie O utilisée pour une opération exonérée**, qui relèverait de la catégorie E, avec le numéro de TVA du vendeur.

## Détails techniques

La catégorie de TVA d'une ligne est BT-151. Le numéro de TVA du vendeur est BT-31, son identifiant d'immatriculation fiscale BT-32, le numéro de TVA de son représentant fiscal BT-63, le numéro de TVA de l'acheteur BT-48 et son identifiant d'immatriculation légale BT-47. En CII, les numéros de TVA sont `ram:SpecifiedTaxRegistration/ram:ID` avec `schemeID` `VA` dans `ram:SellerTradeParty`, `ram:SellerTaxRepresentativeTradeParty` et `ram:BuyerTradeParty` ; en UBL, `cac:PartyTaxScheme/cbc:CompanyID` dans `cac:AccountingSupplierParty`, `cac:TaxRepresentativeParty` et `cac:AccountingCustomerParty`.

La facture d'exemple est entièrement hors du champ de la TVA, et le vendeur y indique son numéro de TVA ; sa version corrigée l'omet et garde le numéro fiscal allemand du vendeur (Steuernummer) comme identifiant d'immatriculation fiscale (BT-32, `schemeID` `FC` en CII), que la règle permet.

La facture d'exemple est allemande : en France, une entreprise assujettie indique toujours son numéro de TVA sur ses factures (CGI, annexe II, art. 242 nonies A), ce que la catégorie O interdit.

## Texte officiel

> An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Not subject to VAT" shall not contain the Seller VAT identifier (BT-31), the Seller tax representative VAT identifier (BT-63) or the Buyer VAT identifier (BT-48).

BR-O-02, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-O-03](../BR-O-03/) : une facture qui a une remise globale hors du champ de la TVA (O) ne doit indiquer aucun numéro de TVA : ni celui du vendeur, ni celui de son représentant fiscal, ni celui de l'acheteur.
- [BR-O-04](../BR-O-04/) : une facture qui a des frais globaux hors du champ de la TVA (O) ne doit indiquer aucun numéro de TVA : ni celui du vendeur, ni celui de son représentant fiscal, ni celui de l'acheteur.
- [BR-S-02](../BR-S-02/) : une facture dont des lignes sont soumises à la TVA doit indiquer le numéro de TVA du vendeur dans ses données, pas seulement sur le PDF.
