# Le motif d'exonération n'est pas un code valide

Le code qui indique le motif d'une exonération de TVA n'est pas dans la liste VATEX.

## Ce que vérifie la règle

Quand aucune TVA n'est facturée (une exonération, une autoliquidation, une exportation…), la ventilation de TVA en indique le motif : en texte, par un code, ou les deux. Les codes viennent de la liste VATEX. Chacun nomme l'article de la directive TVA de l'UE ou de la loi nationale qui fonde le cas : VATEX-EU-132 pour les exonérations de l'article 132 de la directive, VATEX-EU-132-1I pour l'enseignement et la formation professionnelle… La règle vérifie que le code est l'un de ceux de la liste.

## Pourquoi c'est important

BR-CL-22 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-22 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le code motif d'exonération dans la liste de votre logiciel, ou indiquez le motif en texte seulement.
2. Vérifiez que la facture électronique écrit le code en entier, comme dans la liste.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-22.

## Causes fréquentes

- **Un code tronqué**, VATEX-EU-132-1 là où la liste a VATEX-EU-132 et VATEX-EU-132-1A à VATEX-EU-132-1Q.
- **L'article de loi écrit au lieu du code.**

## Détails techniques

Le code motif d'exonération de TVA est BT-121. En CII, c'est le `ram:ExemptionReasonCode` de chaque `ram:ApplicableTradeTax` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, le `cbc:TaxExemptionReasonCode` de chaque `cac:TaxCategory` de la ventilation de TVA. La liste est la liste VATEX de la Commission européenne, version 9 dans les fichiers 1.3.17.

La facture d'exemple a une ligne exonérée dont la ventilation de TVA indique le code `VATEX-EU-132-1`, tronqué. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000589`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Tax exemption reason code identifier scheme identifier MUST belong to the CEF VATEX code list

BR-CL-22, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-E-10](../BR-E-10/) : quand une partie de la facture est exonérée de TVA, la ventilation de TVA doit en donner le motif, en texte ou sous forme de code.
