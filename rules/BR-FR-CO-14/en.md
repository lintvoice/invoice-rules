# A VAT group member's invoice lacks the note that says so

The seller is identified as a member of a VAT group, but the invoice does not carry the note MEMBRE_ASSUJETTI_UNIQUE.

## What the rule checks

A seller can be a member of a VAT group (in France, an assujetti unique, a single taxable person). Its invoice then identifies it as a member, with the group's identifier. The rule checks that such an invoice also carries a tax note, with the subject code TXD, whose text is exactly MEMBRE_ASSUJETTI_UNIQUE.

## Why it matters

BR-FR-CO-14 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. If your company is a member of a VAT group, check that your invoicing software adds the note MEMBRE_ASSUJETTI_UNIQUE, with the subject code TXD, to every invoice.
2. Check that the text is written exactly so, in capitals with underscores.
3. If your software cannot add it, report it to the software's publisher, quoting BR-FR-CO-14.

## Common causes

- **The VAT group's identifier added to the company record** without the note that goes with it.
- **The note written in other words**, for example "Member of a VAT group". The rule wants the exact text.

## Technical details

The seller's identifier is BT-29 and its scheme BT-29-1. The scheme 0231 stands for a member of a single taxable person, and BR-FR-32 checks that this identifier has 9 digits. The note is group BG-1: subject code BT-21 `TXD`, text BT-22 `MEMBRE_ASSUJETTI_UNIQUE`. In CII, the rule looks for a `ram:GlobalID` with `schemeID` `0231` in `ram:SellerTradeParty`, then for a `ram:IncludedNote` of `rsm:ExchangedDocument` whose `ram:SubjectCode` is `TXD` and `ram:Content` `MEMBRE_ASSUJETTI_UNIQUE`. In UBL, it looks for the `schemeID` `0231` in `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID`, then for a `cbc:Note` `#TXD#MEMBRE_ASSUJETTI_UNIQUE`.

## Official text

> Si le schéma d’identification du vendeur (BT-29-1) est '0231', cela signifie qu’il est membre d’un assujetti unique. Dans ce cas, une note (BG-1) avec le code sujet 'TXD' (BT-21) et le texte 'MEMBRE_ASSUJETTI_UNIQUE' (BT-22) doit être présente.

BR-FR-CO-14, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-CO-14_BT-29-1`.

## Related rules

- [BR-FR-CO-15](../BR-FR-CO-15/): a VAT group member's invoice gives the group's VAT number.
- [BR-FR-32](../BR-FR-32/): a VAT group member's identifier must have 9 digits.
