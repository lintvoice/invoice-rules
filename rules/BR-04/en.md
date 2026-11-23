# The document type is missing

The code that says what kind of document this is, is empty.

## What the rule checks

An e-invoice says what kind of document it is with a standard code: an invoice, a credit note, a corrected invoice… The software that receives it treats each kind in its own way. The rule checks that the code is there.

## Why it matters

BR-04 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-04 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check the document type of the invoice in your software: invoice, credit note…
2. Check that the e-invoice writes its code, for example 380 for an invoice or 381 for a credit note.
3. If the code is missing, report it to the software's publisher, quoting BR-04.

## Common causes

- **A new kind of document** in the software, such as a deposit invoice, with no code mapped to it.
- **A template** in which the type was left blank.

## Technical details

The invoice type code is BT-3. In CII, it is `ram:TypeCode` of `rsm:ExchangedDocument`; in UBL, `cbc:InvoiceTypeCode` (`cbc:CreditNoteTypeCode` in a credit note). Its codes come from the UNTDID 1001 list, as rule BR-CL-01 requires.

The example invoice leaves the code empty. An empty code is not in the list either, so BR-CL-01 fails too, and the example fails both rules.

## Official text

> An Invoice shall have an Invoice type code (BT-3).

BR-04, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-01](../BR-CL-01/): the document type must be a code from the official list, such as 380 for an invoice or 381 for a credit note.
- [BR-FR-04](../BR-FR-04/): the document type code must be one of the 16 codes allowed in France, such as 380 for an invoice or 381 for a credit note.
