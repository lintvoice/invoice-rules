# The seller's electronic address is missing

The invoice does not give the seller's electronic address.

## What the rule checks

The seller's electronic address is where invoices are delivered to the seller. It is not necessarily an e-mail address. The rule requires it on every invoice.

## Why it matters

BR-FR-13 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Find your company's e-invoicing address: it is not your e-mail address.
2. Enter it in your company's record, in your software.
3. If your software has no such field, report it to the software's publisher, quoting BR-FR-13.

## Common causes

- **The company record has only an e-mail or a postal address**, no e-invoicing address.
- **The software does not send this field** in the e-invoice.

## Technical details

BT-34, the seller's electronic address, with its scheme BT-34-1: `ram:URIUniversalCommunication/ram:URIID` (attribute `schemeID`) of the seller party in CII, `cbc:EndpointID` in UBL.

## Official text

> Le BT-34 est obligatoire.

BR-FR-13, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-13_BT-34`.

## Related rules

- [BR-FR-12](../BR-FR-12/): the buyer's electronic address is mandatory too.
- [BR-FR-22](../BR-FR-22/): on a self-billed B2B invoice, it starts with the seller's SIREN.
- [BR-FR-23](../BR-FR-23/): the characters allowed in an electronic address.
