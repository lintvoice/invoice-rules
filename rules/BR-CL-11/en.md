# A registration number's kind is not a valid code

The code that says which register a legal registration number comes from is not in the official list.

## What the rule checks

Identifiers come from many registers: a GLN, a SIRET, a DUNS number… A four-digit code from the ISO 6523 list says which register an identifier comes from: 0088 for a GLN, 0009 for a SIRET, 0002 for a SIREN. The rule checks that the legal registration number of the seller, the buyer or the payee, when it gives its register, uses such a code, not the register's name.

## Why it matters

BR-CL-11 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-11 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the register in your software from its list, or leave the code out if there is none for your register.
2. Check that the e-invoice writes the four-digit code, or no code.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-11.

## Common causes

- **The register's name instead of its code**, such as SIREN or HRB.
- **A national register with no ISO 6523 code**, given a made-up one.

## Technical details

The rule reads the scheme of the legal registration identifiers: the seller's (BT-30-1), the buyer's (BT-47-1) and the payee's (BT-61-1). In CII, it is the `schemeID` of each `ram:ID` outside a `ram:SpecifiedTaxRegistration`, such as `ram:ID` of `ram:SpecifiedLegalOrganization`; in UBL, the `schemeID` of `cbc:CompanyID` in each `cac:PartyLegalEntity`. The list is the ISO 6523 ICD list. The scheme is optional: a number without one passes.

The example invoice gives the seller's commercial register number with the scheme `HRB`, the register's name. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000581`, which fails next to it in a Factur-X invoice.

## Official text

> Any registration identifier identification scheme identifier MUST be coded using one of the ISO 6523 ICD list.

BR-CL-11, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-10](../BR-CL-10/): the code that says which register a party's identifier comes from must be in the ISO 6523 list, such as 0088 for a GLN.
- [BR-FR-10](../BR-FR-10/): the invoice must give the seller's SIREN: 9 digits, no spaces.
- [BR-FR-09](../BR-FR-09/): when a party on the invoice has a SIRET, it must have 14 digits and start with that party's SIREN.
