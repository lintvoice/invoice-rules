# Le SIRET ne commence pas par le SIREN

Un SIRET indiqué dans la facture n'a pas 14 chiffres, ou ne commence pas par le SIREN de la même partie.

## Ce que vérifie la règle

Le SIRET identifie un établissement : ses 9 premiers chiffres sont le SIREN de l'entreprise, suivis de 5 chiffres. Quand la facture donne un SIRET pour une partie (vendeur, acheteur, bénéficiaire du paiement, lieu de livraison…), la règle vérifie :

- qu'il compte exactement 14 chiffres ;
- qu'il commence par le SIREN de cette même partie.

## Pourquoi c'est important

BR-FR-09 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez le SIRET de chaque partie dans votre logiciel : 14 chiffres, sans espace.
2. Vérifiez qu'il appartient à la même entreprise que le SIREN indiqué : le SIRET d'une autre société ne peut pas correspondre.
3. Si le SIRET est juste et que l'erreur persiste, votre logiciel associe peut-être le SIRET d'une partie au SIREN d'une autre : signalez-le à son éditeur en citant BR-FR-09.

## Causes fréquentes

- **Le SIRET d'une autre société**, par exemple celui du vendeur recopié pour le bénéficiaire du paiement.
- **Des espaces dans le SIRET** (`012 345 674 00019`).
- **Un SIRET incomplet**, auquel il manque des chiffres.

## Détails techniques

Contrôlé pour le vendeur (BT-29), l'acheteur (BT-46), le bénéficiaire (BT-60) et le lieu de livraison (BT-71, et EXT-FR-FE-146 sur une ligne), ainsi que pour les parties de l'extension française : agent de l'acheteur (EXT-FR-FE-06), payeur (EXT-FR-FE-46), agent du vendeur (EXT-FR-FE-69), facturé (EXT-FR-FE-92) et facturant (EXT-FR-FE-115). Le SIRET est l'identifiant de la partie au schéma `0009` ; le SIREN, l'identifiant légal au schéma `0002`.

## Texte officiel

> Le SIRET doit contenir 14 chiffres et commencer par le SIREN.

BR-FR-09, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-09_BT-29`, `BR-FR-09_BT-46`, `BR-FR-09_BT-60`, `BR-FR-09_BT-71`, `BR-FR-09_EXT-FR-FE-06`, `BR-FR-09_EXT-FR-FE-115`, `BR-FR-09_EXT-FR-FE-146`, `BR-FR-09_EXT-FR-FE-46`, `BR-FR-09_EXT-FR-FE-69`, `BR-FR-09_EXT-FR-FE-92`.

## Règles voisines

- [BR-FR-10](../BR-FR-10/) : le SIREN du vendeur est obligatoire, sur 9 chiffres.
- [BR-FR-32](../BR-FR-32/) : tout SIREN indiqué dans la facture a 9 chiffres.
