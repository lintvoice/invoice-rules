# On a self-billed invoice, the seller's electronic address does not start with its SIREN

A self-billed invoice is declared B2B, but the seller's electronic address does not start with the seller's SIREN, or does not use the scheme code 0225.

## What the rule checks

A self-billed invoice is issued by the buyer on behalf of the seller, and sent to the seller. When it is declared B2B, the seller's electronic address must start with the seller's SIREN, with the scheme code 0225. Self-billed document types: 389, 501, 500, 471, 473, 261, 502.

## Why it matters

BR-FR-22 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Ask your supplier for its e-invoicing address: it starts with its SIREN.
2. Enter it in the supplier record used for self-billing, with the scheme code 0225.
3. If your software does not send it, report it to the software's publisher, quoting BR-FR-22.

## Common causes

- **Your own address** used as the seller's address on the self-billed invoice.
- **An e-mail address instead of the e-invoicing address.**
- **A missing or different scheme code.**

## Technical details

BT-34 (seller electronic address) and its scheme BT-34-1; the seller's SIREN is BT-30. The rule applies when the BAR note is B2B and the document type (BT-3) is a self-billing type.

## Official text

> Si le traitement est BAR/B2B et que le type de document (BT-3) est en autofacture (389, 501, 500, 471, 473, 261, 502), alors le BT-34 (EndpointID du vendeur) doit commencer par le SIREN (BT-30) et le BT-34-1 (schemeID) doit être égal à "0225".

BR-FR-22, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-22_BT-34`.

## Related rules

- [BR-FR-21](../BR-FR-21/): the same check for the buyer on other B2B invoices.
- [BR-FR-13](../BR-FR-13/): the seller's electronic address is mandatory.
