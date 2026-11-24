# Le total des lignes HT manque

La facture n'indique pas le total des lignes HT.

## Ce que vérifie la règle

Le total des lignes HT est la somme des montants nets des lignes de la facture, avant les remises et frais globaux. La facture électronique le donne dans ses totaux, et la règle vérifie qu'il y figure.

## Pourquoi c'est important

BR-12 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-12 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez que votre logiciel calcule ce montant pour chaque facture, même quand il est égal à un autre.
2. Vérifiez que la facture électronique l'écrit, et pas seulement le PDF.
3. S'il manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-12.

## Causes fréquentes

- **Un montant omis parce qu'il est égal à un autre**, par exemple le total des lignes HT d'une facture sans remise ni frais globaux, égal à son total HT.
- **Un export qui n'écrit qu'une partie des totaux.**

## Détails techniques

Le total des lignes HT est BT-106, dans le groupe BG-22. En CII, c'est le `ram:LineTotalAmount` de `ram:SpecifiedTradeSettlementHeaderMonetarySummation` ; en UBL, le `cbc:LineExtensionAmount` de `cac:LegalMonetaryTotal`.

Cette page n'a pas de fichier d'exemple : le [schéma XML de Factur-X EN 16931](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) exige le total des lignes HT, alors que les exemples de [invoice-examples](https://github.com/lintvoice/invoice-examples) restent valides au schéma pour n'échouer qu'à des règles métier. Le [schéma CII complet de l'UN/CEFACT (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled) le laisse en revanche facultatif : une facture CII peut donc passer ce schéma-là et échouer à la règle.

## Texte officiel

> An Invoice shall have the Sum of Invoice line net amount (BT-106).

BR-12, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-10](../BR-CO-10/) : le total des lignes HT doit être exactement la somme des montants HT de chaque ligne, au centime près.
- [BR-13](../BR-13/) : toute facture doit indiquer le total HT.
