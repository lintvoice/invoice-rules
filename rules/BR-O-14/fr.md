# Une facture hors du champ de la TVA a des frais d'une autre catégorie

La facture a une ventilation de TVA hors du champ de la TVA, et des frais au niveau du document d'une autre catégorie de TVA.

## Ce que vérifie la règle

La catégorie O couvre les opérations auxquelles aucune TVA ne s'applique, comme un service rendu à une entreprise hors de l'UE. Une facture est hors du champ de la TVA tout entière, ou pas du tout. Une opération qui porte de la TVA, ou en est exonérée, va sur une autre facture. La règle vérifie qu'une facture qui a une ventilation de TVA en O n'a pas de frais au niveau du document d'une autre catégorie de TVA.

## Pourquoi c'est important

BR-O-14 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-O-14 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Mettez les opérations hors du champ de la TVA sur une facture à part, et les autres sur une autre facture.
2. Vérifiez la catégorie de chaque ligne, remise et frais : hors du champ de la TVA, c'est O, sans taux.
3. Si votre logiciel ajoute de lui-même une autre catégorie, signalez-le à l'éditeur de votre logiciel en citant BR-O-14.

## Causes fréquentes

- **Un modèle qui écrit toujours une ventilation au taux normal**, même vide.
- **Des frais de port ou une remise laissés au taux normal** par défaut.

## Détails techniques

Le code de catégorie d'une ventilation de TVA est BT-118 ; celui d'une ligne, d'une remise et de frais est BT-151, BT-95 et BT-102. En CII, BR-O-13 et BR-O-14 font un seul test, qui refuse toute catégorie de TVA autre que O sur une remise ou des frais : elles échouent donc ensemble ; BR-O-11 et BR-O-12 en font un autre, sur les ventilations et les lignes. UBL distingue les quatre.

La facture d'exemple est hors du champ de la TVA, mais ses frais sont au taux normal, avec leur propre ventilation de TVA. BR-O-13 échoue aussi (en CII, son test est le même), ainsi que BR-O-11 et BR-O-12 sur cette ventilation.

La facture d'exemple est allemande : en France, une entreprise assujettie indique toujours son numéro de TVA sur ses factures (CGI, annexe II, art. 242 nonies A), ce que la catégorie O interdit.

## Texte officiel

> An Invoice that contains a VAT breakdown group (BG-23) with a VAT category code (BT-118) "Not subject to VAT" shall not contain Document level charges (BG-21) where Document level charge VAT category code (BT-102) is not "Not subject to VAT".

BR-O-14, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-O-13](../BR-O-13/) : une facture hors du champ de la TVA (O) ne peut pas avoir aussi une remise au niveau du document d'une autre catégorie de TVA.
- [BR-O-11](../BR-O-11/) : une facture hors du champ de la TVA (O) ne peut pas avoir aussi une ventilation de TVA d'une autre catégorie.
- [BR-O-01](../BR-O-01/) : une facture qui a une ligne, une remise ou des frais de la catégorie de TVA O (hors du champ de la TVA) doit avoir une ventilation de TVA pour cette catégorie, et une seule.
