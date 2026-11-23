# Le prix brut d'une ligne est négatif

Une ligne indique un prix brut inférieur à zéro.

## Ce que vérifie la règle

Une ligne peut indiquer le prix brut de l'article, son prix catalogue, et le rabais qui mène au prix net. La règle vérifie que le prix brut n'est pas négatif. Un retour ou un remboursement s'écrit par un avoir, ou par une quantité négative, pas par un prix négatif.

## Pourquoi c'est important

BR-28 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-28 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez le signe du prix brut dans votre logiciel : il est toujours positif ou nul.
2. Pour un retour, émettez un avoir, ou une ligne à quantité négative.
3. Si le prix brut sort négatif, signalez-le à l'éditeur de votre logiciel en citant BR-28.

## Causes fréquentes

- **Un signe moins reporté** du rabais sur le prix brut.
- **Un retour saisi avec un prix négatif** au lieu d'une quantité négative.

## Détails techniques

Le prix brut de l'article est BT-148. En CII, c'est le `ram:ChargeAmount` de `ram:GrossPriceProductTradePrice` dans le `ram:SpecifiedLineTradeAgreement` de la ligne ; en UBL, le `cbc:BaseAmount` du `cac:AllowanceCharge` du `cac:Price` de la ligne.

La facture d'exemple écrit le prix brut de sa première ligne avec un signe moins ; son rabais et son prix net restent justes, donc elle échoue à BR-28 seule. Sur une facture française, la règle BR-FR-DEC-03, qui exige un prix positif hors des cadres de facturation S9, M9 et B9, échoue aussi.

## Texte officiel

> The Item gross price (BT-148) shall NOT be negative.

BR-28, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-27](../BR-27/) : le prix unitaire net d'une ligne ne peut pas être négatif : une remise se déclare comme une remise, pas comme une ligne à prix négatif.
- [BR-FR-DEC-03](../BR-FR-DEC-03/) : les prix unitaires doivent avoir au plus 6 décimales et pas de signe moins, sauf avec le cadre de facturation B9, S9 ou M9.
