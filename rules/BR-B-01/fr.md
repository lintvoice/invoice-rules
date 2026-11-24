# Le paiement scindé est réservé aux factures italiennes

La facture utilise la catégorie de TVA B (paiement scindé), mais ce n'est pas une facture italienne.

## Ce que vérifie la règle

Le paiement scindé est un régime italien. La règle vérifie qu'une facture qui utilise la catégorie B n'a que l'Italie pour pays : chacun de ses codes pays, ceux du vendeur et de l'acheteur compris, vaut IT.

## Pourquoi c'est important

BR-B-01 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-B-01 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Hors d'Italie, donnez aux lignes la catégorie qui leur correspond, comme S pour le taux normal.
2. Si votre logiciel a choisi B de lui-même, signalez-le à l'éditeur de votre logiciel en citant BR-B-01.

## Causes fréquentes

- **Le code B pris dans la liste des catégories de TVA** pour un autre sens que le paiement scindé italien.

## Détails techniques

Les catégories de TVA sont BT-151 (ligne), BT-95 (remise), BT-102 (frais) et BT-118 (ventilation) ; les codes pays, dont BT-40 pour le vendeur et BT-55 pour l'acheteur. En CII, la règle regarde chaque `ram:CountryID` et chaque `ram:CategoryCode` de la facture ; en UBL, chaque `cbc:IdentificationCode` et le `cbc:ID` de chaque `cac:TaxCategory` et `cac:ClassifiedTaxCategory`.

La catégorie B est le paiement scindé italien (scissione dei pagamenti) : le vendeur facture la TVA, mais l'acheteur, un organisme public, la verse à l'administration fiscale au lieu du vendeur. Le profil Factur-X EN 16931 n'accepte pas du tout la catégorie B : ses règles `FX-SCH-A-000587` et `FX-SCH-A-000619` échouent à côté de celle-ci dans une facture Factur-X, comme dans la facture d'exemple ; sur une facture française, BR-FR-15, sur les catégories admises en France, échoue en plus. Un ticket ouvert des artefacts de validation EN 16931 propose de retirer la catégorie B et ses deux règles ([ticket n° 537](https://github.com/ConnectingEurope/eInvoicing-EN16931/issues/537)).

La facture d'exemple met ses lignes en catégorie B, entre deux entreprises hors d'Italie ; sa version corrigée est la facture de base, au taux normal.

## Texte officiel

> An Invoice where the VAT category code (BT-151, BT-95 or BT-102) is “Split payment” shall be a domestic Italian invoice.

BR-B-01, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-B-02](../BR-B-02/) : une facture qui utilise la catégorie de TVA B, le paiement scindé italien, n'utilise pas aussi le taux normal, S.
- [BR-CL-18](../BR-CL-18/) : la catégorie de TVA de chaque ligne et de chaque taux doit être l'un des codes qu'EN 16931 utilise, comme S.
- [BR-FR-15](../BR-FR-15/) : chaque montant soumis à TVA doit utiliser une des catégories S, E, AE, K, G, O ou Z ; les catégories L et M (îles Canaries, Ceuta et Melilla) ne s'appliquent pas en France.
