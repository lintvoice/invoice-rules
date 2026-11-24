# La livraison intracommunautaire n'indique pas de date de livraison

La facture porte sur une livraison intracommunautaire, mais elle n'indique ni date de livraison ni période de facturation.

## Ce que vérifie la règle

La catégorie K couvre les biens vendus et expédiés à une entreprise d'un autre pays de l'UE, qui y déclare la TVA. La date de la livraison fixe quand s'appliquent l'exonération et la TVA de l'acheteur. La règle vérifie qu'une facture qui a une ventilation en K indique la date de livraison effective (BT-72). Une période de facturation (BG-14) convient aussi, avec sa date de début (BT-73) ou de fin (BT-74).

## Pourquoi c'est important

BR-IC-11 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-IC-11 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Renseignez la date de livraison des biens, ou la période que couvre la facture.
2. Si la date est saisie mais manque dans la facture électronique, signalez-le à l'éditeur de votre logiciel en citant BR-IC-11.

## Causes fréquentes

- **Une date de livraison imprimée sur le seul bon de livraison**, pas sur la facture.

## Détails techniques

La date de livraison effective est BT-72, la période de facturation BG-14. En CII : `ram:ActualDeliverySupplyChainEvent/ram:OccurrenceDateTime` dans `ram:ApplicableHeaderTradeDelivery`, ou `ram:BillingSpecifiedPeriod` avec `ram:StartDateTime` ou `ram:EndDateTime` à côté de la ventilation ; en UBL : `cac:Delivery/cbc:ActualDeliveryDate`, ou `cac:InvoicePeriod`.

La facture d'exemple est entièrement en catégorie K, et n'a pas de date de livraison ; sa version corrigée l'indique.

## Texte officiel

> In an Invoice with a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Intra-community supply" the Actual delivery date (BT-72) or the Invoicing period (BG-14) shall not be blank.

BR-IC-11, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-IC-12](../BR-IC-12/) : une facture de livraison intracommunautaire (K) indique le pays où les biens sont livrés.
- [BR-IC-02](../BR-IC-02/) : une facture qui a une ligne de la catégorie de TVA K (livraison intracommunautaire) doit indiquer les numéros de TVA du vendeur et de l'acheteur.
- [BR-IC-10](../BR-IC-10/) : la ventilation de TVA de la catégorie K (livraison intracommunautaire) indique pourquoi aucune TVA n'est facturée, en texte ou sous forme de code.
