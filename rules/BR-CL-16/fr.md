# Le moyen de paiement n'est pas un code valide

Le moyen de paiement n'est pas un code de la liste officielle.

## Ce que vérifie la règle

Une facture électronique dit comment payer par un numéro d'une liste internationale : 30 pour un virement, 58 pour un virement SEPA, 59 pour un prélèvement SEPA, 48 pour une carte bancaire… La règle vérifie que le code vient de cette liste, et non un mot comme « SEPA ».

## Pourquoi c'est important

BR-CL-16 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-16 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le moyen de paiement dans la liste de votre logiciel.
2. Vérifiez que la facture électronique en écrit le numéro, 30 pour un virement.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-16.

## Causes fréquentes

- **Un mot au lieu du code**, comme SEPA ou VIREMENT.
- **Le code propre à une banque** pour un moyen de paiement.

## Détails techniques

Le code du moyen de paiement est BT-81. En CII, c'est le `ram:TypeCode` de chaque `ram:SpecifiedTradeSettlementPaymentMeans` ; en UBL, le `cbc:PaymentMeansCode` de chaque `cac:PaymentMeans`. La liste est l'UNTDID 4461.

La facture d'exemple indique le moyen de paiement `SEPA` au lieu de `30`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000609`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Payment means in an invoice MUST be coded using UNTDID 4461 code list

BR-CL-16, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-49](../BR-49/) : quand une facture donne des instructions de paiement, elle doit dire comment payer, avec un code normalisé.
- [BR-61](../BR-61/) : quand la facture se paie par virement, elle doit indiquer le compte sur lequel payer : son IBAN, ou son numéro de compte hors du système IBAN.
