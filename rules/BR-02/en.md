# The invoice number is missing

The invoice number is empty.

## What the rule checks

Every invoice has a number that identifies it, given by the seller and unique within the seller's invoices. The rule checks that the e-invoice gives one.

## Why it matters

BR-02 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-02 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give each invoice its number in your software before you issue it.
2. Check that the number printed on the PDF is also in the e-invoice.
3. If the number is missing from the e-invoice, report it to the software's publisher, quoting BR-02.

## Common causes

- **An invoice sent while still a draft**, before the software numbered it.
- **A number printed on the PDF** but not written in the e-invoice data.

## Technical details

The invoice number is BT-1. In CII, it is `ram:ID` of `rsm:ExchangedDocument`; in UBL, `cbc:ID` of the invoice.

The example invoice leaves the number empty.

## Official text

> An Invoice shall have an Invoice number (BT-1).

BR-02, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-FR-01](../BR-FR-01/): the invoice number, and the number of any invoice it refers to, must not exceed 35 characters.
- [BR-FR-02](../BR-FR-02/): the invoice number may contain only letters, digits and the signs + - _ /, with no spaces.
- [BR-03](../BR-03/): every invoice must give its issue date, written as a date.
