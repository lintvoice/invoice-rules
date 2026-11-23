# A VAT category is not a valid code

A line or a VAT rate of the invoice has a VAT category that is not in the official list.

## What the rule checks

The VAT category is a one- or two-letter code from a list that EN 16931 keeps short: S for a standard rate, Z for a zero rate, E for an exemption, AE for a reverse charge, K for an intra-community supply, G for an export, O for outside the scope of VAT, and L, M and B for local cases. EN 16931 has no code for a lower rate: its category S accepts any rate above zero. The rule checks that the category of each line and of each rate of the VAT breakdown is one of these codes.

## Why it matters

BR-CL-18 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-18 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give each VAT rate of your software its category: S for every rate above zero, reduced rates included.
2. Check that the e-invoice writes one of the codes EN 16931 uses.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-18.

## Common causes

- **A code for a lower rate**, AA, taken from the full UNCL 5305 list, which EN 16931 does not use.
- **A national abbreviation** for a rate.

## Technical details

The rule reads the VAT category code of each VAT breakdown (BT-118) and of each line (BT-151). In CII, it is `ram:CategoryCode` of each `ram:ApplicableTradeTax`, in the header and in the lines; in UBL, `cbc:ID` of `cac:ClassifiedTaxCategory` in each line and of `cac:TaxCategory` in each `cac:TaxSubtotal`. The list is the EN 16931 part of UNCL 5305: `AE`, `L`, `M`, `E`, `S`, `Z`, `G`, `O`, `K`, `B`.

The example invoice puts its second line at a reduced rate of 7 %, with the category `AA` in the line and in its VAT breakdown; its fixed counterpart gives `S`. The Factur-X EN 16931 profile checks the same list with its own rules `FX-SCH-A-000587` and `FX-SCH-A-000619`, which fail next to it in a Factur-X invoice.

## Official text

> Invoice tax categories MUST be coded using UNCL 5305 code list

BR-CL-18, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-47](../BR-47/): each VAT breakdown must give its VAT category: standard rate, exempt, reverse charge…
- [BR-CL-17](../BR-CL-17/): the VAT category of an allowance or a charge on the whole invoice must be one of the codes EN 16931 uses, such as S.
- [BR-FR-15](../BR-FR-15/): every VAT amount must use one of the categories S, E, AE, K, G, O or Z; categories L and M (Canary Islands, Ceuta and Melilla) do not apply in France.
