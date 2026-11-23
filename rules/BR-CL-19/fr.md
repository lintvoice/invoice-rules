# Le motif d'une remise n'est pas un code valide

Le code motif d'une remise n'est pas dans la liste officielle des remises.

## Ce que vérifie la règle

Une remise sur la facture ou sur une ligne peut indiquer son motif par un code, d'une liste officielle réservée aux remises : 95 pour une remise, 100 pour un rabais exceptionnel, 64 pour un accord particulier… La règle vérifie que le code vient de cette liste, et non le texte du motif.

## Pourquoi c'est important

BR-CL-19 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-19 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le code motif de la remise dans la liste de votre logiciel, ou indiquez le motif en texte seulement.
2. Vérifiez que la facture électronique écrit le texte dans le motif et le code dans le code motif.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-19.

## Causes fréquentes

- **Le texte du motif recopié dans le code**, comme Remise.
- **Un code de frais utilisé pour une remise** : les deux listes sont différentes.

## Détails techniques

Le code motif d'une remise au niveau du document est BT-98, d'une remise sur ligne BT-140. En CII, c'est le `ram:ReasonCode` de chaque `ram:SpecifiedTradeAllowanceCharge` dont `ram:ChargeIndicator` vaut false ; en UBL, le `cbc:AllowanceChargeReasonCode` de chaque `cac:AllowanceCharge` dont `cbc:ChargeIndicator` vaut false. La liste est la partie EN 16931 de l'UNCL 5189, 19 codes ; le code de frais vient d'une autre liste, l'UNCL 7161 (règle BR-CL-20).

La facture d'exemple donne à une remise globale le code motif `Remise`, le texte de son motif. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000601`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Coded allowance reasons MUST belong to the UNCL 5189 code list

BR-CL-19, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-20](../BR-CL-20/) : quand des frais indiquent leur motif par un code, ce code doit venir de la liste officielle des frais, comme FC pour le transport.
- [BR-33](../BR-33/) : chaque remise globale doit indiquer son motif : en texte, en code, ou les deux.
- [BR-CO-21](../BR-CO-21/) : chaque remise globale doit indiquer son motif : en texte, en code, ou les deux.
