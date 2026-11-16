# Le SIREN du vendeur est absent ou n'a pas 9 chiffres

La facture ne porte pas le SIREN du vendeur, ou ce SIREN n'a pas exactement 9 chiffres.

## Ce que vérifie la règle

Chaque facture doit indiquer le SIREN du vendeur : le numéro à 9 chiffres qui identifie son entreprise. La règle vérifie qu'il est présent et qu'il compte exactement 9 chiffres, sans espace ni lettre.

Elle ne vérifie pas que ce SIREN existe, ni qu'il appartient bien au vendeur.

## Pourquoi c'est important

BR-FR-10 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

La réforme s'appuie sur des plateformes agréées par l'État et sur un annuaire tenu par l'administration, qui identifient les entreprises ([DGFiP, communiqué du 16 janvier 2026](https://presse.economie.gouv.fr/facturation-electronique-la-direction-generale-des-finances-publiques-publie-la-liste-des-101-premieres-plateformes-agreees/)). Sans SIREN, le vendeur n'est pas identifié.

## Comment corriger

1. Dans votre logiciel de facturation, ouvrez la fiche de votre entreprise et vérifiez le SIREN : 9 chiffres, sans espace.
2. Ne le confondez pas avec le SIRET, qui a 14 chiffres : le SIRET identifie un établissement, le SIREN l'entreprise entière. Les 9 premiers chiffres du SIRET sont le SIREN.
3. Si le SIREN est bien saisi et que l'erreur persiste, votre logiciel ne le transmet pas dans la facture électronique. Signalez-le à son éditeur en citant BR-FR-10.

## Causes fréquentes

- **Le SIREN n'est pas saisi** dans la fiche de l'entreprise.
- **Le SIRET est saisi à la place** du SIREN.
- **Le SIREN contient des espaces**, par exemple `012 345 674`.
- **Le logiciel ne le place pas au bon endroit** dans le fichier de la facture.

## Détails techniques

Le SIREN va dans l'identifiant d'immatriculation légale du vendeur (BT-30), avec le code de schéma `0002`, qui désigne le SIREN. Le SIRET va dans l'identifiant du vendeur (BT-29), avec le code `0009` ; il doit commencer par le SIREN (règle BR-FR-09). Dans un PDF Factur-X, la règle s'applique au fichier XML (CII) contenu dans le PDF.

## Texte officiel

> Le SIREN du vendeur (ram:ID) est obligatoire et doit être composé exactement de 9 chiffres.

BR-FR-10/BT-30, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-10_BT-30`.

## Règles voisines

- [BR-FR-09](../BR-FR-09/) : le SIRET du vendeur doit commencer par son SIREN.
- [BR-FR-11](../BR-FR-11/) : le SIREN de l'acheteur, pour les factures entre entreprises.
- [BR-FR-32](../BR-FR-32/) : tout SIREN déclaré dans la facture doit avoir 9 chiffres.
