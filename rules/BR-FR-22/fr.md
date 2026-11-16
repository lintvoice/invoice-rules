# Sur une autofacture, l'adresse électronique du vendeur ne commence pas par son SIREN

Une autofacture est déclarée B2B, mais l'adresse électronique du vendeur ne commence pas par son SIREN, ou n'utilise pas le code de schéma 0225.

## Ce que vérifie la règle

Une autofacture est établie par l'acheteur au nom du vendeur, et envoyée au vendeur. Quand elle est déclarée B2B, l'adresse électronique du vendeur doit commencer par son SIREN, avec le code de schéma 0225. Types de document d'autofacture : 389, 501, 500, 471, 473, 261, 502.

## Pourquoi c'est important

BR-FR-22 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Demandez à votre fournisseur son adresse de facturation électronique : elle commence par son SIREN.
2. Renseignez-la dans la fiche fournisseur utilisée pour l'autofacturation, avec le code de schéma 0225.
3. Si votre logiciel ne l'envoie pas, signalez-le à son éditeur en citant BR-FR-22.

## Causes fréquentes

- **Votre propre adresse** utilisée comme adresse du vendeur sur l'autofacture.
- **Un e-mail à la place de l'adresse de facturation électronique.**
- **Un code de schéma absent ou différent.**

## Détails techniques

BT-34 (adresse électronique du vendeur) et son schéma BT-34-1 ; le SIREN du vendeur est le BT-30. La règle s'applique quand la note BAR vaut B2B et que le type de document (BT-3) est un type d'autofacture.

## Texte officiel

> Si le traitement est BAR/B2B et que le type de document (BT-3) est en autofacture (389, 501, 500, 471, 473, 261, 502), alors le BT-34 (EndpointID du vendeur) doit commencer par le SIREN (BT-30) et le BT-34-1 (schemeID) doit être égal à "0225".

BR-FR-22, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-22_BT-34`.

## Règles voisines

- [BR-FR-21](../BR-FR-21/) : le même contrôle pour l'acheteur sur les autres factures B2B.
- [BR-FR-13](../BR-FR-13/) : l'adresse électronique du vendeur est obligatoire.
