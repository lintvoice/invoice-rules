# Le numéro de la facture antérieure manque

La facture fait référence à une facture antérieure dont le numéro est vide.

## Ce que vérifie la règle

Un avoir, une facture rectificative ou une facture de solde après acomptes fait référence aux factures qui la précèdent. Chacune est désignée par son numéro, et sa date si elle est connue. La règle vérifie que chaque référence donne le numéro.

## Pourquoi c'est important

BR-55 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-55 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Indiquez dans votre logiciel le numéro de la facture que vous rectifiez ou que l'avoir annule.
2. Vérifiez que la facture électronique l'écrit, et pas seulement le PDF.
3. Si il manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-55.

## Causes fréquentes

- **Un avoir créé sans choisir la facture qu'il annule.**
- **Une référence donnée dans une note**, en texte, plutôt que dans son propre champ.

## Détails techniques

Une référence à une facture antérieure est le groupe BG-3, son numéro BT-25 et sa date BT-26. En CII, la règle lit le `ram:IssuerAssignedID` de chaque `ram:InvoiceReferencedDocument` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, le `cbc:ID` de chaque `cac:InvoiceDocumentReference` de `cac:BillingReference`.

La facture d'exemple fait référence à une facture antérieure au numéro vide. Sur une facture française, la règle BR-FR-02, sur les caractères admis dans un numéro, échoue aussi, donc la facture d'exemple française échoue aux deux règles.

## Texte officiel

> Each Preceding Invoice reference (BG-3) shall contain a Preceding Invoice reference (BT-25).

BR-55, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-FR-CO-04](../BR-FR-CO-04/) : une facture rectificative doit citer une, et une seule, facture antérieure, avec son numéro et sa date.
- [BR-FR-02](../BR-FR-02/) : le numéro de facture ne doit contenir que des lettres, des chiffres et les signes + - _ /, sans espace.
