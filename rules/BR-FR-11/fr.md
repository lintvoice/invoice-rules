# Le SIREN de l'acheteur manque sur une facture entre entreprises

La facture est déclarée B2B, mais le SIREN de l'acheteur est absent ou n'a pas 9 chiffres.

## Ce que vérifie la règle

Une note de la facture, codée BAR, indique le type d'opération : B2B (entre entreprises), B2C (vers des particuliers), etc. Quand elle vaut B2B, la règle exige le SIREN de l'acheteur : 9 chiffres, sans espace ni lettre.

## Pourquoi c'est important

BR-FR-11 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

La réforme s'appuie sur des plateformes agréées par l'État et sur un annuaire des destinataires de factures tenu par l'administration ([DGFiP, communiqué du 16 janvier 2026](https://presse.economie.gouv.fr/facturation-electronique-la-direction-generale-des-finances-publiques-publie-la-liste-des-101-premieres-plateformes-agreees/)) : le SIREN identifie l'entreprise qui reçoit la facture.

## Comment corriger

1. Dans la fiche client de votre logiciel, renseignez le SIREN de l'acheteur : 9 chiffres, sans espace.
2. Vous le trouvez sur ses factures, son extrait Kbis ou l'annuaire des entreprises de l'État ([annuaire-entreprises.data.gouv.fr](https://annuaire-entreprises.data.gouv.fr/)).
3. Si votre client est un particulier, la facture ne doit pas être déclarée B2B : vérifiez la note BAR.

## Causes fréquentes

- **La fiche client n'a pas de SIREN.**
- **Le SIRET (14 chiffres) est saisi à la place du SIREN.**
- **Un client particulier facturé comme une entreprise** : la note BAR vaut B2B par erreur.

## Détails techniques

Le type d'opération est une note (BG-1) de code de sujet `BAR` (BT-21), sa valeur étant le texte de la note (BT-22). Le SIREN de l'acheteur est le BT-47, son identifiant d'immatriculation légale au schéma `0002`.

## Texte officiel

> Si une note contient le code sujet BAR avec la valeur 'B2B', alors le SIREN de l’acheteur (BT-47, ram:ID) est obligatoire et doit être composé exactement de 9 chiffres.

BR-FR-11, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-11_BT-47`.

## Règles voisines

- [BR-FR-10](../BR-FR-10/) : le SIREN du vendeur est obligatoire.
- [BR-FR-20](../BR-FR-20/) : les valeurs admises dans la note BAR.
- [BR-FR-21](../BR-FR-21/) : sur une facture B2B, l'adresse électronique de l'acheteur commence par son SIREN.
