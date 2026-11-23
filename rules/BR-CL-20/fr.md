# Le motif de frais n'est pas un code valide

Le code motif de frais n'est pas dans la liste officielle des frais.

## Ce que vérifie la règle

Des frais sur la facture ou sur une ligne peuvent indiquer leur motif par un code, d'une liste officielle réservée aux frais : FC pour le transport, ABL pour un emballage supplémentaire… La règle vérifie que le code vient de cette liste, et non le texte du motif.

## Pourquoi c'est important

BR-CL-20 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-20 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le code motif des frais dans la liste de votre logiciel, ou indiquez le motif en texte seulement.
2. Vérifiez que la facture électronique écrit le texte dans le motif et le code dans le code motif.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-20.

## Causes fréquentes

- **Le texte du motif recopié dans le code**, comme Frais de port.
- **Un code de remise utilisé pour des frais** : les deux listes sont différentes.

## Détails techniques

Le code motif de frais au niveau du document est BT-105, de frais sur ligne BT-145. En CII, c'est le `ram:ReasonCode` de chaque `ram:SpecifiedTradeAllowanceCharge` dont `ram:ChargeIndicator` vaut true ; en UBL, le `cbc:AllowanceChargeReasonCode` de chaque `cac:AllowanceCharge` dont `cbc:ChargeIndicator` vaut true. La liste est l'UNCL 7161 ; le code de remise vient d'une autre liste, l'UNCL 5189 (règle BR-CL-19).

La facture d'exemple donne à des frais globaux le code motif `Frais de port`, le texte de leur motif. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000604`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Coded charge reasons MUST belong to the UNCL 7161 code list

BR-CL-20, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-19](../BR-CL-19/) : quand une remise indique son motif par un code, ce code doit venir de la liste officielle des remises, comme 95 pour une remise.
- [BR-38](../BR-38/) : les frais globaux doivent indiquer leur motif : en texte, en code, ou les deux.
- [BR-CO-22](../BR-CO-22/) : les frais globaux doivent indiquer leur motif : en texte, en code, ou les deux.
