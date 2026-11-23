# Une unité de mesure n'est pas un code valide

Une unité de mesure de la facture n'est pas un code de la liste officielle.

## Ce que vérifie la règle

Une facture électronique écrit chaque unité de mesure par un code d'une liste des Nations unies : C62 pour une unité, H87 pour une pièce, HUR pour une heure, DAY pour un jour, KGM pour un kilogramme… La règle vérifie que chaque unité est un code de cette liste, et non une abréviation comme « pcs ».

## Pourquoi c'est important

BR-CL-23 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-23 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Associez chaque unité de votre logiciel à son code de la liste : « unité » à C62, « heure » à HUR.
2. Vérifiez que la facture électronique écrit le code, et non le nom court de l'unité.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-23.

## Causes fréquentes

- **Une abréviation locale au lieu du code**, comme U, pcs ou Stk.
- **Une unité créée dans le catalogue** sans code associé.

## Détails techniques

L'unité de mesure de la quantité facturée est BT-130, celle de la quantité de base du prix BT-150. En CII, c'est le `unitCode` de `ram:BilledQuantity` et de `ram:BasisQuantity` ; en UBL, le `unitCode` de `cbc:InvoicedQuantity` (`cbc:CreditedQuantity` dans un avoir) et de `cbc:BaseQuantity`. La liste est la recommandation 20 de la CEE-ONU, avec l'extension de la recommandation 21.

La facture d'exemple donne à sa première ligne l'unité `U`, une abréviation française d'unité, au lieu de `C62`. Le profil Factur-X EN 16931 contrôle la même liste avec sa propre règle `FX-SCH-A-000613`, qui échoue à côté d'elle dans une facture Factur-X.

## Texte officiel

> Unit code MUST be coded according to the UN/ECE Recommendation 20 with Rec 21 extension

BR-CL-23, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-23](../BR-23/) : chaque quantité facturée doit indiquer son unité de mesure (unité, heure, jour…), sous forme de code normalisé.
