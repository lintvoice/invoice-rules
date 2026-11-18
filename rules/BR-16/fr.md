# La facture n'a aucune ligne

La facture ne contient aucune ligne.

## Ce que vérifie la règle

Toute facture doit contenir au moins une ligne : ce qui est vendu, sa quantité, son prix et son montant. C'est vrai aussi pour un avoir ou pour une facture d'un montant global : une seule ligne suffit alors, avec ce montant et son motif.

## Pourquoi c'est important

BR-16 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-16 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Pour un avoir ou un geste commercial d'un montant global, créez une ligne unique avec le montant, le motif et le taux de TVA qui s'applique.
2. Vérifiez que les lignes saisies dans votre logiciel sont envoyées dans la facture électronique, et pas seulement imprimées sur le PDF.
3. Si votre logiciel produit des factures ou des avoirs sans ligne, signalez-le à son éditeur en citant BR-16.

## Causes fréquentes

- **Un avoir saisi comme un simple montant à rembourser**, sans ligne.
- **Une facture créée à partir d'un total**, sans le détail de ce qui est facturé.
- **Des lignes imprimées sur le PDF** mais absentes des données de la facture électronique.

## Détails techniques

Une ligne de facture est le groupe BG-25. En CII, la règle cherche au moins un `ram:IncludedSupplyChainTradeLineItem` dans le document ; en UBL, au moins un `cac:InvoiceLine` (`cac:CreditNoteLine` dans un avoir).

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige au moins une ligne, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) n'exige en revanche aucune ligne : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> An Invoice shall have at least one Invoice line (BG-25).

BR-16, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-22](../BR-22/) : chaque ligne doit indiquer une quantité.
- [BR-26](../BR-26/) : chaque ligne doit indiquer son prix unitaire net.
