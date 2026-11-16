# Le type d'opération (note BAR) a une valeur non admise

La note codée BAR a une valeur hors de la liste admise.

## Ce que vérifie la règle

Une note codée BAR indique comment la facture doit être traitée, par exemple B2B pour une facture entre entreprises ou B2C pour une facture à un particulier. Elle ne peut valoir que : B2B, B2BINT, B2C, B2CINT, OUTOFSCOPE ou ARCHIVEONLY. Toute autre valeur, faute de frappe ou minuscules comprises, est refusée.

## Pourquoi c'est important

BR-FR-20 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez la valeur de la note BAR envoyée par votre logiciel.
2. Corrigez-la avec une valeur de la liste, en majuscules, sans espace.
3. Si vous ne savez pas laquelle s'applique, demandez à votre plateforme agréée ou à l'éditeur de votre logiciel.

## Causes fréquentes

- **Des minuscules** (`b2b`).
- **Un espace ou un tiret** (`B2B ` ou `B-2-B`).
- **Une valeur venue d'un autre système**, comme `BUSINESS`.

## Détails techniques

Une note (BG-1) dont le code de sujet BT-21 vaut `BAR` ; la valeur est le texte de la note BT-22.

## Texte officiel

> Lorsqu’une note a pour code sujet « BAR » (BT-21), la valeur associée (BT-22, contenu de la note) doit être l’une des suivantes : B2B, B2BINT, B2C, B2CINT, OUTOFSCOPE, ARCHIVEONLY.

BR-FR-20, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-20_BT-21`.

## Règles voisines

- [BR-FR-31](../BR-FR-31/) : une seule note BAR par facture.
- [BR-FR-11](../BR-FR-11/) : une facture B2B exige le SIREN de l'acheteur.
- [BR-FR-21](../BR-FR-21/) : sur une facture B2B, l'adresse électronique de l'acheteur commence par son SIREN.
