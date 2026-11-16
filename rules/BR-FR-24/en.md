# A private identifier contains a character that is not allowed

A seller or buyer identifier declared with the scheme code 0224 contains a space, an accent or a sign that is not allowed.

## What the rule checks

The seller and the buyer may be identified by a private identifier, declared with the scheme code 0224. It may contain only letters without accents, digits and the signs `-`, `_` and `.`; spaces are refused.

## Why it matters

BR-FR-24 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check the private identifier in the seller or customer record: remove spaces, accents and other signs.
2. For example, `CLIENT 0042` becomes `CLIENT-0042`.
3. If your software changes the identifier on export, report it to the software's publisher, quoting BR-FR-24.

## Common causes

- **A space in the identifier.**
- **A slash or a colon** used as a separator.
- **An accented letter.**

## Technical details

Seller identifier BT-29 and buyer identifier BT-46 (`ram:GlobalID` in CII) whose scheme is `0224`. Pattern checked: `^[A-Za-z0-9+\-_.]+$`, which also accepts `+`.

## Official text

> L'identifiant privé (ram:GlobalID) ne respecte pas le format autorisé.

BR-FR-24, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-24_BT-29`, `BR-FR-24_BT-46`.

## Related rules

- [BR-FR-26](../BR-FR-26/): a private identifier is at most 100 characters long.
- [BR-FR-CO-10](../BR-FR-CO-10/): each identifier has a scheme, used once per party.
