# Paiement scindé et taux normal sur une même facture

La facture utilise à la fois la catégorie de TVA B (paiement scindé) et la catégorie S (taux normal).

## Ce que vérifie la règle

Avec le paiement scindé italien, l'acheteur verse la TVA à l'administration fiscale ; au taux normal, il la verse au vendeur. Les deux ne se mêlent pas sur une même facture : la règle vérifie qu'une facture en catégorie B n'a aucune ligne, remise, frais ni ventilation en S.

## Pourquoi c'est important

BR-B-02 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-B-02 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. En paiement scindé, donnez la catégorie B à chaque ligne, remise et frais.
2. Hors d'Italie, ou hors paiement scindé, n'utilisez pas B du tout.
3. Si votre logiciel mêle les deux, signalez-le à l'éditeur de votre logiciel en citant BR-B-02.

## Causes fréquentes

- **Une ligne passée en B** alors que les autres restent au taux normal.

## Détails techniques

Les catégories de TVA sont BT-151 (ligne), BT-95 (remise), BT-102 (frais) et BT-118 (ventilation). En CII, la règle regarde chaque `ram:CategoryCode` de la facture ; en UBL, le `cbc:ID` de chaque `cac:TaxCategory` et `cac:ClassifiedTaxCategory`.

La catégorie B est le paiement scindé italien (scissione dei pagamenti) : le vendeur facture la TVA, mais l'acheteur, un organisme public, la verse à l'administration fiscale au lieu du vendeur. Le profil Factur-X EN 16931 n'accepte pas du tout la catégorie B : ses règles `FX-SCH-A-000587` et `FX-SCH-A-000619` échouent à côté de celle-ci dans une facture Factur-X, comme dans la facture d'exemple ; sur une facture française, BR-FR-15, sur les catégories admises en France, échoue en plus. Un ticket ouvert des artefacts de validation EN 16931 propose de retirer la catégorie B et ses deux règles ([ticket n° 537](https://github.com/ConnectingEurope/eInvoicing-EN16931/issues/537)).

La facture d'exemple met sa deuxième ligne en B et garde la première au taux normal ; n'étant pas italienne, elle échoue aussi à BR-B-01.

## Texte officiel

> An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is “Split payment" shall not contain an invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is “Standard rated”.

BR-B-02, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-B-01](../BR-B-01/) : la catégorie de TVA B, le paiement scindé italien, ne va que sur une facture dont les parties et les adresses sont toutes en Italie.
- [BR-S-01](../BR-S-01/) : une facture qui a une ligne, une remise ou des frais de la catégorie de TVA S (taux normal) doit avoir une ventilation de TVA pour cette catégorie.
- [BR-CL-18](../BR-CL-18/) : la catégorie de TVA de chaque ligne et de chaque taux doit être l'un des codes qu'EN 16931 utilise, comme S.
