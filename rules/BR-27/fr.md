# Le prix net d'une ligne est négatif

Le prix unitaire net d'une ligne de la facture est négatif.

## Ce que vérifie la règle

Le prix unitaire net d'une ligne ne peut pas être négatif : il peut valoir zéro, jamais moins. Une remise, un acompte déduit ou un retour d'article ne s'écrivent donc pas comme une ligne à prix négatif.

## Pourquoi c'est important

BR-27 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-27 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Pour une remise, utilisez la remise de votre logiciel : sur la ligne concernée, ou sur l'ensemble de la facture.
2. Pour un acompte déjà versé, indiquez-le comme montant déjà payé : il se déduit du net à payer.
3. Pour un article repris ou retourné, indiquez une quantité négative avec un prix positif, ou émettez un avoir.
4. Si votre logiciel ne permet les remises que sous forme de ligne à prix négatif, signalez-le à son éditeur en citant BR-27.

## Causes fréquentes

- **Une remise saisie comme une ligne** à prix négatif.
- **Un acompte déduit** sous forme de ligne négative.
- **Un retour d'article** facturé avec un prix négatif au lieu d'une quantité négative.

## Détails techniques

Le prix unitaire net est BT-146. En CII : `ram:NetPriceProductTradePrice/ram:ChargeAmount` dans `ram:SpecifiedLineTradeAgreement` ; en UBL : `cac:Price/cbc:PriceAmount` de chaque `cac:InvoiceLine`. La règle accepte un prix nul. Une quantité négative (BT-129) reste possible : la règle française BR-FR-DEC-02 accepte le signe « - ».

En France, la règle BR-FR-DEC-03 exige en plus un prix sans signe « - », sauf pour les cadres de facturation S9, M9 et B9 : la facture d'exemple, une facture française qui saisit une remise comme une ligne à −50,00 €, échoue donc aux deux règles. Sa version corrigée porte la même remise au niveau de la facture.

## Texte officiel

> The Item net price (BT-146) shall NOT be negative.

BR-27, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-26](../BR-26/) : chaque ligne doit indiquer son prix unitaire net.
- [BR-FR-DEC-03](../BR-FR-DEC-03/) : en France, un prix unitaire s'écrit sans signe « - ».
- [BR-CO-21](../BR-CO-21/) : une remise sur l'ensemble de la facture doit indiquer son motif.
