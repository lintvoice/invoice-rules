# A VAT group member's invoice does not give the group's VAT number

The seller is identified as a member of a VAT group, but the invoice does not give the group's VAT number.

## What the rule checks

A seller can be a member of a VAT group (in France, an assujetti unique, a single taxable person). Its invoice then identifies it as a member, with the group's identifier, and gives the group's VAT number. The French rules put it in the seller's tax representative block. The rule checks that this block is there and holds a VAT number.

## Why it matters

BR-FR-CO-15 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. In your software, enter the VAT group as the seller's tax representative: its name, address and VAT number.
2. Check that this block is in the e-invoice, not only on the PDF.
3. If your software cannot fill it in, report it to the software's publisher, quoting BR-FR-CO-15.

## Common causes

- **The VAT group's identifier added to the company record** without its VAT number.
- **The group's VAT number written in a note** or on the PDF, but not in the tax representative block.

## Technical details

The tax representative is group BG-11: name BT-62, address BG-12, VAT identifier BT-63. In CII, when `ram:SellerTradeParty` has a `ram:GlobalID` with `schemeID` `0231`, the rule looks for `ram:SellerTaxRepresentativeTradeParty` in `ram:ApplicableHeaderTradeAgreement`, with a `ram:SpecifiedTaxRegistration/ram:ID` whose `schemeID` is `VA`. In UBL, it looks for `cbc:CompanyID` in `cac:TaxRepresentativeParty/cac:PartyTaxScheme`.

When the block is there, the EN 16931 rules BR-18, BR-19 and BR-20 also require its name, its address and its country code.

## Official text

> Si le vendeur est membre d’un assujetti unique (BT-29-1 = 0231), alors le bloc représentant fiscal (BG-11) doit être présent et contenir le numéro de TVA de l’assujetti unique (BT-63).

BR-FR-CO-15, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-CO-15_BT-29-1`.

## Related rules

- [BR-FR-CO-14](../BR-FR-CO-14/): a VAT group member's invoice carries the note MEMBRE_ASSUJETTI_UNIQUE.
- [BR-FR-32](../BR-FR-32/): a VAT group member's identifier must have 9 digits.
