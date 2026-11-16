# The seller's SIREN is missing or not 9 digits

The invoice does not give the seller's SIREN, or that SIREN does not have exactly 9 digits.

## What the rule checks

Every invoice must give the seller's SIREN: the 9-digit number that identifies a French company. The rule checks that it is there and that it has exactly 9 digits, with no spaces or letters.

It does not check that the SIREN exists, or that it belongs to the seller.

## Why it matters

BR-FR-10 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

The reform relies on platforms approved by the State and on a directory run by the administration, which identify companies ([DGFiP press release, 16 January 2026, in French](https://presse.economie.gouv.fr/facturation-electronique-la-direction-generale-des-finances-publiques-publie-la-liste-des-101-premieres-plateformes-agreees/)). Without a SIREN, the seller is not identified.

## How to fix it

1. In your invoicing software, open your company's settings and check the SIREN: 9 digits, no spaces.
2. Do not confuse it with the SIRET, which has 14 digits: the SIRET identifies one establishment, the SIREN the whole company. The first 9 digits of the SIRET are the SIREN.
3. If the SIREN is entered and the error remains, your software does not send it in the e-invoice. Report it to the software's publisher, quoting BR-FR-10.

## Common causes

- **The SIREN is not entered** in the company settings.
- **The SIRET is entered instead** of the SIREN.
- **The SIREN contains spaces**, for example `012 345 674`.
- **The software does not put it in the right place** in the invoice file.

## Technical details

The SIREN goes in the seller's legal registration identifier (BT-30), with the scheme code `0002`, which stands for SIREN. The SIRET goes in the seller identifier (BT-29), with the code `0009`; it must start with the SIREN (rule BR-FR-09). In a Factur-X PDF, the rule applies to the XML (CII) file inside the PDF.

## Official text

> Le SIREN du vendeur (ram:ID) est obligatoire et doit être composé exactement de 9 chiffres.

BR-FR-10/BT-30, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-10_BT-30`.

## Related rules

- [BR-FR-09](../BR-FR-09/): the seller's SIRET must start with its SIREN.
- [BR-FR-11](../BR-FR-11/): the buyer's SIREN, on invoices between businesses.
- [BR-FR-32](../BR-FR-32/): every SIREN given in the invoice must have 9 digits.
