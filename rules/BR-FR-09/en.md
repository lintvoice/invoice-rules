# The SIRET does not start with the SIREN

A SIRET given on the invoice does not have 14 digits, or does not start with the SIREN of the same party.

## What the rule checks

The SIRET identifies one establishment of a French company: its first 9 digits are the company's SIREN, followed by 5 digits. When the invoice gives a SIRET for a party (seller, buyer, payee, delivery place…), the rule checks:

- that it has exactly 14 digits;
- that it starts with the SIREN of that same party.

## Why it matters

BR-FR-09 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check each party's SIRET in your software: 14 digits, no spaces.
2. Check that it belongs to the same company as the SIREN given: another company's SIRET cannot match.
3. If the SIRET is right and the error remains, your software may pair one party's SIRET with another's SIREN: report it to the software's publisher, quoting BR-FR-09.

## Common causes

- **Another company's SIRET**, such as the seller's copied for the payee.
- **Spaces in the SIRET** (`012 345 674 00019`).
- **An incomplete SIRET**, with digits missing.

## Technical details

Checked for the seller (BT-29), buyer (BT-46), payee (BT-60) and delivery place (BT-71, and EXT-FR-FE-146 on a line), and for the parties of the French extension: buyer's agent (EXT-FR-FE-06), payer (EXT-FR-FE-46), seller's agent (EXT-FR-FE-69), invoicee (EXT-FR-FE-92) and invoicer (EXT-FR-FE-115). The SIRET is the party identifier with scheme `0009`; the SIREN, the legal identifier with scheme `0002`.

## Official text

> Le SIRET doit contenir 14 chiffres et commencer par le SIREN.

BR-FR-09, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-09_BT-29`, `BR-FR-09_BT-46`, `BR-FR-09_BT-60`, `BR-FR-09_BT-71`, `BR-FR-09_EXT-FR-FE-06`, `BR-FR-09_EXT-FR-FE-115`, `BR-FR-09_EXT-FR-FE-146`, `BR-FR-09_EXT-FR-FE-46`, `BR-FR-09_EXT-FR-FE-69`, `BR-FR-09_EXT-FR-FE-92`.

## Related rules

- [BR-FR-10](../BR-FR-10/): the seller's SIREN is mandatory, 9 digits.
- [BR-FR-32](../BR-FR-32/): every SIREN given in the invoice has 9 digits.
