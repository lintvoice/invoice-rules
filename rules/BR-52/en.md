# A supporting document has no reference

A supporting document of the invoice has an empty reference.

## What the rule checks

An invoice can refer to supporting documents: a timesheet, a delivery note, an attached file… Each one is given by its reference, the number or name that identifies it. The rule checks that each supporting document has one.

## Why it matters

BR-52 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-52 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give each supporting document its reference in your software, its number or file name for example.
2. Check that the e-invoice writes it.
3. If it is missing from the e-invoice, report it to the software's publisher, quoting BR-52.

## Common causes

- **A file attached without a reference.**
- **A reference kept in the file's description** instead of its own field.

## Technical details

An additional supporting document is group BG-24, its reference BT-122. In CII, it is `ram:IssuerAssignedID` of each `ram:AdditionalReferencedDocument` in `ram:ApplicableHeaderTradeAgreement`, whatever its type: in CII, the same element also carries the invoiced object identifier, BT-18, with type code 130. In UBL, `cbc:ID` of each `cac:AdditionalDocumentReference`.

The example invoice refers to a timesheet whose reference is blank, so it fails BR-52 alone.

## Official text

> Each Additional supporting document (BG-24) shall contain a Supporting document reference (BT-122).

BR-52, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-FR-29](../BR-FR-29/): the invoice may give at most one invoiced object reference of type AFL and one of type AVV, and neither may be empty.
- [BR-CL-24](../BR-CL-24/): a file attached to the invoice must be a PDF, a PNG or JPEG image, a CSV file or a spreadsheet (XLSX, ODS), declared with its type.
