# La livraison intracommunautaire n'indique pas le pays de livraison

La facture porte sur une livraison intracommunautaire, mais elle n'indique pas le pays de livraison.

## Ce que vérifie la règle

La catégorie K couvre les biens vendus et expédiés à une entreprise d'un autre pays de l'UE, qui y déclare la TVA. L'exonération repose sur le départ des biens vers un autre pays de l'UE : la facture dit lequel. La règle vérifie qu'une facture qui a une ventilation en K indique le code du pays de livraison (BT-80).

## Pourquoi c'est important

BR-IC-12 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-IC-12 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Indiquez l'adresse de livraison, avec son pays, même quand c'est l'adresse de l'acheteur.
2. Si l'adresse est saisie mais manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-IC-12.

## Causes fréquentes

- **Aucune adresse de livraison écrite** quand les biens partent à l'adresse même de l'acheteur.

## Détails techniques

Le code du pays de livraison est BT-80, dans l'adresse de livraison BG-15. En CII : `ram:CountryID` de `ram:ShipToTradeParty/ram:PostalTradeAddress` dans `ram:ApplicableHeaderTradeDelivery` ; en UBL : `cac:Delivery/cac:DeliveryLocation/cac:Address/cac:Country/cbc:IdentificationCode`.

La facture d'exemple est entièrement en catégorie K, et n'a pas de destinataire de livraison, donc pas de pays de livraison ; sa version corrigée a les deux, dans le pays de l'acheteur.

## Texte officiel

> In an Invoice with a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Intra-community supply" the Deliver to country code (BT-80) shall not be blank.

BR-IC-12, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-IC-11](../BR-IC-11/) : une facture de livraison intracommunautaire (K) indique la date de livraison effective, ou la période de facturation.
- [BR-IC-02](../BR-IC-02/) : une facture qui a une ligne de la catégorie de TVA K (livraison intracommunautaire) doit indiquer les numéros de TVA du vendeur et de l'acheteur.
- [BR-IC-10](../BR-IC-10/) : la ventilation de TVA de la catégorie K (livraison intracommunautaire) indique pourquoi aucune TVA n'est facturée, en texte ou sous forme de code.
