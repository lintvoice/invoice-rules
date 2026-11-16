# The operation type (BAR note) has a value that is not allowed

The note coded BAR has a value outside the allowed list.

## What the rule checks

A note coded BAR says how the invoice is to be handled, for example B2B for an invoice between businesses or B2C for an invoice to a private person. It may only be: B2B, B2BINT, B2C, B2CINT, OUTOFSCOPE or ARCHIVEONLY. Any other value, a typing error or lowercase letters included, is refused.

## Why it matters

BR-FR-20 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check the value of the BAR note your software sends.
2. Correct it with a value from the list, in capitals, with no spaces.
3. If you do not know which one applies, ask your approved platform or your software's publisher.

## Common causes

- **Lowercase letters** (`b2b`).
- **A space or a hyphen** (`B2B ` or `B-2-B`).
- **A value from another system**, such as `BUSINESS`.

## Technical details

A note (BG-1) whose subject code BT-21 is `BAR`; the value is the note text BT-22.

## Official text

> Lorsqu’une note a pour code sujet « BAR » (BT-21), la valeur associée (BT-22, contenu de la note) doit être l’une des suivantes : B2B, B2BINT, B2C, B2CINT, OUTOFSCOPE, ARCHIVEONLY.

BR-FR-20, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-20_BT-21`.

## Related rules

- [BR-FR-31](../BR-FR-31/): only one BAR note per invoice.
- [BR-FR-11](../BR-FR-11/): a B2B invoice requires the buyer's SIREN.
- [BR-FR-21](../BR-FR-21/): on a B2B invoice, the buyer's electronic address starts with its SIREN.
