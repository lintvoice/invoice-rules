# Le numéro de facture contient un caractère non autorisé

Le numéro de la facture, ou celui d'une facture qu'elle cite, contient un espace ou un caractère autre que lettres, chiffres et + - _ /.

## Ce que vérifie la règle

Le numéro de la facture, et celui de toute facture antérieure citée, ne peuvent contenir que :

- des lettres sans accent et des chiffres ;
- les signes `+`, `-`, `_` et `/`.

Les espaces, les points, les lettres accentuées et les autres signes sont refusés.

## Pourquoi c'est important

BR-FR-02 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Dans votre logiciel, retirez de la numérotation les espaces, les points, les accents et les autres signes : gardez lettres, chiffres et + - _ /.
2. Par exemple, `FA 2026.001` devient `FA-2026-001`.
3. Pour un avoir ou une facture rectificative, citez la facture d'origine avec un numéro au même format.

## Causes fréquentes

- **Un espace dans le numéro**, par exemple `FA 2026-001`.
- **Un point ou un deux-points** comme séparateur.
- **Une lettre accentuée** dans un préfixe.
- **Un numéro saisi à la main** avec des signes que le logiciel n'aurait pas mis.

## Détails techniques

Vérifié sur le numéro de facture (BT-1), le numéro d'une facture antérieure citée (BT-25) et le même numéro sur une ligne (EXT-FR-FE-136). Le format accepté correspond à l'expression `^[A-Za-z0-9+\-_/]+$`. En UBL, les fichiers officiels publient ce contrôle sous BR-FR-01.

## Texte officiel

> L'identifiant de facture (ram:ID) contient des caractères non autorisés.

BR-FR-02, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-02_BT-1`, `BR-FR-02_BT-25`, `BR-FR-02_EXT-FR-FE-136`.

## Règles voisines

- [BR-FR-01](../BR-FR-01/) : un numéro de facture compte au plus 35 caractères.
