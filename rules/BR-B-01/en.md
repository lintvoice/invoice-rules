# Split payment is for Italian invoices only

The invoice uses the VAT category B (split payment), but it is not a domestic Italian invoice.

## What the rule checks

Split payment is an Italian scheme. The rule checks that an invoice using category B has only Italy as country: every country code in it, the seller's and the buyer's included, is IT.

## Why it matters

BR-B-01 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-B-01 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Outside Italy, give the lines the category that fits them, such as S for the standard rate.
2. If your software chose B on its own, report it to the software's publisher, quoting BR-B-01.

## Common causes

- **Code B picked from the list of VAT categories** for another meaning than the Italian split payment.

## Technical details

The VAT categories are BT-151 (line), BT-95 (allowance), BT-102 (charge) and BT-118 (breakdown); the country codes, BT-40 for the seller and BT-55 for the buyer among them. In CII, the rule looks at every `ram:CountryID` and `ram:CategoryCode` of the invoice; in UBL, every `cbc:IdentificationCode` and the `cbc:ID` of each `cac:TaxCategory` and `cac:ClassifiedTaxCategory`.

Category B is the Italian split payment (scissione dei pagamenti): the seller charges VAT, but the buyer, a public body, pays it to the tax administration instead of the seller. The Factur-X EN 16931 profile does not accept category B at all: its rules `FX-SCH-A-000587` and `FX-SCH-A-000619` fail next to this one in a Factur-X invoice, as in the example invoice; on a French invoice, BR-FR-15, on the categories France accepts, fails too. An open issue of the EN 16931 validation artefacts proposes to remove category B and its two rules ([issue #537](https://github.com/ConnectingEurope/eInvoicing-EN16931/issues/537)).

The example invoice puts its lines in category B, between two companies outside Italy; its fixed version is the base invoice, at the standard rate.

## Official text

> An Invoice where the VAT category code (BT-151, BT-95 or BT-102) is “Split payment” shall be a domestic Italian invoice.

BR-B-01, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-B-02](../BR-B-02/): an invoice that uses the VAT category B, Italy's split payment, does not also use the standard rate, S.
- [BR-CL-18](../BR-CL-18/): the VAT category of each line and of each VAT rate must be one of the codes EN 16931 uses, such as S.
- [BR-FR-15](../BR-FR-15/): every VAT amount must use one of the categories S, E, AE, K, G, O or Z; categories L and M (Canary Islands, Ceuta and Melilla) do not apply in France.
