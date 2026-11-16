# Un identifiant privé contient un caractère non autorisé

Un identifiant de vendeur ou d'acheteur déclaré avec le code de schéma 0224 contient un espace, un accent ou un signe non admis.

## Ce que vérifie la règle

Le vendeur et l'acheteur peuvent être identifiés par un identifiant privé, déclaré avec le code de schéma 0224. Il ne peut contenir que des lettres sans accent, des chiffres et les signes `-`, `_` et `.` ; les espaces sont refusés.

## Pourquoi c'est important

BR-FR-24 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez l'identifiant privé dans la fiche du vendeur ou du client : retirez les espaces, les accents et les autres signes.
2. Par exemple, `CLIENT 0042` devient `CLIENT-0042`.
3. Si votre logiciel modifie l'identifiant à l'export, signalez-le à son éditeur en citant BR-FR-24.

## Causes fréquentes

- **Un espace dans l'identifiant.**
- **Une barre oblique ou un deux-points** comme séparateur.
- **Une lettre accentuée.**

## Détails techniques

Identifiant du vendeur BT-29 et de l'acheteur BT-46 (`ram:GlobalID` en CII) au schéma `0224`. Expression contrôlée : `^[A-Za-z0-9+\-_.]+$`, qui accepte aussi `+`.

## Texte officiel

> L'identifiant privé (ram:GlobalID) ne respecte pas le format autorisé.

BR-FR-24, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-24_BT-29`, `BR-FR-24_BT-46`.

## Règles voisines

- [BR-FR-26](../BR-FR-26/) : un identifiant privé compte au plus 100 caractères.
- [BR-FR-CO-10](../BR-FR-CO-10/) : chaque identifiant a un schéma, utilisé une fois par partie.
