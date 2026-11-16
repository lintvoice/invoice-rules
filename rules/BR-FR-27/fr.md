# Une caractéristique d'article n'a ni nom ni code

Une caractéristique d'article sur une ligne a un nom vide, un code vide, ou ni l'un ni l'autre.

## Ce que vérifie la règle

Une ligne peut décrire l'article par des caractéristiques, par exemple « Couleur : bleu ». Chaque caractéristique doit avoir un nom (« Couleur ») ou un code, et le nom ou le code indiqué ne doit pas être vide.

## Pourquoi c'est important

BR-FR-27 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez les caractéristiques des articles dans les fiches produits de votre logiciel.
2. Donnez un nom à chaque caractéristique, ou supprimez celles qui sont vides.
3. Si votre logiciel envoie de lui-même des caractéristiques vides, signalez-le à son éditeur en citant BR-FR-27.

## Causes fréquentes

- **Une caractéristique avec une valeur mais sans nom.**
- **Une caractéristique vide** restée dans une fiche produit.

## Détails techniques

Les caractéristiques d'article forment le groupe BG-32 : nom BT-160 (`ram:Description`) et code de l'extension française EXT-FR-FE-159 (`ram:TypeCode`), sous `ram:ApplicableProductCharacteristic` en CII.

## Texte officiel

> Le groupe Attribut d’article (BG-32) doit contenir soit un nom d’attribut d’article (BT-160 : ram:Description), soit un code d’attribut d’article (EXT-FR-FE-159 : ram:TypeCode).

BR-FR-27, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-27_BG-32`, `BR-FR-27_BT-160`, `BR-FR-27_EXT-FR-FE-159`.

## Règles voisines

Pas de règle voisine directe.
