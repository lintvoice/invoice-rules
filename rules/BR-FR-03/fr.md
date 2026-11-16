# Une date de la facture n'a pas une année entre 2000 et 2099

Une date de la facture (émission, échéance, livraison, période…) n'existe pas, ou son année est hors de 2000 à 2099.

## Ce que vérifie la règle

La règle vérifie les dates de la facture :

- la date d'émission et la date d'échéance ;
- la date de fait générateur de la TVA ;
- la date de livraison ;
- le début et la fin de la période facturée, pour la facture et pour ses lignes ;
- la date d'une facture antérieure citée.

Chacune doit être une date qui existe (pas de 31 avril), avec une année de 2000 à 2099.

## Pourquoi c'est important

BR-FR-03 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Repérez la date en cause : le rapport de validation cite son code (BT-2, BT-9…), voir les détails techniques.
2. Corrigez-la dans votre logiciel, par exemple une faute de frappe sur l'année (`2206` au lieu de `2026`).
3. Si une date vide ou par défaut apparaît (`19000101`), c'est votre logiciel qui la produit : signalez-le à son éditeur en citant BR-FR-03.

## Causes fréquentes

- **Une faute de frappe sur l'année**, par exemple `2206` au lieu de `2026`.
- **Une date par défaut** écrite par le logiciel quand le champ est vide, comme `19000101`.
- **Une date qui n'existe pas**, comme un 30 février.
- **Le jour, le mois et l'année dans le mauvais ordre** après un export.

## Détails techniques

Format attendu : `AAAAMMJJ` (format 102 en CII). Dates contrôlées : BT-2 (émission), BT-7 (fait générateur de la TVA), BT-9 (échéance), BT-26 (facture antérieure), BT-72 (livraison), BT-73 et BT-74 (période facturée), et leurs équivalents sur les lignes (BT-134, BT-135, EXT-FR-FE-138, EXT-FR-FE-158). La règle lit les 8 premiers caractères et vérifie que le jour existe dans le mois, années bissextiles comprises.

## Texte officiel

> La date d’émission (udt:DateTimeString) doit contenir une année comprise entre 2000 et 2099, au format AAAAMMJJ.

BR-FR-03, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-03_BT-134`, `BR-FR-03_BT-135`, `BR-FR-03_BT-2`, `BR-FR-03_BT-26`, `BR-FR-03_BT-7`, `BR-FR-03_BT-72`, `BR-FR-03_BT-73`, `BR-FR-03_BT-74`, `BR-FR-03_BT-9`, `BR-FR-03_EXT-FR-FE-134`, `BR-FR-03_EXT-FR-FE-135`, `BR-FR-03_EXT-FR-FE-138`, `BR-FR-03_EXT-FR-FE-158`.

## Règles voisines

- [BR-FR-CO-07](../BR-FR-CO-07/) : la date d'échéance ne peut pas précéder la date d'émission.
