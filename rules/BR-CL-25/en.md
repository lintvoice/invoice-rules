# An electronic address's kind is not a valid code

The code that says what kind of electronic address a party has is not in the EAS list.

## What the rule checks

An e-invoice gives where each party receives e-invoices, its electronic address, with a code from the EAS list that says what kind of address it is: EM for an e-mail address, 0088 for a GLN, 0225 for an address of the French reform's platforms… The rule checks that the code comes from that list, not a word such as "EMAIL".

## Why it matters

BR-CL-25 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-25 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the kind of electronic address in your software from its list.
2. Check that the e-invoice writes its code, EM for an e-mail address.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-25.

## Common causes

- **A word instead of the code**, such as EMAIL or SIREN.
- **A code from another list**, a scheme of the ISO 6523 list that EAS does not have.

## Technical details

The seller's and the buyer's electronic addresses are BT-34 and BT-49, their scheme identifiers BT-34-1 and BT-49-1. In CII, the rule reads the `schemeID` of each `ram:URIID` in a `ram:URIUniversalCommunication`; in UBL, the `schemeID` of each `cbc:EndpointID`. The list is the CEF EAS list, version 17 in the 1.3.17 files. The Peppol network keeps a shorter list, without EM.

The example invoice gives the seller's e-mail address with the scheme `EMAIL` instead of `EM`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000582`, which fails next to it in a Factur-X invoice.

## Official text

> Endpoint identifier scheme identifier MUST belong to the CEF EAS code list

BR-CL-25, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-62](../BR-62/): the seller's electronic address must say, with a standard code, what kind of address it is.
- [BR-63](../BR-63/): the buyer's electronic address must say, with a standard code, what kind of address it is.
- [BR-FR-21](../BR-FR-21/): on a business-to-business invoice, the buyer's electronic address must start with the buyer's SIREN and be declared as a French reform address.
