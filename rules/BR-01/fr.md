# La facture ne dit pas quelles règles elle suit

Le champ qui nomme les règles suivies par la facture est vide.

## Ce que vérifie la règle

Une facture électronique indique quelle spécification elle suit : la norme européenne EN 16931, ou un profil fondé sur elle, comme un profil Factur-X, XRechnung ou Peppol BIS. Le logiciel qui reçoit la facture lit ce champ pour savoir quelles règles appliquer. La règle vérifie que ce champ est rempli.

## Pourquoi c'est important

BR-01 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-01 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez quel format et quel profil produit votre logiciel, par exemple Factur-X EN 16931 ou XRechnung.
2. Vérifiez qu'il écrit l'identifiant de ce profil dans chaque facture électronique.
3. Si le champ reste vide, signalez-le à l'éditeur de votre logiciel en citant BR-01.

## Causes fréquentes

- **Un modèle** dans lequel l'identifiant est resté vide.
- **Un export construit champ par champ** qui oublie celui-ci, car rien ne le montre sur le PDF.

## Détails techniques

L'identifiant de spécification est BT-24. En CII, c'est le `ram:ID` de `ram:GuidelineSpecifiedDocumentContextParameter`, dans `rsm:ExchangedDocumentContext` ; en UBL, `cbc:CustomizationID`. Pour le profil Factur-X EN 16931, sa valeur est `urn:cen.eu:en16931:2017`.

La facture d'exemple laisse l'identifiant vide. Le contrôle propre au profil Factur-X sur cet identifiant ne lit qu'une valeur présente, donc l'exemple échoue à BR-01 seule.

## Texte officiel

> An Invoice shall have a Specification identifier (BT-24).

BR-01, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-02](../BR-02/) : toute facture doit avoir un numéro.
- [BR-03](../BR-03/) : toute facture doit indiquer sa date d'émission, écrite comme une date.
- [BR-04](../BR-04/) : toute facture doit dire de quel type de document il s'agit, une facture ou un avoir par exemple, avec un code normalisé.
