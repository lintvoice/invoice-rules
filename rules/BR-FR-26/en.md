# A private identifier is longer than 100 characters

A seller or buyer identifier declared with the scheme code 0224 is longer than 100 characters.

## What the rule checks

The private identifier of the seller or the buyer, declared with the scheme code 0224, is limited to 100 characters.

## Why it matters

BR-FR-26 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check the private identifier in the seller or customer record.
2. Shorten it: a short reference, such as a customer number, is enough.
3. If your software builds a long identifier on export, report it to the software's publisher, quoting BR-FR-26.

## Common causes

- **A name or an address used as the identifier.**
- **Several references joined** in one identifier.

## Technical details

Seller identifier BT-29 and buyer identifier BT-46 (`ram:GlobalID` in CII) whose scheme is `0224`: at most 100 characters.

## Official text

> L'identifiant privé (ram:GlobalID) dépasse 100 caractères.

BR-FR-26, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-26_BT-29`, `BR-FR-26_BT-46`.

## Related rules

- [BR-FR-24](../BR-FR-24/): the characters allowed in a private identifier.
