# L'adresse électronique de l'acheteur ne commence pas par son SIREN

La facture est déclarée B2B, mais l'adresse électronique de l'acheteur ne commence pas par son SIREN, ou n'utilise pas le code de schéma 0225.

## Ce que vérifie la règle

Quand la facture est déclarée B2B (note BAR) et que ce n'est pas une autofacture, l'adresse électronique de l'acheteur doit :

- commencer par le SIREN de l'acheteur ;
- être déclarée avec le code de schéma 0225.

Pour une autofacture (types 389, 501, 500, 471, 473, 261, 502), c'est l'adresse du vendeur qui est contrôlée (BR-FR-22).

## Pourquoi c'est important

BR-FR-21 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez l'adresse de facturation électronique de votre client : elle commence par son SIREN (9 chiffres).
2. Vérifiez que votre logiciel l'envoie avec le code de schéma 0225.
3. Si l'adresse et le code sont justes dans la fiche client mais pas dans la facture, signalez-le à l'éditeur de votre logiciel en citant BR-FR-21.

## Causes fréquentes

- **Un e-mail à la place de l'adresse de facturation électronique.**
- **L'adresse d'une autre entité** du groupe, avec un autre SIREN.
- **Un code de schéma absent ou différent** (comme 0009 ou EM).

## Détails techniques

BT-49 (adresse électronique de l'acheteur) et son schéma BT-49-1 ; le SIREN de l'acheteur est le BT-47. Types de document (BT-3) d'autofacture exclus : 389, 501, 500, 471, 473, 261, 502.

## Texte officiel

> Si le traitement est BAR/B2B et que le type de document (BT-3) n’est pas en autofacture (389, 501, 500, 471, 473, 261, 502), alors le BT-49 (EndpointID) doit commencer par le SIREN (BT-47) et le BT-49-1 (schemeID) doit être égal à "0225".

BR-FR-21, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-21_BT-49`.

## Règles voisines

- [BR-FR-12](../BR-FR-12/) : l'adresse électronique de l'acheteur est obligatoire.
- [BR-FR-22](../BR-FR-22/) : le même contrôle pour le vendeur sur les autofactures.
- [BR-FR-11](../BR-FR-11/) : une facture B2B exige le SIREN de l'acheteur.
