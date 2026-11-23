# The invoice does not say which rules it follows

The field that names the rules the invoice follows is empty.

## What the rule checks

An e-invoice says which specification it follows: the European standard EN 16931, or a profile built on it, such as a Factur-X profile, XRechnung or Peppol BIS. The software that receives the invoice reads this field to know which rules apply. The rule checks that the field is filled in.

## Why it matters

BR-01 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-01 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Find out which format and profile your software produces, for example Factur-X EN 16931 or XRechnung.
2. Check that it writes this profile's identifier in every e-invoice.
3. If the field stays empty, report it to the software's publisher, quoting BR-01.

## Common causes

- **A template** in which the identifier was left blank.
- **An export built field by field** that skips this one, because nothing on the PDF shows it.

## Technical details

The specification identifier is BT-24. In CII, it is `ram:ID` of `ram:GuidelineSpecifiedDocumentContextParameter`, in `rsm:ExchangedDocumentContext`; in UBL, `cbc:CustomizationID`. For the Factur-X EN 16931 profile, its value is `urn:cen.eu:en16931:2017`.

The example invoice leaves the identifier empty. The Factur-X profile's own check of this identifier reads only a value that is there, so the example fails BR-01 alone.

## Official text

> An Invoice shall have a Specification identifier (BT-24).

BR-01, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-02](../BR-02/): every invoice must have a number.
- [BR-03](../BR-03/): every invoice must give its issue date, written as a date.
- [BR-04](../BR-04/): every invoice must say what kind of document it is, an invoice or a credit note for example, with a standard code.
