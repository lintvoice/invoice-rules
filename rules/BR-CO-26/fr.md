# Le vendeur n'a aucun identifiant

La facture n'indique aucun identifiant du vendeur.

## Ce que vérifie la règle

Pour que l'acheteur reconnaisse automatiquement son fournisseur, la facture doit identifier le vendeur par au moins un de ces numéros : un identifiant (en France, le SIRET), un numéro d'immatriculation (en France, le SIREN) ou un numéro de TVA intracommunautaire. La règle vérifie qu'au moins un des trois est présent.

## Pourquoi c'est important

BR-CO-26 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-26 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Dans la fiche de votre entreprise, renseignez votre SIREN, votre SIRET et votre numéro de TVA.
2. Vérifiez qu'ils sont envoyés dans la facture électronique, et pas seulement imprimés sur le PDF.
3. Si votre logiciel ne les envoie pas, signalez-le à son éditeur en citant BR-CO-26.

## Causes fréquentes

- **Une fiche entreprise incomplète** dans le logiciel de facturation.
- **Des identifiants imprimés sur le PDF** mais absents des données de la facture électronique.

## Détails techniques

Les identifiants du vendeur sont BT-29 (identifiant, en France le SIRET avec le schéma 0009), BT-30 (numéro d'immatriculation, en France le SIREN avec le schéma 0002) et BT-31 (numéro de TVA). En CII, la règle cherche `ram:ID`, `ram:GlobalID`, `ram:SpecifiedLegalOrganization/ram:ID` ou `ram:SpecifiedTaxRegistration/ram:ID` avec `schemeID` à `VA` dans `ram:SellerTradeParty` ; en UBL, `cac:PartyIdentification/cbc:ID` (sauf schéma `SEPA`), `cac:PartyLegalEntity/cbc:CompanyID` ou `cac:PartyTaxScheme/cbc:CompanyID` (schéma `VAT`) dans `cac:AccountingSupplierParty/cac:Party`.

En France, une facture sans aucun identifiant du vendeur échoue aussi à BR-FR-10, qui exige le SIREN, et à BR-S-02, qui exige un identifiant de TVA du vendeur quand des lignes sont au taux normal. La facture d'exemple échoue donc à ces trois règles.

## Texte officiel

> In order for the buyer to automatically identify a supplier, the Seller identifier (BT-29), the Seller legal registration identifier (BT-30) and/or the Seller VAT identifier (BT-31) shall be present.

BR-CO-26, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-FR-10](../BR-FR-10/) : le SIREN du vendeur est obligatoire et doit avoir 9 chiffres.
- [BR-CO-09](../BR-CO-09/) : un numéro de TVA doit commencer par un code pays.
