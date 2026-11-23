# La facture d'un membre d'un groupe TVA n'indique pas le numéro de TVA du groupe

Le vendeur est identifié comme membre d'un groupe TVA, mais la facture n'indique pas le numéro de TVA du groupe.

## Ce que vérifie la règle

Un vendeur peut être membre d'un groupe TVA (en France, un assujetti unique). Sa facture l'identifie alors comme membre, avec l'identifiant du groupe, et donne le numéro de TVA du groupe. Les règles françaises le placent dans le bloc du représentant fiscal du vendeur. La règle vérifie que ce bloc est présent et qu'il contient un numéro de TVA.

## Pourquoi c'est important

BR-FR-CO-15 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

## Comment corriger

1. Dans votre logiciel, renseignez le groupe TVA comme représentant fiscal du vendeur : son nom, son adresse et son numéro de TVA.
2. Vérifiez que ce bloc figure dans la facture électronique, pas seulement sur le PDF.
3. Si votre logiciel ne sait pas le renseigner, signalez-le à son éditeur en citant BR-FR-CO-15.

## Causes fréquentes

- **L'identifiant du groupe TVA ajouté à la fiche de l'entreprise** sans son numéro de TVA.
- **Le numéro de TVA du groupe écrit dans une mention** ou sur le PDF, mais pas dans le bloc du représentant fiscal.

## Détails techniques

Le représentant fiscal est le groupe BG-11 : nom BT-62, adresse BG-12, numéro de TVA BT-63. En CII, quand `ram:SellerTradeParty` a un `ram:GlobalID` au `schemeID` `0231`, la règle cherche `ram:SellerTaxRepresentativeTradeParty` dans `ram:ApplicableHeaderTradeAgreement`, avec un `ram:SpecifiedTaxRegistration/ram:ID` au `schemeID` `VA`. En UBL, elle cherche `cbc:CompanyID` dans `cac:TaxRepresentativeParty/cac:PartyTaxScheme`.

Quand le bloc est présent, les règles EN 16931 BR-18, BR-19 et BR-20 exigent aussi son nom, son adresse et son code pays.

## Texte officiel

> Si le vendeur est membre d’un assujetti unique (BT-29-1 = 0231), alors le bloc représentant fiscal (BG-11) doit être présent et contenir le numéro de TVA de l’assujetti unique (BT-63).

BR-FR-CO-15, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous l'identifiant `BR-FR-CO-15_BT-29-1`.

## Règles voisines

- [BR-FR-CO-14](../BR-FR-CO-14/) : la facture d'un membre de groupe TVA porte la mention MEMBRE_ASSUJETTI_UNIQUE.
- [BR-FR-32](../BR-FR-32/) : l'identifiant d'un membre de groupe TVA doit avoir 9 chiffres.
