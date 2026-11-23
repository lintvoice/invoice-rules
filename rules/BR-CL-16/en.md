# The payment means is not a valid code

The payment means is not a code from the official list.

## What the rule checks

An e-invoice says how to pay with a number from an international list: 30 for a credit transfer, 58 for a SEPA credit transfer, 59 for a SEPA direct debit, 48 for a bank card… The rule checks that the code comes from that list, not a word such as "SEPA".

## Why it matters

BR-CL-16 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-16 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the payment means in your software from its list.
2. Check that the e-invoice writes its number, 58 for a SEPA credit transfer.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-16.

## Common causes

- **A word instead of the code**, such as SEPA or TRANSFER.
- **A bank's own code** for a payment means.

## Technical details

The payment means type code is BT-81. In CII, it is `ram:TypeCode` of each `ram:SpecifiedTradeSettlementPaymentMeans`; in UBL, `cbc:PaymentMeansCode` of each `cac:PaymentMeans`. The list is UNTDID 4461.

The example invoice gives the payment means `SEPA` instead of `58`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000609`, which fails next to it in a Factur-X invoice.

## Official text

> Payment means in an invoice MUST be coded using UNTDID 4461 code list

BR-CL-16, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-49](../BR-49/): when an invoice gives payment instructions, it must say how to pay, with a standard code.
- [BR-61](../BR-61/): when the invoice is paid by credit transfer, it must give the account to pay into: its IBAN, or its account number outside the IBAN system.
