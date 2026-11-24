# An allowance's or a charge's VAT category is not a valid code

An allowance or a charge on the whole invoice has a VAT category that is not in the official list.

## What the rule checks

The VAT category is a code of one or two letters. EN 16931 keeps the list short: S for a standard rate, Z for a zero rate, E for an exemption, AE for a reverse charge, K for an intra-community supply, G for an export, O for outside the scope of VAT, L for the Canary Islands, M for Ceuta and Melilla, B for a VAT transferred in Italy. EN 16931 has no code for a lower rate: its category S accepts any rate above zero. The rule checks that the category of each allowance and charge on the whole invoice is one of these codes.

## Why it matters

BR-CL-17 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-17 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give each allowance and charge the VAT category of what it applies to, S for a standard rate.
2. Check that the e-invoice writes the category, rather than the tax type (VAT) or the rate.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-17.

## Common causes

- **The tax type instead of the category**, VAT where S is expected.
- **The rate written as a category**, such as 19.

## Technical details

The VAT category code of a document level allowance is BT-95, of a charge BT-102. In CII, it is `ram:CategoryCode` of the `ram:CategoryTradeTax` of each `ram:SpecifiedTradeAllowanceCharge`; in UBL, `cbc:ID` of the `cac:TaxCategory` of each `cac:AllowanceCharge`. The list is the EN 16931 part of UNCL 5305: `AE`, `L`, `M`, `E`, `S`, `Z`, `G`, `O`, `K`, `B`.

The example invoice gives an allowance the category `VAT`, the tax type. The allowance then lowers no VAT breakdown, so the taxable amount of the standard rate no longer matches its lines minus its allowances, and BR-S-08 fails too. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000599`, which fails next to it in a Factur-X invoice.

## Official text

> Invoice tax categories MUST be coded using UNCL 5305 code list

BR-CL-17, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-32](../BR-32/): each allowance on the whole invoice must give its VAT category, so that the VAT breakdown can take it into account.
- [BR-37](../BR-37/): each charge on the whole invoice must give its VAT category, so that the VAT breakdown can take it into account.
- [BR-CL-18](../BR-CL-18/): the VAT category of each line and of each VAT rate must be one of the codes EN 16931 uses, such as S.
- [BR-FR-15](../BR-FR-15/): every VAT amount must use one of the categories S, E, AE, K, G, O or Z; categories L and M (Canary Islands, Ceuta and Melilla) do not apply in France.
