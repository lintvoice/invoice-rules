# An attached file's type is not allowed

A file attached to the invoice declares a type that is not allowed.

## What the rule checks

An e-invoice can carry files inside it: a timesheet, a delivery note… Each file declares its type, its MIME code, and only six are allowed: application/pdf, image/png, image/jpeg, text/csv, and the XLSX and ODS spreadsheet types. The rule checks that each attached file declares one of them.

## Why it matters

BR-CL-24 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-24 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Attach your supporting documents as PDF, PNG, JPEG, CSV, XLSX or ODS files; convert the others.
2. Check that the e-invoice declares the file's exact type, text/csv for a CSV file.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-24.

## Common causes

- **A Word document or a ZIP archive** attached as is.
- **A generic type**, text/plain for a CSV file.

## Technical details

The attached document is BT-125, its MIME code BT-125-1. In CII, it is the `mimeCode` of `ram:AttachmentBinaryObject` in an `ram:AdditionalReferencedDocument`; in UBL, the `mimeCode` of `cbc:EmbeddedDocumentBinaryObject`. The list is the same in both syntaxes: `application/pdf`, `image/png`, `image/jpeg`, `text/csv`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` and `application/vnd.oasis.opendocument.spreadsheet`.

The example invoice attaches a CSV timesheet declared as `text/plain`; its fixed counterpart declares `text/csv`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000287`, which fails next to it in a Factur-X invoice.

## Official text

> For Mime code in attribute use MIMEMediaType.

BR-CL-24, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-52](../BR-52/): each supporting document an invoice refers to must give its reference.
- [BR-FR-17](../BR-FR-17/): each attachment must be described with one of the 12 codes of the French list, such as RIB, BON_COMMANDE or LISIBLE.
