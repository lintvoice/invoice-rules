# The preceding invoice's number is missing

The invoice refers to a preceding invoice whose number is empty.

## What the rule checks

A credit note, a corrected invoice or a final invoice after deposits refers to the invoices that came before. Each one is given by its number, and its date when known. The rule checks that each reference gives the number.

## Why it matters

BR-55 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-55 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give the number of the invoice you correct or credit in your software.
2. Check that the e-invoice writes it, not only the PDF.
3. If it is missing from the e-invoice, report it to the software's publisher, quoting BR-55.

## Common causes

- **A credit note created without choosing the invoice it cancels.**
- **A reference given in a note**, as text, rather than in its own field.

## Technical details

A preceding invoice reference is group BG-3, its number BT-25 and its date BT-26. In CII, the rule reads `ram:IssuerAssignedID` of each `ram:InvoiceReferencedDocument` in `ram:ApplicableHeaderTradeSettlement`; in UBL, `cbc:ID` of each `cac:InvoiceDocumentReference` in `cac:BillingReference`.

The example invoice refers to a preceding invoice with an empty number, so it fails BR-55 alone.

## Official text

> Each Preceding Invoice reference (BG-3) shall contain a Preceding Invoice reference (BT-25).

BR-55, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-FR-CO-04](../BR-FR-CO-04/): a corrective invoice must cite one, and only one, earlier invoice, with its number and its date.
- [BR-FR-02](../BR-FR-02/): the invoice number may contain only letters, digits and the signs + - _ /, with no spaces.
