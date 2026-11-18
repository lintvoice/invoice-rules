# L'adresse électronique contient un caractère non autorisé

Une adresse électronique déclarée avec le code de schéma 0225 contient un espace, un accent ou un signe non admis.

## Ce que vérifie la règle

Les adresses électroniques déclarées avec le code de schéma 0225, celui des adresses de la réforme française, ne peuvent contenir que des lettres sans accent, des chiffres et les signes `+`, `-`, `_` et `.`. Les espaces, l'arobase (@) et les autres signes sont refusés. La règle vérifie l'adresse de chaque partie : vendeur, acheteur, bénéficiaire, agents, payeur, facturé, facturant.

## Pourquoi c'est important

BR-FR-23 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez l'adresse : retirez les espaces, les accents et les signes non admis.
2. Un e-mail (avec @) n'est pas une adresse 0225 : utilisez l'adresse de facturation électronique de la partie.
3. Si l'adresse est juste dans votre logiciel mais pas dans la facture, signalez-le à son éditeur en citant BR-FR-23.

## Causes fréquentes

- **Un espace dans l'adresse.**
- **Un e-mail** déclaré avec le schéma 0225.
- **Une lettre accentuée.**

## Détails techniques

Adresses électroniques du vendeur (BT-34), acheteur (BT-49), et parties de l'extension française : agent de l'acheteur, bénéficiaire, payeur, agent du vendeur, facturé et facturant (EXT-FR-FE-12, -29, -52, -75, -98, -121), quand leur schéma vaut `0225`. Expression contrôlée : `^[A-Za-z0-9+\-_.]+$` ; le signe `+` est donc accepté aussi, bien que le message officiel ne le cite pas.

## Texte officiel

> L'adresse électronique (ram:URIID) ne respecte pas le format autorisé.

BR-FR-23, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-23_BT-34`, `BR-FR-23_BT-49`, `BR-FR-23_EXT-FR-FE-12`, `BR-FR-23_EXT-FR-FE-121`, `BR-FR-23_EXT-FR-FE-29`, `BR-FR-23_EXT-FR-FE-52`, `BR-FR-23_EXT-FR-FE-75`, `BR-FR-23_EXT-FR-FE-98`.

## Règles voisines

- [BR-FR-25](../BR-FR-25/) : une adresse électronique compte au plus 125 caractères.
- [BR-FR-12](../BR-FR-12/) : l'adresse électronique de l'acheteur est obligatoire.
