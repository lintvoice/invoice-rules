# The amount due is not the total with VAT minus what is paid plus rounding

The invoice's amount due is not equal to the total with VAT, minus the amount already paid, plus rounding.

## What the rule checks

The amount due is what the buyer still has to pay. It starts from the total with VAT, takes off what was already paid, a prepayment for example, and adds any rounding. The rule checks this computation exactly.

## Why it matters

BR-CO-16 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-16 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Start from the total with VAT, take off the amount already paid if there is one and add the rounding if there is one: the result is the amount due.
2. If a prepayment was made, give it as the amount already paid, rather than taking it off the total with VAT.
3. If your software computes the amount due another way, report it to the software's publisher, quoting BR-CO-16.

## Common causes

- **A prepayment taken off the amount due** without being given as the amount already paid.
- **Rounding applied to the amount due** without being given as the rounding amount.
- **An amount due set to zero** for an invoice already paid, without giving the amount already paid.

## Technical details

The amount due for payment is BT-115, the total with VAT BT-112, the paid amount BT-113 and the rounding amount BT-114; when the last two are absent, the rule does not count them. In CII: `ram:DuePayableAmount`, `ram:GrandTotalAmount`, `ram:TotalPrepaidAmount` and `ram:RoundingAmount` of `ram:SpecifiedTradeSettlementHeaderMonetarySummation`; in UBL: `cbc:PayableAmount`, `cbc:TaxInclusiveAmount`, `cbc:PrepaidAmount` and `cbc:PayableRoundingAmount` of `cac:LegalMonetaryTotal`.

## Official text

> Amount due for payment (BT-115) = Invoice total amount with VAT (BT-112) -Paid amount (BT-113) +Rounding amount (BT-114).

BR-CO-16, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-15](../BR-CO-15/): the total with VAT must be the total without VAT plus the VAT.
