# Des frais hors du champ de la TVA n'ont pas de taux de TVA

Des frais hors du champ de la TVA indiquent un taux de TVA.

## Ce que vérifie la règle

La catégorie O couvre les opérations auxquelles aucune TVA ne s'applique, comme un service rendu à une entreprise hors de l'UE. La TVA ne s'applique pas : il n'y a pas de taux à indiquer. La règle vérifie que des frais au niveau du document en O n'ont aucun taux de TVA (BT-103).

## Pourquoi c'est important

BR-O-07 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-O-07 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Laissez le taux de TVA vide pour les articles hors du champ de la TVA : aucun taux, plutôt que 0 %.
2. Si votre logiciel écrit toujours un taux, signalez-le à l'éditeur de votre logiciel en citant BR-O-07.

## Causes fréquentes

- **Un logiciel qui écrit toujours un taux**, 0 % quand aucune TVA ne s'applique.

## Détails techniques

La catégorie de TVA des frais au niveau du document est BT-102, son taux BT-103. En CII : `ram:RateApplicablePercent` du `ram:CategoryTradeTax` de chaque `ram:SpecifiedTradeAllowanceCharge` dont le `ram:ChargeIndicator` vaut true ; en UBL : `cbc:Percent` du `cac:TaxCategory` de chaque `cac:AllowanceCharge` dont le `cbc:ChargeIndicator` vaut true.

La facture d'exemple est entièrement hors du champ de la TVA, et donne à ses frais un taux de 0 % ; sa version corrigée n'en donne aucun.

La facture d'exemple est allemande : en France, une entreprise assujettie indique toujours son numéro de TVA sur ses factures (CGI, annexe II, art. 242 nonies A), ce que la catégorie O interdit.

## Texte officiel

> A Document level charge (BG-21) where the VAT category code (BT-102) is "Not subject to VAT" shall not contain a Document level charge VAT rate (BT-103).

BR-O-07, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-O-05](../BR-O-05/) : une ligne hors du champ de la TVA (O) n'indique aucun taux de TVA, pas même 0 %.
- [BR-O-06](../BR-O-06/) : une remise au niveau du document hors du champ de la TVA (O) n'indique aucun taux de TVA, pas même 0 %.
- [BR-S-05](../BR-S-05/) : dans la catégorie de TVA S (taux normal), le taux de TVA d'une ligne est supérieur à zéro : un taux de 0 % relève d'une autre catégorie.
