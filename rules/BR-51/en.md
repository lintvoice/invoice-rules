# The invoice shows a full card number

The invoice gives the full number of a payment card.

## What the rule checks

When an invoice is paid by card, it can say which card, but the card payment security standards forbid showing its full number. The official message allows at most the first 6 and the last 4 digits. The rule checks that the number written has 10 characters at most.

## Why it matters

BR-51 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-51 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Write only the last 4 digits of the card in the invoice.
2. Check that your software masks the card number in the e-invoice too, not only on the PDF.
3. If it writes the full number, report it to the software's publisher, quoting BR-51.

## Common causes

- **A card number masked on the PDF only**, with stars, but written in full in the data.
- **A masked number longer than 10 characters**, such as 12 stars and 4 digits.

## Technical details

The payment card primary account number is BT-87. In CII, it is `ram:ID` of `ram:ApplicableTradeSettlementFinancialCard` in `ram:SpecifiedTradeSettlementPaymentMeans`; in UBL, `cbc:PrimaryAccountNumberID` of `cac:CardAccount`. The rule counts its characters: at most 10.

In the 1.3.17 files, the rule is fatal in CII and a warning in UBL. Its CII message names BT-97, the reason of an allowance, where the UBL message names BT-87, the card number.

The example invoice is paid by card and gives the card's full number, so it fails BR-51 alone.

## Official text

> In accordance with card payments security standards an invoice should never include a full card primary account number (BT-97). At the moment PCI Security Standards Council has defined that the first 6 digits and last 4 digits are the maximum number of digits to be shown.

BR-51, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-49](../BR-49/): when an invoice gives payment instructions, it must say how to pay, with a standard code.
- [BR-CL-16](../BR-CL-16/): the payment means must be a code from the official list, such as 58 for a SEPA credit transfer.
