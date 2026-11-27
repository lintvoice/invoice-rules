# Split payment and the standard rate on one invoice

The invoice uses both the VAT category B (split payment) and the category S (standard rate).

## What the rule checks

In Italy's split payment, the buyer pays the VAT to the tax administration; with the standard rate, it pays the VAT to the seller. The two do not mix on one invoice. The rule checks that an invoice with category B has no line, allowance, charge or breakdown in S.

## Why it matters

BR-B-02 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-B-02 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Under split payment, give every line, allowance and charge the category B.
2. Outside Italy, or outside split payment, do not use B at all.
3. If your software mixes the two, report it to the software's publisher, quoting BR-B-02.

## Common causes

- **One line switched to B** while the others stay at the standard rate.

## Technical details

The VAT categories are BT-151 (line), BT-95 (allowance), BT-102 (charge) and BT-118 (breakdown). In CII, the rule looks at every `ram:CategoryCode` of the invoice; in UBL, at the `cbc:ID` of each `cac:TaxCategory` and `cac:ClassifiedTaxCategory`.

Category B is the Italian split payment (scissione dei pagamenti): the seller charges VAT, but the buyer, a public body, pays it to the tax administration instead of the seller. The Factur-X EN 16931 profile does not accept category B at all: its rules `FX-SCH-A-000587` and `FX-SCH-A-000619` fail next to this one in a Factur-X invoice, as in the example invoice; on a French invoice, BR-FR-15, on the categories France accepts, fails too. An open issue of the EN 16931 validation artefacts proposes to remove category B and its two rules ([issue #537](https://github.com/ConnectingEurope/eInvoicing-EN16931/issues/537)).

The example invoice puts its second line in B and keeps the first at the standard rate; as it is not an Italian invoice, BR-B-01 fails too.

## Official text

> An Invoice that contains an Invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is “Split payment" shall not contain an invoice line (BG-25), a Document level allowance (BG-20) or a Document level charge (BG-21) where the VAT category code (BT-151, BT-95 or BT-102) is “Standard rated”.

BR-B-02, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-B-01](../BR-B-01/): the VAT category B, Italy's split payment, belongs on an invoice whose parties and addresses are all in Italy.
- [BR-S-01](../BR-S-01/): an invoice with a line, an allowance or a charge in the VAT category S (standard rate) must have a VAT breakdown for it.
- [BR-CL-18](../BR-CL-18/): the VAT category of each line and of each VAT rate must be one of the codes EN 16931 uses, such as S.
