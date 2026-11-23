# Une ligne n'a pas de montant net

Une ligne de la facture n'indique pas de montant net.

## Ce que vérifie la règle

Chaque ligne d'une facture a un montant net : la quantité multipliée par le prix, moins les remises de la ligne et plus ses frais, hors TVA. La règle vérifie que chaque ligne l'indique.

## Pourquoi c'est important

BR-24 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-24 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez que chaque ligne de la facture a son montant dans votre logiciel, y compris les lignes de texte libre.
2. Pour une ligne qui n'est qu'un commentaire, écrivez-la en note plutôt qu'en ligne.
3. Si une ligne n'a pas de montant dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-24.

## Causes fréquentes

- **Un commentaire saisi comme une ligne**, sans montant.
- **Une ligne de titre** qui regroupe les suivantes.

## Détails techniques

Le montant net de la ligne est BT-131. En CII, c'est le `ram:LineTotalAmount` du `ram:SpecifiedTradeSettlementLineMonetarySummation` de la ligne ; en UBL, le `cbc:LineExtensionAmount` de `cac:InvoiceLine`.

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige le montant net de chaque ligne, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) le laisse en revanche facultatif : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> Each Invoice line (BG-25) shall have an Invoice line net amount (BT-131).

BR-24, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-10](../BR-CO-10/) : le total des lignes HT doit être exactement la somme des montants HT de chaque ligne, au centime près.
- [BR-16](../BR-16/) : toute facture doit contenir au moins une ligne, avoirs compris : pour un montant global, une seule ligne suffit.
- [BR-26](../BR-26/) : chaque ligne doit indiquer son prix unitaire net ; pour un forfait de quantité 1, c'est le montant de la ligne.
