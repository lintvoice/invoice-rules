# Le net à payer n'a ni date d'échéance ni conditions de paiement

La facture laisse un montant à payer, mais n'indique ni sa date d'échéance ni ses conditions de paiement.

## Ce que vérifie la règle

Quand la facture laisse un montant à payer, elle doit dire quand ou comment le régler : par une date d'échéance, par des conditions de paiement (par exemple « 30 jours fin de mois »), ou les deux. Une facture déjà réglée, dont le net à payer est nul, n'est pas concernée.

## Pourquoi c'est important

BR-CO-25 est une règle de la norme européenne de facturation électronique, EN 16931. Depuis leur version 1.3.16 (avril 2026), les fichiers de validation publiés pour cette norme ne la vérifient plus ([notes de version](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.16)) ; une demande publique ouverte le 18 octobre 2026 conteste ce retrait ([#541](https://github.com/ConnectingEurope/eInvoicing-EN16931/issues/541)). La règle reste appliquée, et bloquante, par les règles du profil EXTENDED-CTC-FR, l'un des profils que la réforme française admet, ainsi que par les règles du profil Factur-X EXTENDED et par la spécification Peppol BIS Billing ([règle BR-CO-25](https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/BR-CO-25/)).

Quelle que soit la règle vérifiée, le Code de commerce exige que la facture mentionne la date à laquelle le règlement doit intervenir ([article L441-9](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414397)).

## Comment corriger

1. Indiquez la date d'échéance de la facture, ses conditions de paiement, ou les deux.
2. Vérifiez que ces informations sont envoyées dans la facture électronique, et pas seulement imprimées sur le PDF.
3. Si votre logiciel ne les envoie pas, signalez-le à son éditeur en citant BR-CO-25.

## Causes fréquentes

- **Des conditions de paiement imprimées sur le PDF** mais absentes des données de la facture électronique.
- **Un modèle de facture sans échéance** dans le logiciel de facturation.

## Détails techniques

Le net à payer est BT-115, la date d'échéance BT-9 et les conditions de paiement BT-20. En CII, la règle cherche `ram:DueDateDateTime` ou `ram:Description` dans `ram:SpecifiedTradePaymentTerms` quand `ram:DuePayableAmount` est positif ; en UBL, `cbc:DueDate` ou `cac:PaymentTerms/cbc:Note` quand `cac:LegalMonetaryTotal/cbc:PayableAmount` est positif. En UBL, elle ne vise que les factures, pas les avoirs ; en CII, tous les types de documents.

La facture d'exemple est au profil EXTENDED-CTC-FR, car une facture au profil EN 16931 n'est plus vérifiée sur cette règle par les fichiers de validation actuels.

## Texte officiel

> In case the Amount due for payment (BT-115) is positive, either the Payment due date (BT-9) or the Payment terms (BT-20) shall be present.

BR-CO-25, [règles EXTENDED-CTC-FR de France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/blob/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/EXTENDED-CTC-FR/schematron/EXTENDED-CTC-FR-CII.sch), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-16](../BR-CO-16/) : le net à payer doit être le total TTC, moins ce qui est déjà payé, plus l'arrondi.
- [BR-FR-CO-09](../BR-FR-CO-09/) : une facture déjà payée doit indiquer sa date d'échéance et un net à payer nul.
- [BR-FR-05](../BR-FR-05/) : la facture doit porter les mentions de paiement (indemnité de recouvrement, pénalités de retard, escompte).
