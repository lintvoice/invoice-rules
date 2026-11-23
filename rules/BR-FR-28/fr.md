# Une caractéristique d'article donne sa valeur à la fois en texte et en mesure

Une caractéristique d'article d'une ligne donne sa valeur à la fois en texte et en mesure, ou n'en donne aucune.

## Ce que vérifie la règle

Une ligne peut décrire l'article par des caractéristiques, par exemple « Durée : 2 jours ». Chaque caractéristique donne sa valeur d'une de deux façons : en texte (« 2 jours »), ou en quantité avec son unité de mesure (2, en jours). La règle vérifie que chaque caractéristique donne exactement l'une des deux, et qu'une mesure a son unité.

## Pourquoi c'est important

BR-FR-28 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Dans les fiches produits de votre logiciel, donnez la valeur de chaque caractéristique une seule fois : en texte, ou en quantité avec son unité.
2. Vérifiez qu'une caractéristique donnée en quantité a bien son unité de mesure.
3. Si votre logiciel envoie de lui-même les deux formes, signalez-le à son éditeur en citant BR-FR-28.

## Causes fréquentes

- **Une caractéristique saisie deux fois** dans la fiche produit, une fois en texte et une fois en quantité.
- **Une quantité sans son unité de mesure.**
- **Une caractéristique sans valeur**, restée vide dans la fiche produit.

## Détails techniques

Les caractéristiques d'article forment le groupe BG-32 : nom BT-160 (`ram:Description`), valeur BT-161 (`ram:Value`) et, dans les profils EXTENDED, valeur en mesure EXT-FR-FE-160 (`ram:ValueMeasure`) avec son unité EXT-FR-FE-161 (`@unitCode`). En UBL, la règle lit `cbc:Value` et `cbc:ValueQuantity` de chaque `cac:AdditionalItemProperty`.

Le schéma Factur-X du profil EN 16931 exige une `ram:Value` et n'a pas de `ram:ValueMeasure`, donc seule une facture d'un profil EXTENDED peut échouer à cette règle en CII. La facture d'exemple, au profil EXTENDED-CTC-FR, échoue aussi à la règle de ce profil BR-FREXT-54-2, qui dit la même chose.

## Texte officiel

> La valeur d’attribut (ram:Value) ou la valeur (ram:ValueMeasure avec unité de mesure) doivent être présents, mais pas les deux

BR-FR-28, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-28-Value`.

## Règles voisines

- [BR-FR-27](../BR-FR-27/) : une caractéristique d'article doit avoir un nom ou un code.
