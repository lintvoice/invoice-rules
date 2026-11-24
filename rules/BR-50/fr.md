# Le compte à payer est vide

La facture indique un compte pour le virement, avec un identifiant vide.

## Ce que vérifie la règle

Pour un virement, la facture indique le compte sur lequel payer, par son IBAN ou, hors du système IBAN, son numéro de compte. Quand la facture donne un tel compte, la règle vérifie que son identifiant est rempli.

## Pourquoi c'est important

BR-50 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-50 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez l'IBAN de votre compte bancaire dans les paramètres de votre logiciel.
2. Vérifiez que la facture électronique l'écrit en entier.
3. S'il reste vide, signalez-le à l'éditeur de votre logiciel en citant BR-50.

## Causes fréquentes

- **Des coordonnées bancaires paramétrées sans l'IBAN**, avec le seul nom de la banque.
- **Un IBAN affiché sur le PDF depuis une image** du RIB.

## Détails techniques

L'identifiant du compte de paiement est BT-84. En CII, la règle lit `ram:IBANID` et `ram:ProprietaryID` de `ram:PayeePartyCreditorFinancialAccount`, dans un `ram:SpecifiedTradeSettlementPaymentMeans` dont le `ram:TypeCode` vaut 30 ou 58, virement et virement SEPA ; en UBL, le `cbc:ID` de `cac:PayeeFinancialAccount` avec les mêmes codes.

La facture d'exemple indique un compte dont l'IBAN est vide, donc elle échoue à BR-50 seule.

## Texte officiel

> A Payment account identifier (BT-84) shall be present if Credit transfer (BG-16) information is provided in the Invoice.

BR-50, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-61](../BR-61/) : quand la facture se paie par virement, elle doit indiquer le compte sur lequel payer : son IBAN, ou son numéro de compte hors du système IBAN.
- [BR-49](../BR-49/) : quand une facture donne des instructions de paiement, elle doit dire comment payer, avec un code normalisé.
