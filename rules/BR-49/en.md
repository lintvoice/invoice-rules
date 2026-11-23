# The payment means is missing

The invoice gives payment instructions without saying how to pay.

## What the rule checks

An invoice can tell the buyer how to pay: by credit transfer, direct debit, card… In an e-invoice, the payment means is a standard code, 58 for a SEPA credit transfer for example. When the invoice gives payment instructions, the rule checks that it gives this code.

## Why it matters

BR-49 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-49 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose the payment means of each invoice in your software, or a default one.
2. Check that the e-invoice writes its code.
3. If it is missing from the e-invoice, report it to the software's publisher, quoting BR-49.

## Common causes

- **Bank details written without a payment means.**
- **A payment means typed as text** that the software does not turn into a code.

## Technical details

A payment instruction is group BG-16, its payment means type code BT-81. In CII, it is `ram:TypeCode` of each `ram:SpecifiedTradeSettlementPaymentMeans`; in UBL, `cbc:PaymentMeansCode` of each `cac:PaymentMeans`. Its codes come from the UNCL 4461 list, as rule BR-CL-16 requires.

This page has no example file: the [Factur-X EN 16931 XML schema](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/Factur-X/EN16931/1xsd) requires the payment means type code, while the examples of [invoice-examples](https://github.com/lintvoice/invoice-examples) stay schema-valid so that they fail business rules only. The [full UN/CEFACT CII schema (D22B)](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/1xsd-CII_D22B_uncoupled), on the other hand, leaves it optional: a CII invoice can pass that schema and still fail the rule.

## Official text

> A Payment instruction (BG-16) shall specify the Payment means type code (BT-81).

BR-49, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CL-16](../BR-CL-16/): the payment means must be a code from the official list, such as 58 for a SEPA credit transfer.
- [BR-50](../BR-50/): when the invoice is paid by credit transfer and gives an account, the account's identifier, such as its IBAN, must be filled in.
- [BR-61](../BR-61/): when the invoice is paid by credit transfer, it must give the account to pay into: its IBAN, or its account number outside the IBAN system.
