# Le type de document manque

Le code qui dit de quel type de document il s'agit est vide.

## Ce que vérifie la règle

Une facture électronique dit de quel type de document il s'agit avec un code normalisé : une facture, un avoir, une facture rectificative… Le logiciel qui la reçoit traite chaque type à sa façon. La règle vérifie que ce code est présent.

## Pourquoi c'est important

BR-04 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-04 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez le type du document dans votre logiciel : facture, avoir…
2. Vérifiez que la facture électronique en écrit le code, par exemple 380 pour une facture ou 381 pour un avoir.
3. Si le code manque, signalez-le à l'éditeur de votre logiciel en citant BR-04.

## Causes fréquentes

- **Un nouveau type de document** dans le logiciel, comme une facture d'acompte, sans code associé.
- **Un modèle** dans lequel le type est resté vide.

## Détails techniques

Le code type de facture est BT-3. En CII, c'est le `ram:TypeCode` de `rsm:ExchangedDocument` ; en UBL, `cbc:InvoiceTypeCode` (`cbc:CreditNoteTypeCode` dans un avoir). Ses codes viennent de la liste UNTDID 1001, comme l'exige la règle BR-CL-01.

La facture d'exemple laisse le code vide. Un code vide n'est pas non plus dans la liste, donc BR-CL-01 échoue aussi, et l'exemple échoue aux deux règles. Sur une facture française, la règle BR-FR-04, sur la liste des codes admis en France, échoue en plus.

## Texte officiel

> An Invoice shall have an Invoice type code (BT-3).

BR-04, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-01](../BR-CL-01/) : le type de document doit être un code de la liste officielle, comme 380 pour une facture ou 381 pour un avoir.
- [BR-FR-04](../BR-FR-04/) : le code du type de document doit faire partie des 16 codes admis en France, par exemple 380 pour une facture ou 381 pour un avoir.
