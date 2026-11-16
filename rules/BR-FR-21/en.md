# The buyer's electronic address does not start with its SIREN

The invoice is declared B2B, but the buyer's electronic address does not start with the buyer's SIREN, or does not use the scheme code 0225.

## What the rule checks

When the invoice is declared B2B (BAR note) and is not self-billed, the buyer's electronic address must:

- start with the buyer's SIREN;
- be declared with the scheme code 0225.

For a self-billed invoice (types 389, 501, 500, 471, 473, 261, 502), the seller's address is checked instead (BR-FR-22).

## Why it matters

BR-FR-21 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check your customer's e-invoicing address: it starts with its SIREN (9 digits).
2. Check that your software sends it with the scheme code 0225.
3. If the address and code are right in the customer record but not in the invoice, report it to the software's publisher, quoting BR-FR-21.

## Common causes

- **An e-mail address instead of the e-invoicing address.**
- **The address of another entity** of the group, with another SIREN.
- **A missing or different scheme code** (such as 0009 or EM).

## Technical details

BT-49 (buyer electronic address) and its scheme BT-49-1; the buyer's SIREN is BT-47. Self-billed document types (BT-3) excluded: 389, 501, 500, 471, 473, 261, 502.

## Official text

> Si le traitement est BAR/B2B et que le type de document (BT-3) n’est pas en autofacture (389, 501, 500, 471, 473, 261, 502), alors le BT-49 (EndpointID) doit commencer par le SIREN (BT-47) et le BT-49-1 (schemeID) doit être égal à "0225".

BR-FR-21, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-21_BT-49`.

## Related rules

- [BR-FR-12](../BR-FR-12/): the buyer's electronic address is mandatory.
- [BR-FR-22](../BR-FR-22/): the same check for the seller on self-billed invoices.
- [BR-FR-11](../BR-FR-11/): a B2B invoice requires the buyer's SIREN.
