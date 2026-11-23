# The invoicing period ends before it starts

The invoicing period's end date is before its start date.

## What the rule checks

An invoice can give the period it covers, a month of service for example, with a start date and an end date. When both are given, the rule checks that the end is on or after the start.

## Why it matters

BR-29 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-29 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check the period's two dates in your software: they may be swapped.
2. For a single day, give the same date as start and end.
3. If the dates come out swapped, report it to the software's publisher, quoting BR-29.

## Common causes

- **Swapped dates**, the end typed in the start field.
- **A date read in the wrong order**, day and month swapped in an import.

## Technical details

The invoicing period is group BG-14, with a start date BT-73 and an end date BT-74. In CII, the rule compares `ram:StartDateTime` and `ram:EndDateTime` of `ram:BillingSpecifiedPeriod`, in `ram:ApplicableHeaderTradeSettlement`, both in format 102; in UBL, `cbc:StartDate` and `cbc:EndDate` of `cac:InvoicePeriod`.

The example invoice gives an invoicing period whose two dates are swapped, so it fails BR-29 alone.

## Official text

> If both Invoicing period start date (BT-73) and Invoicing period end date (BT-74) are given then the Invoicing period end date (BT-74) shall be later or equal to the Invoicing period start date (BT-73).

BR-29, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-30](../BR-30/): when the line period gives both dates, the end date must not be before the start date.
- [BR-CO-19](../BR-CO-19/): if the invoice gives an invoicing period, give at least its start date or its end date.
