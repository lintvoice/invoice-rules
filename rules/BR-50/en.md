# The account to pay is empty

The invoice gives an account for the credit transfer, with an empty identifier.

## What the rule checks

For a credit transfer, the invoice gives the account to pay into, by its IBAN or, outside the IBAN system, its account number. When the invoice gives such an account, the rule checks that its identifier is filled in.

## Why it matters

BR-50 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-50 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the IBAN of your bank account in your software settings.
2. Check that the e-invoice writes it in full.
3. If it stays empty, report it to the software's publisher, quoting BR-50.

## Common causes

- **Bank details set up without the IBAN**, only the bank's name.
- **An IBAN shown on the PDF from an image** of the bank details.

## Technical details

The payment account identifier is BT-84. In CII, the rule reads `ram:IBANID` and `ram:ProprietaryID` of `ram:PayeePartyCreditorFinancialAccount`, in a `ram:SpecifiedTradeSettlementPaymentMeans` whose `ram:TypeCode` is 30 or 58, credit transfer and SEPA credit transfer; in UBL, `cbc:ID` of `cac:PayeeFinancialAccount` with the same codes.

The example invoice gives an account whose IBAN is empty, so it fails BR-50 alone.

## Official text

> A Payment account identifier (BT-84) shall be present if Credit transfer (BG-16) information is provided in the Invoice.

BR-50, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-61](../BR-61/): when the invoice is paid by credit transfer, it must give the account to pay into: its IBAN, or its account number outside the IBAN system.
- [BR-49](../BR-49/): when an invoice gives payment instructions, it must say how to pay, with a standard code.
