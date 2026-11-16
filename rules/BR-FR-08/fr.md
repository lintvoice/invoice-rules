# Le cadre de facturation est absent ou inconnu

La facture n'indique pas son cadre de facturation, ou utilise un code absent de la liste française.

## Ce que vérifie la règle

Chaque facture doit porter un code de cadre de facturation, qui décrit sa situation. Par exemple, d'après les règles françaises elles-mêmes :

- S2, B2 ou M2 : une facture déjà payée (voir BR-FR-CO-09) ;
- S4, B4 ou M4 : une facture définitive après acompte (voir BR-FR-CO-08).

Les 20 codes admis : B1, S1, M1, B2, S2, M2, S3, B4, S4, M4, S5, S6, B7, S7, B8, S8, M8, B9, S9, M9.

## Pourquoi c'est important

BR-FR-08 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Vérifiez que votre logiciel renseigne le cadre de facturation : c'est un paramètre de la facture électronique, pas une mention imprimée.
2. Choisissez le code qui correspond à votre situation dans la liste ci-dessus ; votre plateforme agréée ou l'éditeur de votre logiciel peut vous indiquer lequel utiliser.
3. Si votre logiciel ne le propose pas, signalez-le à son éditeur en citant BR-FR-08.

## Causes fréquentes

- **Le logiciel ne renseigne pas ce champ**, que la norme européenne laisse facultatif.
- **Un code d'un autre pays ou d'un autre profil** à la place du cadre français.
- **Une faute de frappe** dans le code, ou une minuscule (`s1`).

## Détails techniques

Le cadre de facturation utilise le BT-23 de la norme EN 16931 (type de processus métier) : `ram:BusinessProcessSpecifiedDocumentContextParameter/ram:ID` en CII, `cbc:ProfileID` en UBL. En UBL, les fichiers officiels publient aussi sous `BR-FR-08_BT-151-2` un contrôle des codes de catégorie de TVA L et M qui relève de BR-FR-15.

## Texte officiel

> La valeur du mode de facturation (ram:ID) est absente ou n’est pas autorisée. Valeurs acceptées : B1, S1, M1, B2, S2, M2, S3, B4, S4, M4, S5, S6, B7, S7, B8, S8, M8, B9, S9, M9.

BR-FR-08, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-08_BT-151-2`, `BR-FR-08_BT-23`.

## Règles voisines

- [BR-FR-CO-08](../BR-FR-CO-08/) : une facture définitive après acompte ne peut pas être une facture d'acompte.
- [BR-FR-CO-09](../BR-FR-CO-09/) : une facture déjà payée doit le montrer dans ses montants.
