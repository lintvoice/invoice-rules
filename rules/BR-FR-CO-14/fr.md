# La facture d'un membre d'un groupe TVA n'a pas la mention qui le dit

Le vendeur est identifié comme membre d'un groupe TVA, mais la facture ne porte pas la mention « MEMBRE_ASSUJETTI_UNIQUE ».

## Ce que vérifie la règle

Un vendeur peut être membre d'un groupe TVA (en France, un assujetti unique). Sa facture l'identifie alors comme membre, avec l'identifiant du groupe. La règle vérifie qu'une telle facture porte aussi une mention fiscale, de code sujet TXD, dont le texte est exactement « MEMBRE_ASSUJETTI_UNIQUE ».

## Pourquoi c'est important

BR-FR-CO-14 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Si votre entreprise est membre d'un groupe TVA, vérifiez que votre logiciel de facturation ajoute à chaque facture la mention « MEMBRE_ASSUJETTI_UNIQUE », avec le code sujet TXD.
2. Vérifiez que le texte est écrit exactement ainsi, en majuscules avec des tirets bas.
3. Si votre logiciel ne sait pas l'ajouter, signalez-le à son éditeur en citant BR-FR-CO-14.

## Causes fréquentes

- **L'identifiant du groupe TVA ajouté à la fiche de l'entreprise** sans la mention qui va avec.
- **La mention écrite avec d'autres mots**, par exemple « Membre d'un assujetti unique », alors que la règle attend le texte exact.

## Détails techniques

L'identifiant du vendeur est BT-29 et son schéma BT-29-1. Le schéma 0231 désigne un membre d'un assujetti unique, et BR-FR-32 vérifie que cet identifiant a 9 chiffres. La mention est le groupe BG-1 : code sujet BT-21 `TXD`, texte BT-22 `MEMBRE_ASSUJETTI_UNIQUE`. En CII, la règle cherche un `ram:GlobalID` au `schemeID` `0231` dans `ram:SellerTradeParty`, puis un `ram:IncludedNote` de `rsm:ExchangedDocument` dont le `ram:SubjectCode` vaut `TXD` et le `ram:Content` `MEMBRE_ASSUJETTI_UNIQUE`. En UBL, elle cherche le `schemeID` `0231` dans `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID`, puis une `cbc:Note` `#TXD#MEMBRE_ASSUJETTI_UNIQUE`.

## Texte officiel

> Si le schéma d’identification du vendeur (BT-29-1) est '0231', cela signifie qu’il est membre d’un assujetti unique. Dans ce cas, une note (BG-1) avec le code sujet 'TXD' (BT-21) et le texte 'MEMBRE_ASSUJETTI_UNIQUE' (BT-22) doit être présente.

BR-FR-CO-14, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-CO-14_BT-29-1`.

## Règles voisines

- [BR-FR-CO-15](../BR-FR-CO-15/) : la facture d'un membre de groupe TVA indique le numéro de TVA du groupe.
- [BR-FR-32](../BR-FR-32/) : l'identifiant d'un membre de groupe TVA doit avoir 9 chiffres.
