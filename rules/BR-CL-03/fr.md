# La devise d'un montant n'est pas un code valide

La devise d'un montant n'est pas un code de devise.

## Ce que vérifie la règle

Les devises s'écrivent avec leur code ISO 4217 à trois lettres : EUR pour l'euro, USD pour le dollar américain, CHF pour le franc suisse… La règle vérifie que la devise écrite à côté d'un montant est un tel code, et non un nom, un symbole ou une autre abréviation.

## Pourquoi c'est important

BR-CL-03 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-03 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez la devise dans la liste de votre logiciel, plutôt que de la saisir.
2. Vérifiez que la facture électronique écrit le code à trois lettres, EUR pour l'euro.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-03.

## Causes fréquentes

- **Un nom ou un symbole au lieu du code**, comme EURO ou €.
- **Une devise saisie à la main** dans un champ libre.

## Détails techniques

En CII, seul le total de TVA, `ram:TaxTotalAmount`, porte sa devise, dans son attribut `currencyID` : le total de TVA dans la devise de la facture (BT-110) et, s'il y en a un, dans la devise de comptabilisation de la TVA (BT-111). En UBL, chaque montant porte un `currencyID`. La liste est celle des codes à trois lettres de l'ISO 4217.

La facture d'exemple écrit sa devise `EURO` partout : dans la devise de la facture, donc BR-CL-04 échoue aussi, et dans la devise du total de TVA. Sur une facture française, la règle BR-FR-CO-12 échoue en plus, car elle demande à une facture qui n'est pas en EUR sa TVA en euros. Le profil Factur-X EN 16931 contrôle la même liste avec ses propres règles `FX-SCH-A-000595` et `FX-SCH-A-000606`, qui échouent à côté d'elle dans une facture Factur-X.

## Texte officiel

> currencyID MUST be coded using ISO code list 4217 alpha-3

BR-CL-03, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-04](../BR-CL-04/) : la devise de la facture doit être un code ISO 4217 à trois lettres, comme EUR.
- [BR-CL-05](../BR-CL-05/) : la devise dans laquelle le vendeur comptabilise la TVA doit être un code ISO 4217 à trois lettres, comme EUR.
- [BR-05](../BR-05/) : toute facture doit indiquer sa devise, avec son code à trois lettres comme EUR.
