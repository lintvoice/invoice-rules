# The electronic address is longer than 125 characters

An electronic address on the invoice is longer than 125 characters.

## What the rule checks

The rule limits each party's electronic address to 125 characters: seller, buyer, payee, agents, payer, invoicee, invoicer, whatever the scheme code.

## Why it matters

BR-FR-25 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Check the address in the party's record: it is often a text pasted by mistake, not a real address.
2. Replace it with the party's e-invoicing address.
3. If your software joins several fields into the address, report it to the software's publisher, quoting BR-FR-25.

## Common causes

- **A note or a comment pasted** in the address field.
- **Several addresses joined** in one field.

## Technical details

Electronic addresses of the seller (BT-34), buyer (BT-49), and the parties of the French extension: buyer's agent, payee, payer, seller's agent, invoicee and invoicer (EXT-FR-FE-12, -29, -52, -75, -98, -121) (`ram:URIUniversalCommunication/ram:URIID` in CII): at most 125 characters.

## Official text

> L'adresse électronique (ram:URIID) dépasse 125 caractères.

BR-FR-25, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-25_BT-34`, `BR-FR-25_BT-49`, `BR-FR-25_EXT-FR-FE-12`, `BR-FR-25_EXT-FR-FE-121`, `BR-FR-25_EXT-FR-FE-29`, `BR-FR-25_EXT-FR-FE-52`, `BR-FR-25_EXT-FR-FE-75`, `BR-FR-25_EXT-FR-FE-98`.

## Related rules

- [BR-FR-23](../BR-FR-23/): the characters allowed in an electronic address.
