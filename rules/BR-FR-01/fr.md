# Le numéro de facture dépasse 35 caractères

Le numéro de la facture, ou celui d'une facture qu'elle cite, compte plus de 35 caractères.

## Ce que vérifie la règle

La règle limite à 35 caractères :

- le numéro de la facture ;
- le numéro d'une facture antérieure qu'elle cite, par exemple celle qu'un avoir corrige, en tête de facture ou sur une ligne.

## Pourquoi c'est important

BR-FR-01 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Dans votre logiciel de facturation, vérifiez le format de numérotation : préfixe, année et compteur compris, il doit tenir en 35 caractères.
2. Si la facture cite une facture antérieure (avoir, facture rectificative), vérifiez aussi la longueur de ce numéro.
3. Si votre logiciel ajoute un préfixe ou un suffixe à l'export, signalez-le à son éditeur en citant BR-FR-01.

## Causes fréquentes

- **Un préfixe trop long** ajouté au numéro, par exemple le nom de l'entreprise ou du service.
- **Un numéro de commande ou de dossier collé au numéro de facture.**
- **Une facture antérieure citée avec une référence trop longue**, par exemple son libellé complet au lieu de son numéro.

## Détails techniques

Le numéro de facture est le BT-1 ; celui d'une facture antérieure citée, le BT-25 en tête et l'EXT-FR-FE-136 sur une ligne (extension française). En UBL, les fichiers officiels vérifient aussi sous ce code que ces numéros n'utilisent que des caractères autorisés, ce que BR-FR-02 vérifie en CII.

## Texte officiel

> L'identifiant de facture (ram:ID) ne doit pas dépasser 35 caractères.

BR-FR-01, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-01_BT-1`, `BR-FR-01_BT-1-1`, `BR-FR-01_BT-1-2`, `BR-FR-01_BT-25`, `BR-FR-01_BT-25-1`, `BR-FR-01_BT-25-2`, `BR-FR-01_EXT-FR-FE-136`, `BR-FR-01_EXT-FR-FE-136-1`, `BR-FR-01_EXT-FR-FE-136-2`.

## Règles voisines

- [BR-FR-02](../BR-FR-02/) : les caractères autorisés dans un numéro de facture.
- [BR-FR-CO-05](../BR-FR-CO-05/) : un avoir doit citer la facture qu'il corrige.
