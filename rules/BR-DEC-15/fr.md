# Le total de TVA en devise de comptabilisation n'est pas arrondi au centime

Le total de TVA en devise de comptabilisation a plus de 2 décimales, car il n'est pas arrondi au centime.

## Ce que vérifie la règle

Quand la facture est dans une autre devise que celle où le vendeur comptabilise la TVA, elle indique aussi son total de TVA converti dans cette devise, par exemple en euros pour une facture en dollars américains. La règle vérifie que le total de TVA dans cette devise est arrondi au centime, avec au plus 2 décimales. Par exemple, `179.48` passe et `179.482` échoue.

## Pourquoi c'est important

BR-DEC-15 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-DEC-15 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Convertissez le total de TVA au taux de change, puis arrondissez le résultat au centime.
2. Vérifiez que la facture électronique écrit ce montant arrondi au centime.
3. Si votre logiciel l'écrit avec plus de décimales, signalez-le à son éditeur en citant BR-DEC-15.

## Causes fréquentes

- **Le total de TVA converti au taux de change**, sans arrondi au centime.
- **La TVA de chaque ligne convertie une à une**, puis additionnée sans arrondi.

## Détails techniques

Le total de TVA en devise de comptabilisation est BT-111, dans le groupe BG-22. La facture doit l'indiquer quand elle nomme une devise de comptabilisation de la TVA (BT-6), qui doit être différente de la devise de la facture (BT-5), comme l'exige la règle BR-53. En CII, c'est le `ram:TaxTotalAmount` dont le `currencyID` est la devise de comptabilisation de la TVA, et la règle lit sa valeur, et non son écriture, donc `179.480` passe et `179.482` échoue. En UBL, le test des fichiers 1.3.17 compare la devise du montant à un code devise qu'il cherche sous le montant lui-même, où il n'y en a pas, donc la règle ne se déclenche pas ; la règle de syntaxe UBL UBL-DT-01, qui n'admet que 2 décimales au plus dans chaque montant, repère un tel montant.

Sur une facture française, la règle BR-FR-DEC-01 vérifie aussi ce montant. Les validateurs la signalent alors sous l'identifiant `BR-FR-DEC-01_BT-110`, et non `BR-FR-DEC-01_BT-111`, car dans le fichier de règles français la règle de BT-110 s'applique aux deux totaux de TVA avant celle de BT-111. La facture d'exemple française, en dollars américains avec sa TVA en euros, échoue donc à BR-DEC-15 et à BR-FR-DEC-01.

## Texte officiel

> The allowed maximum number of decimals for the Invoice total VAT amount in accounting currency (BT-111) is 2.

BR-DEC-15, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-13](../BR-DEC-13/) : le total de TVA, 2 décimales au plus.
- [BR-FR-CO-12](../BR-FR-CO-12/) : en France, une facture en devise étrangère indique sa TVA en euros.
- [BR-FR-DEC-01](../BR-FR-DEC-01/) : en France, la même limite pour chaque montant, avec un point comme séparateur décimal.
