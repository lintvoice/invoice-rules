# Une ligne n'a pas de quantité

Une ligne de la facture n'indique pas de quantité facturée.

## Ce que vérifie la règle

Chaque ligne doit indiquer la quantité facturée : un nombre d'articles, d'heures, de jours… Une prestation au forfait a elle aussi une quantité : 1.

## Pourquoi c'est important

BR-22 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-22 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez une quantité sur chaque ligne ; pour un forfait, indiquez 1, avec le montant du forfait comme prix unitaire.
2. Indiquez aussi l'unité de la quantité (unité, heure, jour…), que la règle BR-23 exige.
3. Si votre logiciel n'envoie pas de quantité pour les lignes au forfait, signalez-le à son éditeur en citant BR-22.

## Causes fréquentes

- **Une ligne au forfait** saisie avec un montant seulement, sans quantité ni prix unitaire.
- **Une ligne de titre ou de commentaire** envoyée comme une ligne de facture.

## Détails techniques

La quantité facturée est BT-129, avec son unité BT-130 (BR-23). En CII : `ram:SpecifiedLineTradeDelivery/ram:BilledQuantity` de chaque `ram:IncludedSupplyChainTradeLineItem` ; en UBL : `cbc:InvoicedQuantity` de chaque `cac:InvoiceLine` (`cbc:CreditedQuantity` dans un avoir).

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige une quantité sur chaque ligne, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) n'exige en revanche pas de quantité : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> Each Invoice line (BG-25) shall have an Invoiced quantity (BT-129).

BR-22, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-23](../BR-23/) : la quantité doit indiquer son unité.
- [BR-26](../BR-26/) : chaque ligne doit indiquer son prix unitaire net.
