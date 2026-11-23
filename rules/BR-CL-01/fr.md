# Le type de document n'est pas un code valide

Le code qui dit de quel type de document il s'agit n'est pas dans la liste officielle.

## Ce que vérifie la règle

Une facture électronique dit de quel type de document il s'agit par un numéro d'une liste internationale : 380 pour une facture, 381 pour un avoir… La règle vérifie que le code est l'un des codes de facture ou d'avoir de cette liste, et non un mot comme « INV ».

## Pourquoi c'est important

BR-CL-01 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-01 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le type de document dans la liste de votre logiciel, plutôt que de le saisir.
2. Vérifiez que la facture électronique écrit le numéro, 380 pour une facture.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-01.

## Causes fréquentes

- **Une abréviation au lieu du code**, comme INV ou FAC.
- **Un code d'une liste ancienne ou nationale.**

## Détails techniques

Le code type de facture est BT-3. En CII, c'est le `ram:TypeCode` de `rsm:ExchangedDocument` ; en UBL, `cbc:InvoiceTypeCode` (`cbc:CreditNoteTypeCode` dans un avoir). La liste est la partie facture et avoir de l'UNTDID 1001.

La facture d'exemple indique le code type `INV`. Sur une facture française, la règle BR-FR-04, sur la liste des codes admis en France, échoue aussi. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000555`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> The document type code MUST be coded by the invoice and credit note related code lists of UNTDID 1001.

BR-CL-01, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-04](../BR-04/) : toute facture doit dire de quel type de document il s'agit, une facture ou un avoir par exemple, avec un code normalisé.
- [BR-FR-04](../BR-FR-04/) : le code du type de document doit faire partie des 16 codes admis en France, par exemple 380 pour une facture ou 381 pour un avoir.
