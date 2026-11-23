# Un virement n'indique pas de compte

La facture se paie par virement, mais n'indique pas d'identifiant de compte.

## Ce que vérifie la règle

Pour un virement, SEPA, national ou international, l'acheteur a besoin du compte sur lequel payer. La règle vérifie que la facture l'indique, par son IBAN ou par un autre numéro de compte.

## Pourquoi c'est important

BR-61 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-61 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez l'IBAN de votre compte bancaire dans les paramètres de votre logiciel.
2. Si vous êtes payé par un autre moyen qu'un virement, choisissez plutôt ce moyen de paiement.
3. Si le compte manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-61.

## Causes fréquentes

- **Un compte donné par le seul nom de son titulaire.**
- **Le virement choisi par défaut** pour chaque facture, même sans compte paramétré.

## Détails techniques

L'identifiant du compte de paiement est BT-84, le code du moyen de paiement BT-81. En CII, la règle cherche `ram:IBANID` ou `ram:ProprietaryID` dans `ram:PayeePartyCreditorFinancialAccount`, dans un `ram:SpecifiedTradeSettlementPaymentMeans` dont le `ram:TypeCode` vaut 30 ou 58, virement et virement SEPA ; en UBL, le `cbc:ID` de `cac:PayeeFinancialAccount`.

La facture d'exemple donne le nom du compte mais pas d'IBAN. La règle BR-50, qui exige le même identifiant quand un compte est indiqué, et la règle de syntaxe CII `CII-SR-470`, qui exige un IBAN ou un autre numéro de compte, échouent aussi : l'exemple échoue aux trois règles.

## Texte officiel

> If the Payment means type code (BT-81) means SEPA credit transfer, Local credit transfer or Non-SEPA international credit transfer, the Payment account identifier (BT-84) shall be present.

BR-61, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-50](../BR-50/) : quand la facture se paie par virement et indique un compte, l'identifiant de ce compte, comme son IBAN, doit être rempli.
- [BR-49](../BR-49/) : quand une facture donne des instructions de paiement, elle doit dire comment payer, avec un code normalisé.
- [BR-CL-16](../BR-CL-16/) : le moyen de paiement doit être un code de la liste officielle, comme 58 pour un virement SEPA.
