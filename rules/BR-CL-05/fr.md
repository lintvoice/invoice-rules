# La devise de comptabilisation de la TVA n'est pas un code valide

La devise de comptabilisation de la TVA n'est pas un code de devise.

## Ce que vérifie la règle

Une facture en devise étrangère peut dire dans quelle devise le vendeur comptabilise la TVA. Les devises s'écrivent avec leur code ISO 4217 à trois lettres : EUR pour l'euro, USD pour le dollar américain, CHF pour le franc suisse… La règle vérifie que cette devise est un tel code, et non un nom, un symbole ou une autre abréviation.

## Pourquoi c'est important

BR-CL-05 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-05 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez la devise dans la liste de votre logiciel, plutôt que de la saisir.
2. Vérifiez que la facture électronique écrit le code à trois lettres, EUR pour l'euro.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-05.

## Causes fréquentes

- **Un nom ou un symbole au lieu du code**, comme EURO ou €.
- **Une devise saisie à la main** dans un champ libre.

## Détails techniques

Le code de devise de comptabilisation de la TVA est BT-6. En CII, c'est le `ram:TaxCurrencyCode` de `ram:ApplicableHeaderTradeSettlement` ; en UBL, `cbc:TaxCurrencyCode`. La liste est celle des codes à trois lettres de l'ISO 4217.

La facture d'exemple est en dollars américains et écrit sa devise de comptabilisation de la TVA `EURO`, comme la devise de son total de TVA dans cette devise : BR-CL-03, qui contrôle la devise d'un montant, échoue aussi. Sur une facture française, la règle BR-FR-CO-12, qui demande à une facture en devise étrangère sa TVA en euros, avec le code EUR, échoue en plus. Le profil Factur-X EN 16931 contrôle la même liste avec ses propres règles `FX-SCH-A-000607` et `FX-SCH-A-000610`, qui échouent à côté d'elle dans une facture Factur-X.

## Texte officiel

> Tax currency code MUST be coded using ISO code list 4217 alpha-3

BR-CL-05, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-53](../BR-53/) : quand la facture indique une devise de comptabilisation de la TVA, autre que sa propre devise, elle doit donner son total de TVA dans cette devise.
- [BR-CL-04](../BR-CL-04/) : la devise de la facture doit être un code ISO 4217 à trois lettres, comme EUR.
- [BR-FR-CO-12](../BR-FR-CO-12/) : quand la facture n'est pas en euros, elle doit indiquer la devise de comptabilisation de la TVA (EUR) et le total de TVA en euros.
