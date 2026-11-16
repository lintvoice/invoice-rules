# A line's period has neither a start date nor an end date

An invoice line gives a period, but with neither a start date nor an end date.

## What the rule checks

Each line can give its own period, for example for a subscription or rental line. When it does, the rule checks that the period has at least one date: the start, the end, or both.

## Why it matters

BR-CO-20 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-20 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. If the line covers a period, fill in its start date, its end date, or both.
2. If it covers no period, remove the line's period rather than leaving it empty.
3. If your software creates an empty line period, report it to the software's publisher, quoting BR-CO-20.

## Common causes

- **A line period the software creates empty**, when no date is entered.
- **Dates written in the line's item name** instead of the period's fields.

## Technical details

The invoice line period is group BG-26, with its start date BT-134 and its end date BT-135. In CII: `ram:BillingSpecifiedPeriod` in `ram:SpecifiedLineTradeSettlement`, with `ram:StartDateTime` and `ram:EndDateTime`; in UBL: `cac:InvoicePeriod` in `cac:InvoiceLine` (or `cac:CreditNoteLine`), with `cbc:StartDate` and `cbc:EndDate`.

## Official text

> If Invoice line period (BG-26) is used, the Invoice line period start date (BT-134) or the Invoice line period end date (BT-135) shall be filled, or both.

BR-CO-20, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-19](../BR-CO-19/): the invoicing period must have a start or an end date.
- [BR-FR-03](../BR-FR-03/): the period's dates, like the invoice's other dates, must have a year between 2000 and 2099.
