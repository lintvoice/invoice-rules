# Le moyen de paiement manque

La facture donne des instructions de paiement sans dire comment payer.

## Ce que vérifie la règle

Une facture peut dire à l'acheteur comment payer : par virement, prélèvement, carte… Dans une facture électronique, le moyen de paiement est un code normalisé, 58 pour un virement SEPA par exemple. Quand la facture donne des instructions de paiement, la règle vérifie qu'elle donne ce code.

## Pourquoi c'est important

BR-49 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-49 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Choisissez le moyen de paiement de chaque facture dans votre logiciel, ou un moyen par défaut.
2. Vérifiez que la facture électronique en écrit le code.
3. S'il manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-49.

## Causes fréquentes

- **Des coordonnées bancaires écrites sans moyen de paiement.**
- **Un moyen de paiement saisi en texte** que le logiciel ne traduit pas en code.

## Détails techniques

Une instruction de paiement est le groupe BG-16, son code de moyen de paiement BT-81. En CII, c'est le `ram:TypeCode` de chaque `ram:SpecifiedTradeSettlementPaymentMeans` ; en UBL, le `cbc:PaymentMeansCode` de chaque `cac:PaymentMeans`. Ses codes viennent de la liste UNCL 4461, comme l'exige la règle BR-CL-16.

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige le code du moyen de paiement, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) le laisse en revanche facultatif : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> A Payment instruction (BG-16) shall specify the Payment means type code (BT-81).

BR-49, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CL-16](../BR-CL-16/) : le moyen de paiement doit être un code de la liste officielle, comme 58 pour un virement SEPA.
- [BR-50](../BR-50/) : quand la facture se paie par virement et indique un compte, l'identifiant de ce compte, comme son IBAN, doit être rempli.
- [BR-61](../BR-61/) : quand la facture se paie par virement, elle doit indiquer le compte sur lequel payer : son IBAN, ou son numéro de compte hors du système IBAN.
