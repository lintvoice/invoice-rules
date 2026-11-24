# Une ligne hors du champ de la TVA n'a pas de taux de TVA

Une ligne hors du champ de la TVA indique un taux de TVA.

## Ce que vérifie la règle

La catégorie O couvre les opérations auxquelles aucune TVA ne s'applique, comme un service rendu à une entreprise hors de l'UE. La TVA ne s'applique pas : il n'y a pas de taux à indiquer. La règle vérifie qu'une ligne en O n'a aucun taux de TVA (BT-152).

## Pourquoi c'est important

BR-O-05 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-O-05 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Laissez le taux de TVA vide pour les articles hors du champ de la TVA : aucun taux, plutôt que 0 %.
2. Si votre logiciel écrit toujours un taux, signalez-le à l'éditeur de votre logiciel en citant BR-O-05.

## Causes fréquentes

- **Un logiciel qui écrit toujours un taux**, 0 % quand aucune TVA ne s'applique.

## Détails techniques

La catégorie de TVA d'une ligne est BT-151, son taux BT-152. En CII : `ram:RateApplicablePercent` du `ram:ApplicableTradeTax` ; en UBL : `cbc:Percent` de `cac:Item/cac:ClassifiedTaxCategory`.

La facture d'exemple est entièrement hors du champ de la TVA, et donne à sa première ligne un taux de 0 % ; sa version corrigée n'en donne aucun.

La facture d'exemple est allemande : en France, une entreprise assujettie indique toujours son numéro de TVA sur ses factures (CGI, annexe II, art. 242 nonies A), ce que la catégorie O interdit.

## Texte officiel

> An Invoice line (BG-25) where the VAT category code (BT-151) is "Not subject to VAT" shall not contain an Invoiced item VAT rate (BT-152).

BR-O-05, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-O-06](../BR-O-06/) : une remise au niveau du document hors du champ de la TVA (O) n'indique aucun taux de TVA, pas même 0 %.
- [BR-O-07](../BR-O-07/) : des frais au niveau du document hors du champ de la TVA (O) n'indiquent aucun taux de TVA, pas même 0 %.
- [BR-S-05](../BR-S-05/) : dans la catégorie de TVA S (taux normal), le taux de TVA d'une ligne est supérieur à zéro : un taux de 0 % relève d'une autre catégorie.
