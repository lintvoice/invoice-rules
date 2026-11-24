# Le représentant fiscal n'a pas de numéro de TVA

La facture indique un représentant fiscal du vendeur, sans son numéro de TVA.

## Ce que vérifie la règle

Certains vendeurs agissent par un représentant fiscal, une société qui gère leur TVA dans un pays où ils ne sont pas établis. Son numéro de TVA est celui que la facture utilise pour la TVA. Quand la facture indique un représentant, la règle vérifie qu'elle donne ce numéro.

## Pourquoi c'est important

BR-56 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-56 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez le numéro de TVA du représentant fiscal dans votre logiciel.
2. Vérifiez que la facture électronique l'écrit comme un numéro de TVA, commençant par son code pays.
3. S'il manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-56.

## Causes fréquentes

- **Un représentant saisi avec ses seuls nom et adresse.**
- **Un autre numéro fiscal donné à la place**, un numéro fiscal national par exemple.

## Détails techniques

Le numéro de TVA du représentant fiscal est BT-63. En CII, la règle lit le `ram:ID` avec `schemeID="VA"` de `ram:SpecifiedTaxRegistration` dans `ram:SellerTaxRepresentativeTradeParty` ; en UBL, le `cbc:CompanyID` du `cac:PartyTaxScheme` du représentant.

La facture d'exemple indique un représentant fiscal sans numéro de TVA. Le profil Factur-X EN 16931 a ses propres règles, qui vérifient aussi la présence du numéro : dans une facture Factur-X, sa règle `FX-SCH-A-000169` échoue donc à côté de BR-56, comme dans la facture d'exemple.

## Texte officiel

> Each Seller tax representative party (BG-11) shall have a Seller tax representative VAT identifier (BT-63).

BR-56, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-18](../BR-18/) : quand le vendeur a un représentant fiscal, la facture doit en indiquer le nom.
- [BR-19](../BR-19/) : quand le vendeur a un représentant fiscal, la facture doit en indiquer l'adresse postale.
- [BR-CO-09](../BR-CO-09/) : un numéro de TVA intracommunautaire commence par les deux lettres de son pays, FR pour la France.
