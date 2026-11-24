# Une catégorie de TVA n'est pas un code valide

Une ligne ou un taux de TVA de la facture a une catégorie de TVA qui n'est pas dans la liste officielle.

## Ce que vérifie la règle

La catégorie de TVA est un code d'une ou deux lettres. EN 16931 en garde la liste courte : S pour un taux normal, Z pour un taux zéro, E pour une exonération, AE pour une autoliquidation, K pour une livraison intracommunautaire, G pour une exportation, O pour une opération hors du champ de la TVA, L pour les Canaries, M pour Ceuta et Melilla, B pour une TVA transférée en Italie. EN 16931 n'a pas de code pour un taux réduit : sa catégorie S admet tout taux supérieur à zéro. La règle vérifie que la catégorie de chaque ligne et de chaque taux de la ventilation de TVA est l'un de ces codes.

## Pourquoi c'est important

BR-CL-18 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CL-18 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Donnez à chaque taux de TVA de votre logiciel sa catégorie : S pour tout taux supérieur à zéro, taux réduits compris.
2. Vérifiez que la facture électronique écrit l'un des codes qu'EN 16931 utilise.
3. Si votre logiciel écrit une autre valeur, signalez-le à l'éditeur de votre logiciel en citant BR-CL-18.

## Causes fréquentes

- **Un code de taux réduit**, AA, pris dans la liste UNCL 5305 complète, qu'EN 16931 n'utilise pas.
- **Une abréviation nationale** pour un taux.

## Détails techniques

La règle lit le code de catégorie de TVA de chaque ventilation de TVA (BT-118) et de chaque ligne (BT-151). En CII, c'est le `ram:CategoryCode` de chaque `ram:ApplicableTradeTax`, dans l'en-tête et dans les lignes ; en UBL, le `cbc:ID` du `cac:ClassifiedTaxCategory` de chaque ligne et du `cac:TaxCategory` de chaque `cac:TaxSubtotal`. La liste est la partie EN 16931 de l'UNCL 5305 : `AE`, `L`, `M`, `E`, `S`, `Z`, `G`, `O`, `K`, `B`.

La facture d'exemple met sa deuxième ligne au taux réduit de 5,5 %, avec la catégorie `AA` dans la ligne et dans sa ventilation de TVA ; sa version corrigée indique `S`. Sur une facture française, la règle BR-FR-15, sur les catégories admises en France, échoue aussi. Le profil Factur-X EN 16931 contrôle la même liste avec ses propres règles `FX-SCH-A-000587` et `FX-SCH-A-000619`, qui échouent à côté d'elle dans une facture Factur-X.

## Texte officiel

> Invoice tax categories MUST be coded using UNCL 5305 code list

BR-CL-18, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-47](../BR-47/) : chaque ventilation de TVA doit indiquer sa catégorie de TVA : taux normal, exonération, autoliquidation…
- [BR-CL-17](../BR-CL-17/) : la catégorie de TVA d'une remise ou de frais globaux doit être l'un des codes qu'EN 16931 utilise, comme S.
- [BR-FR-15](../BR-FR-15/) : chaque montant soumis à TVA doit utiliser une des catégories S, E, AE, K, G, O ou Z ; les catégories L et M (îles Canaries, Ceuta et Melilla) ne s'appliquent pas en France.
