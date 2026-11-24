# The document type is not a valid code

The code for the kind of document is not in the official list.

## What the rule checks

An e-invoice says what kind of document it is with a number from an international list: 380 for an invoice, 381 for a credit note… The rule checks that the code is one of the list's invoice and credit note codes, not a word such as "INV".

## Why it matters

BR-CL-01 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-01 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the document type in your software from its list, rather than typing it.
2. Check that the e-invoice writes the number, 380 for an invoice.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-01.

## Common causes

- **An abbreviation instead of the code**, such as INV or FAC.
- **A code from an older or national list.**

## Technical details

The invoice type code is BT-3. In CII, it is `ram:TypeCode` of `rsm:ExchangedDocument`; in UBL, `cbc:InvoiceTypeCode` (`cbc:CreditNoteTypeCode` in a credit note). The list is the invoice and credit note part of UNTDID 1001.

The example invoice gives the type code `INV`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000555`, which fails next to it in a Factur-X invoice.

## Official text

> The document type code MUST be coded by the invoice and credit note related code lists of UNTDID 1001.

BR-CL-01, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-04](../BR-04/): every invoice must say what kind of document it is, an invoice or a credit note for example, with a standard code.
- [BR-FR-04](../BR-FR-04/): the document type code must be one of the 16 codes allowed in France, such as 380 for an invoice or 381 for a credit note.
