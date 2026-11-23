# The kind of invoiced object is not a valid code

The code that says what kind of identifier the invoiced object has is not in the official list.

## What the rule checks

An invoice can identify the object it invoices: a contract, a meter, a subscription… A code says what kind of identifier it is, AVV for a framework agreement number for example. The rule checks that this code comes from the official list, not a word such as "ORDER".

## Why it matters

BR-CL-07 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-07 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the kind of identifier in your software from its list.
2. Check that the e-invoice writes a code from the list next to the identifier.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-07.

## Common causes

- **A word instead of the code**, such as ORDER or CONTRACT.
- **An order number written as an invoiced object**, with a made-up code.

## Technical details

The invoiced object identifier is BT-18, its scheme identifier BT-18-1. In CII, it is `ram:ReferenceTypeCode` of the `ram:AdditionalReferencedDocument` whose `ram:TypeCode` is 130; in UBL, the `schemeID` of `cbc:ID` in the `cac:AdditionalDocumentReference` whose `cbc:DocumentTypeCode` is 130. The list is part of UNTDID 1153.

The example invoice gives an invoiced object with the code `ORDER`; its fixed counterpart gives `AVV`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000282`, which fails next to it in a Factur-X invoice.

## Official text

> Object identifier identification scheme identifier MUST be coded using a restriction of UNTDID 1153.

BR-CL-07, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-FR-29](../BR-FR-29/): the invoice may give at most one invoiced object reference of type AFL and one of type AVV, and neither may be empty.
- [BR-52](../BR-52/): each supporting document an invoice refers to must give its reference.
