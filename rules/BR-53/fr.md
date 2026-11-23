# Le total de TVA dans la devise de comptabilisation manque

La facture indique une devise de comptabilisation de la TVA, mais pas de total de TVA dans cette devise.

## Ce que vérifie la règle

Une facture en devise étrangère, en dollars américains par exemple, peut dire dans quelle devise le vendeur comptabilise la TVA, en euros par exemple, et donner son total de TVA converti dans cette devise. Quand la facture indique cette devise, la règle vérifie qu'elle donne le total de TVA dans cette devise. En CII, cette devise doit aussi être différente de celle de la facture.

## Pourquoi c'est important

BR-53 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-53 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Pour une facture en devise étrangère, indiquez le total de TVA converti dans votre devise de comptabilisation.
2. Pour une facture dans votre propre devise, n'indiquez pas de devise de comptabilisation de la TVA.
3. Si votre logiciel l'écrit quand même, signalez-le à l'éditeur de votre logiciel en citant BR-53.

## Causes fréquentes

- **La devise de comptabilisation remplie par défaut**, sur chaque facture, même dans la devise de la facture.
- **La TVA convertie sur le PDF seulement.**

## Détails techniques

Le code de devise de comptabilisation de la TVA est BT-6, le total de TVA dans cette devise BT-111. En CII, la règle cherche un `ram:TaxTotalAmount` dont le `currencyID` est le `ram:TaxCurrencyCode`, et exige que ce code soit différent de `ram:InvoiceCurrencyCode` : avec la même devise, le total de TVA en devise de comptabilisation ne se distingue pas du total de TVA en devise de la facture (BT-110), que BR-CO-15 n'admet qu'une fois. En UBL, elle cherche un `cac:TaxTotal` dont le `cbc:TaxAmount` est dans le `cbc:TaxCurrencyCode`.

La facture d'exemple indique sa propre devise comme devise de comptabilisation de la TVA, donc elle échoue à BR-53 seule.

## Texte officiel

> If the VAT accounting currency code (BT-6) is present, then the Invoice total VAT amount in accounting currency (BT-111) shall be provided.

BR-53, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-DEC-15](../BR-DEC-15/) : le total de TVA en devise de comptabilisation doit être arrondi au centime, avec au plus 2 décimales.
- [BR-CL-05](../BR-CL-05/) : la devise dans laquelle le vendeur comptabilise la TVA doit être un code ISO 4217 à trois lettres, comme EUR.
- [BR-FR-CO-12](../BR-FR-CO-12/) : quand la facture n'est pas en euros, elle doit indiquer la devise de comptabilisation de la TVA (EUR) et le total de TVA en euros.
