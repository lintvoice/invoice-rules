# La facture n'a pas de ventilation de TVA

La facture ne contient aucune ventilation de TVA.

## Ce que vérifie la règle

La facture doit contenir au moins une ventilation de TVA : pour chaque catégorie et chaque taux, la base HT et le montant de TVA. C'est vrai même pour une facture sans TVA, exonérée par exemple : la ventilation indique alors la catégorie, la base et un montant de TVA de zéro.

## Pourquoi c'est important

BR-CO-18 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-18 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez que votre logiciel produit, pour chaque taux de TVA utilisé, une ventilation avec la base et le montant de TVA.
2. Pour une facture sans TVA, indiquez la catégorie qui s'applique (exonération, autoliquidation…) avec sa base et un montant de TVA de zéro.
3. Si votre logiciel n'envoie pas la ventilation de TVA, signalez-le à son éditeur en citant BR-CO-18.

## Causes fréquentes

- **Une facture sans TVA** pour laquelle le logiciel n'écrit aucune ventilation.
- **Une conversion depuis un autre format** qui ne portait pas la ventilation de TVA.

## Détails techniques

La ventilation de TVA est le groupe BG-23 : base (BT-116), montant (BT-117), catégorie (BT-118) et taux (BT-119). En CII, la règle cherche au moins un `ram:ApplicableTradeTax` dans `ram:ApplicableHeaderTradeSettlement` ; en UBL, au moins un `cac:TaxTotal/cac:TaxSubtotal`.

Cette page n'a pas de fichier d'exemple : une facture Factur-X sans ventilation de TVA ne passe pas non plus le schéma XML du format, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier.

## Texte officiel

> An Invoice shall at least have one VAT breakdown group (BG-23).

BR-CO-18, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-14](../BR-CO-14/) : le total de TVA doit être la somme de la TVA de chaque taux.
- [BR-CO-04](../BR-CO-04/) : chaque ligne doit indiquer sa catégorie de TVA.
