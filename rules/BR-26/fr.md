# Une ligne n'a pas de prix unitaire net

Une ligne de la facture n'indique pas son prix unitaire net.

## Ce que vérifie la règle

Chaque ligne doit indiquer son prix unitaire net : le prix d'une unité, hors TVA, remise sur le prix déduite. Pour une prestation au forfait de quantité 1, ce prix est le montant du forfait.

## Pourquoi c'est important

BR-26 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-26 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez un prix unitaire sur chaque ligne ; pour un forfait, indiquez une quantité de 1 et le montant du forfait comme prix.
2. Vérifiez que le montant de la ligne correspond à la quantité multipliée par le prix, remises et frais de la ligne compris.
3. Si votre logiciel n'envoie pas de prix unitaire, signalez-le à son éditeur en citant BR-26.

## Causes fréquentes

- **Une ligne au forfait** saisie avec un montant seulement.
- **Un prix unitaire imprimé sur le PDF** mais absent des données de la facture électronique.

## Détails techniques

Le prix unitaire net est BT-146. En CII : `ram:NetPriceProductTradePrice/ram:ChargeAmount` dans `ram:SpecifiedLineTradeAgreement` ; en UBL : `cac:Price/cbc:PriceAmount` de chaque `cac:InvoiceLine`. Le prix brut (BT-148) et la remise sur le prix (BT-147) sont facultatifs : le prix net est le prix brut moins cette remise.

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige un prix net sur chaque ligne, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) laisse en revanche le prix net facultatif : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> Each Invoice line (BG-25) shall contain the Item net price (BT-146).

BR-26, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-27](../BR-27/) : le prix unitaire net ne peut pas être négatif.
- [BR-22](../BR-22/) : chaque ligne doit indiquer une quantité.
