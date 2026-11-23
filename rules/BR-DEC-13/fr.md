# Le total de TVA n'est pas arrondi au centime

Le total de TVA a plus de 2 décimales, car il n'est pas arrondi au centime.

## Ce que vérifie la règle

Le total de TVA est la TVA de toute la facture, tous taux confondus, dans la devise de la facture. La règle vérifie que le total de TVA est arrondi au centime, avec au plus 2 décimales. Par exemple, `194.75` passe et `194.754` échoue.

## Pourquoi c'est important

BR-DEC-13 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-13 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Arrondissez la TVA de chaque taux au centime, puis additionnez ces montants arrondis pour obtenir le total de TVA.
2. Vérifiez que la facture électronique écrit le total de TVA arrondi au centime.
3. Si votre logiciel écrit le total de TVA avec plus de décimales, signalez-le à son éditeur en citant BR-DEC-13.

## Causes fréquentes

- **Un total de TVA calculé ligne par ligne à partir de montants de TVA non arrondis**, sans arrondi final.
- **Un total de TVA calculé à part de la ventilation de TVA**, qui est arrondie taux par taux.

## Détails techniques

Le total de TVA est BT-110, dans le groupe BG-22. En CII, la règle lit la valeur du `ram:TaxTotalAmount` dont le `currencyID` est la devise de la facture (BT-5), et non son écriture, donc `194.750` passe et `194.754` échoue. En UBL, le test des fichiers 1.3.17 cherche le code devise sous le montant lui-même, où il n'y en a pas, donc la règle ne se déclenche jamais. C'est la règle de syntaxe UBL UBL-DT-01, qui n'admet que 2 décimales au plus dans un montant, qui repère alors un tel montant.

Un total de TVA non arrondi au centime n'est plus la somme de la ventilation de TVA, arrondie taux par taux. BR-CO-14 échoue donc avec lui, et la facture d'exemple échoue aux deux règles. Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant, donc la facture d'exemple française échoue à ces trois règles.

## Texte officiel

> The allowed maximum number of decimals for the Invoice total VAT amount (BT-110) is 2.

BR-DEC-13, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-20](../BR-DEC-20/) : le montant de TVA d'un taux, 2 décimales au plus.
- [BR-CO-14](../BR-CO-14/) : le total de TVA doit être la somme de la TVA de chaque taux.
- [BR-DEC-15](../BR-DEC-15/) : le total de TVA en devise de comptabilisation, 2 décimales au plus.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
