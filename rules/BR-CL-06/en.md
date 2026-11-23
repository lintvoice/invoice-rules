# The VAT due date code is not a valid code

The code that says when the VAT becomes due is not one of the allowed codes.

## What the rule checks

An invoice can say, with a code, which date makes the VAT due: the invoice date, the delivery date or the payment date. The codes differ between the two syntaxes of e-invoices, CII (used by Factur-X and ZUGFeRD) and UBL (used by Peppol). The rule checks that the code is one of the three of the invoice's syntax.

## Why it matters

BR-CL-06 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-06 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check which date makes your VAT due, and choose it in your software.
2. Check that a CII invoice writes 5, 29 or 72, and a UBL invoice 3, 35 or 432.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-06.

## Common causes

- **A UBL code in a CII invoice**, or the reverse, from software that writes both syntaxes.
- **A code typed by hand** in a free field.

## Technical details

The VAT point date code is BT-8. In CII, it is `ram:DueDateTypeCode` of `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`, from UNTDID 2475: `5` the invoice date, `29` the delivery date, `72` the payment date. In UBL, it is `cbc:DescriptionCode` of `cac:InvoicePeriod`, from UNTDID 2005: `3` the invoice date, `35` the actual delivery date, `432` the paid-to date. Rule BR-CO-03 forbids giving both this code and a VAT point date (BT-7).

The example invoice, in CII, gives the code `35`, the UBL code for the delivery date. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000588`, which fails next to it in a Factur-X invoice.

## Official text

> Value added tax point date code MUST be coded using a restriction of UNTDID 2475.

BR-CL-06, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-03](../BR-CO-03/): give either the VAT point date or its code, never both.
