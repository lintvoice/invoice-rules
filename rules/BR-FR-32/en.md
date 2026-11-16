# A SIREN on the invoice does not have 9 digits

An identifier declared with the scheme code 0002 or 0231 does not have exactly 9 digits.

## What the rule checks

The rule checks every identifier on the invoice declared with:

- the scheme code 0002, which stands for the SIREN;
- the code 0231, used for a member of a single VAT taxpayer (assujetti unique, a VAT group).

Each must have exactly 9 digits, with no spaces or letters, whatever the party: seller, buyer, payee, delivery place…

## Why it matters

BR-FR-32 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Find the party at fault in the validation report.
2. Correct its SIREN in your software: 9 digits, no spaces; not the SIRET (14 digits).
3. If the SIREN is right and the error remains, report it to the software's publisher, quoting BR-FR-32.

## Common causes

- **A SIRET declared with the scheme 0002.**
- **Spaces in the SIREN.**
- **A SIREN with a digit missing.**

## Technical details

Two checks: every `ram:SpecifiedLegalOrganization/ram:ID` with `schemeID="0002"` (`BR-FR-32-LEGALID`), and every `ram:GlobalID` with `schemeID` `0002` or `0231` (`BR-FR-32-GLOBALID`), for any party in the invoice. Pattern: `^\d{9}$`.

## Official text

> Tout identifiant légal d'une Partie avec schemeID = '0002' DOIT être composé de 9 chiffres.

BR-FR-32, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-32-GLOBALID`, `BR-FR-32-ID`, `BR-FR-32-LEGALID`.

## Related rules

- [BR-FR-10](../BR-FR-10/): the seller's SIREN is mandatory.
- [BR-FR-09](../BR-FR-09/): a SIRET starts with its party's SIREN.
