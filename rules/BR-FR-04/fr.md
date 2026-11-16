# Le type de document n'est pas dans la liste française

Le code qui indique ce qu'est le document (facture, avoir, acompte…) n'est pas admis par les règles françaises.

## Ce que vérifie la règle

Chaque facture porte un code à 3 chiffres qui dit ce qu'elle est, par exemple 380 (facture), 381 (avoir), 384 (facture rectificative), 386 (facture d'acompte) ou 389 (autofacture). Les règles françaises n'admettent que ces 16 codes : 380, 389, 393, 501, 386, 500, 384, 471, 472, 473, 261, 262, 381, 396, 502, 503.

La règle vérifie le code de la facture, et celui d'un document antérieur qu'elle cite, en tête ou sur une ligne.

## Pourquoi c'est important

BR-FR-04 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

La liste internationale de codes (UNTDID 1001) en compte bien d'autres ; le message officiel précise qu'ils ne doivent pas être utilisés.

## Comment corriger

1. Vérifiez le type choisi dans votre logiciel : facture, avoir, acompte, facture rectificative.
2. Utilisez un code de la liste, par exemple 380 pour une facture ordinaire au lieu de 326 (facture partielle).
3. Si votre logiciel ne propose aucun type admis, signalez-le à son éditeur en citant BR-FR-04.

## Causes fréquentes

- **Un code valable en Europe mais pas en France**, comme 326 (facture partielle).
- **Un code par défaut d'un logiciel conçu pour un autre pays.**
- **Le type d'un document antérieur cité** est faux, alors que celui de la facture est correct.

## Détails techniques

Le type de document est le BT-3 (codes UNTDID 1001). La règle s'applique aussi au type d'un document référencé (EXT-FR-FE-02) et d'un document référencé sur une ligne (EXT-FR-FE-137).

## Texte officiel

> Le code type de document (ram:TypeCode) n’est pas autorisé. Valeurs acceptées : 380, 389, 393, 501, 386, 500, 384, 471, 472, 473, 261, 262, 381, 396, 502, 503.

BR-FR-04, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-04_BT-3`, `BR-FR-04_EXT-FR-FE-02`, `BR-FR-04_EXT-FR-FE-137`.

## Règles voisines

- [BR-FR-CO-04](../BR-FR-CO-04/) : une facture rectificative doit citer exactement une facture antérieure.
- [BR-FR-CO-05](../BR-FR-CO-05/) : un avoir doit citer la facture qu'il corrige.
