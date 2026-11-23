# La facture montre un numéro de carte complet

La facture indique le numéro complet d'une carte de paiement.

## Ce que vérifie la règle

Quand une facture est payée par carte, elle peut dire quelle carte, mais les normes de sécurité des paiements par carte interdisent d'en montrer le numéro complet. Le message officiel indique que les 6 premiers et les 4 derniers chiffres sont le plus qu'on puisse montrer, et la règle vérifie que le numéro écrit a 10 caractères au plus.

## Pourquoi c'est important

BR-51 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-51 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. N'écrivez que les 4 derniers chiffres de la carte dans la facture.
2. Vérifiez que votre logiciel masque le numéro de carte dans la facture électronique aussi, pas seulement sur le PDF.
3. Si il écrit le numéro complet, signalez-le à l'éditeur de votre logiciel en citant BR-51.

## Causes fréquentes

- **Un numéro masqué sur le PDF seulement**, par des étoiles, mais écrit en entier dans les données.
- **Un numéro masqué de plus de 10 caractères**, comme 12 étoiles et 4 chiffres.

## Détails techniques

Le numéro de carte de paiement est BT-87. En CII, c'est le `ram:ID` de `ram:ApplicableTradeSettlementFinancialCard` dans `ram:SpecifiedTradeSettlementPaymentMeans` ; en UBL, le `cbc:PrimaryAccountNumberID` de `cac:CardAccount`. La règle compte ses caractères : 10 au plus.

Dans les fichiers 1.3.17, la règle est bloquante en CII et un avertissement en UBL. Son message CII nomme BT-97, le motif d'une remise, là où le message UBL nomme BT-87, le numéro de carte.

La facture d'exemple est payée par carte et indique le numéro complet de la carte, donc elle échoue à BR-51 seule.

## Texte officiel

> In accordance with card payments security standards an invoice should never include a full card primary account number (BT-97). At the moment PCI Security Standards Council has defined that the first 6 digits and last 4 digits are the maximum number of digits to be shown.

BR-51, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-49](../BR-49/) : quand une facture donne des instructions de paiement, elle doit dire comment payer, avec un code normalisé.
- [BR-CL-16](../BR-CL-16/) : le moyen de paiement doit être un code de la liste officielle, comme 58 pour un virement SEPA.
