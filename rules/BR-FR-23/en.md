# The electronic address contains a character that is not allowed

An electronic address declared with the scheme code 0225 contains a space, an accent or a sign that is not allowed.

## What the rule checks

Electronic addresses declared with the scheme code 0225, the code used for the French reform's addresses, may contain only letters without accents, digits and the signs `-`, `_` and `.`. Spaces, the @ sign and other signs are refused. The rule checks the address of every party: seller, buyer, payee, agents, payer, invoicee, invoicer.

## Why it matters

BR-FR-23 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check the address: remove spaces, accents and signs that are not allowed.
2. An e-mail address (with @) is not a 0225 address: use the party's e-invoicing address.
3. If the address is right in your software but not in the invoice, report it to the software's publisher, quoting BR-FR-23.

## Common causes

- **A space in the address.**
- **An e-mail address** declared with the scheme 0225.
- **An accented letter.**

## Technical details

Electronic addresses of the seller (BT-34), buyer (BT-49), and the parties of the French extension: buyer's agent, payee, payer, seller's agent, invoicee and invoicer (EXT-FR-FE-12, -29, -52, -75, -98, -121), when their scheme is `0225`. Pattern checked: `^[A-Za-z0-9+\-_.]+$`; so the sign `+` is accepted too, although the official message does not mention it.

## Official text

> L'adresse électronique (ram:URIID) ne respecte pas le format autorisé.

BR-FR-23, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-23_BT-34`, `BR-FR-23_BT-49`, `BR-FR-23_EXT-FR-FE-12`, `BR-FR-23_EXT-FR-FE-121`, `BR-FR-23_EXT-FR-FE-29`, `BR-FR-23_EXT-FR-FE-52`, `BR-FR-23_EXT-FR-FE-75`, `BR-FR-23_EXT-FR-FE-98`.

## Related rules

- [BR-FR-25](../BR-FR-25/): an electronic address is at most 125 characters long.
- [BR-FR-12](../BR-FR-12/): the buyer's electronic address is mandatory.
