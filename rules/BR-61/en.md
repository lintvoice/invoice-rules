# A credit transfer gives no account

The invoice is paid by credit transfer, but gives no account identifier.

## What the rule checks

For a credit transfer, SEPA, national or international, the buyer needs the account to pay into. The rule checks that the invoice gives it, by its IBAN or by another account number.

## Why it matters

BR-61 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-61 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the IBAN of your bank account in your software settings.
2. If you are paid by another means than a credit transfer, choose that payment means instead.
3. If the account is missing from the e-invoice, report it to the software's publisher, quoting BR-61.

## Common causes

- **An account given by its holder's name only.**
- **Credit transfer chosen by default** for every invoice, even when no account is set up.

## Technical details

The payment account identifier is BT-84, the payment means type code BT-81. In CII, the rule looks for `ram:IBANID` or `ram:ProprietaryID` in `ram:PayeePartyCreditorFinancialAccount`, in a `ram:SpecifiedTradeSettlementPaymentMeans` whose `ram:TypeCode` is 30 or 58, credit transfer and SEPA credit transfer; in UBL, `cbc:ID` of `cac:PayeeFinancialAccount`.

The example invoice gives the account's name but no IBAN. Rule BR-50, which asks for the same identifier when an account is given, and the CII syntax rule `CII-SR-470`, which asks for an IBAN or another account number, fail too: the example fails the three rules.

## Official text

> If the Payment means type code (BT-81) means SEPA credit transfer, Local credit transfer or Non-SEPA international credit transfer, the Payment account identifier (BT-84) shall be present.

BR-61, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-50](../BR-50/): when the invoice is paid by credit transfer and gives an account, the account's identifier, such as its IBAN, must be filled in.
- [BR-49](../BR-49/): when an invoice gives payment instructions, it must say how to pay, with a standard code.
- [BR-CL-16](../BR-CL-16/): the payment means must be a code from the official list, such as 58 for a SEPA credit transfer.
