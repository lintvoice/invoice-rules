# La devise de la facture manque

La devise de la facture est vide.

## Ce que vérifie la règle

Tous les montants d'une facture sont dans une seule devise, que la facture électronique indique une fois, avec son code à trois lettres : EUR pour l'euro, CHF pour le franc suisse… La règle vérifie que la facture l'indique.

## Pourquoi c'est important

BR-05 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-05 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Indiquez la devise de chaque facture, ou une devise par défaut, dans votre logiciel.
2. Vérifiez que la facture électronique en écrit le code à trois lettres.
3. Si elle reste vide, signalez-le à l'éditeur de votre logiciel en citant BR-05.

## Causes fréquentes

- **Aucune devise par défaut** dans le logiciel, pour les factures dans la devise du pays.
- **Une devise affichée en symbole**, €, que le logiciel ne traduit pas en code.

## Détails techniques

Le code devise de la facture est BT-5. En CII, c'est le `ram:InvoiceCurrencyCode` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, `cbc:DocumentCurrencyCode`. Son code vient de l'ISO 4217, comme l'exige la règle BR-CL-04.

La facture d'exemple laisse la devise vide, comme la devise de son total de TVA (`currencyID` de `ram:TaxTotalAmount`). Un code vide n'est pas dans l'ISO 4217, donc BR-CL-04 et BR-CL-03, qui contrôle la devise d'un montant, échouent aussi : l'exemple échoue aux trois règles. Sur une facture française, la règle BR-FR-CO-12 échoue en plus, car elle demande à une facture qui n'est pas en EUR sa TVA en euros.

## Texte officiel

> An Invoice shall have an Invoice currency code (BT-5).

BR-05, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-04](../BR-CL-04/) : la devise de la facture doit être un code ISO 4217 à trois lettres, comme EUR.
- [BR-CL-03](../BR-CL-03/) : la devise écrite à côté d'un montant doit être un code ISO 4217 à trois lettres, comme EUR.
- [BR-FR-CO-12](../BR-FR-CO-12/) : quand la facture n'est pas en euros, elle doit indiquer la devise de comptabilisation de la TVA (EUR) et le total de TVA en euros.
