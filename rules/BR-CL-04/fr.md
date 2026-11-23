# La devise de la facture n'est pas un code valide

La devise de la facture n'est pas un code de devise.

## Ce que vérifie la règle

Les devises s'écrivent avec leur code ISO 4217 à trois lettres : EUR pour l'euro, USD pour le dollar américain, CHF pour le franc suisse… La règle vérifie que la devise de la facture est un tel code, et non un nom, un symbole ou une autre abréviation.

## Pourquoi c'est important

BR-CL-04 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-04 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez la devise dans la liste de votre logiciel, plutôt que de la saisir.
2. Vérifiez que la facture électronique écrit le code à trois lettres, EUR pour l'euro.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-04.

## Causes fréquentes

- **Un nom ou un symbole au lieu du code**, comme EURO ou €.
- **Une devise saisie à la main** dans un champ libre.

## Détails techniques

Le code devise de la facture est BT-5. En CII, c'est le `ram:InvoiceCurrencyCode` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, `cbc:DocumentCurrencyCode`. La liste est celle des codes à trois lettres de l'ISO 4217.

La facture d'exemple écrit sa devise `EURO`, dans la devise de la facture et dans la devise du total de TVA, donc BR-CL-03, qui contrôle la devise d'un montant, échoue aussi. Sur une facture française, la règle BR-FR-CO-12 échoue en plus, car elle demande à une facture qui n'est pas en EUR sa TVA en euros. Le profil Factur-X EN 16931 contrôle la même liste avec ses propres règles `FX-SCH-A-000595` et `FX-SCH-A-000606`, qui échouent à côté d'elle dans une facture Factur-X.

## Texte officiel

> Invoice currency code MUST be coded using ISO code list 4217 alpha-3

BR-CL-04, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-05](../BR-05/) : toute facture doit indiquer sa devise, avec son code à trois lettres comme EUR.
- [BR-CL-03](../BR-CL-03/) : la devise écrite à côté d'un montant doit être un code ISO 4217 à trois lettres, comme EUR.
- [BR-CL-05](../BR-CL-05/) : la devise dans laquelle le vendeur comptabilise la TVA doit être un code ISO 4217 à trois lettres, comme EUR.
