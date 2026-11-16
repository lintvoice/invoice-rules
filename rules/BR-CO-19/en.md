# The invoicing period has neither a start date nor an end date

The invoice gives an invoicing period, but with neither a start date nor an end date.

## What the rule checks

An invoice can give the period it covers, for example a subscription from 1 to 31 October. When it does, the rule checks that the period has at least one date: the start, the end, or both.

## Why it matters

BR-CO-19 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-19 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. If the invoice covers a period, fill in its start date, its end date, or both.
2. If it covers no period, remove the invoicing period rather than leaving it empty.
3. If your software creates an empty period, report it to the software's publisher, quoting BR-CO-19.

## Common causes

- **A period the software creates empty**, when no date is entered.
- **Dates written elsewhere**, in free text for example, instead of the period's fields.

## Technical details

The invoicing period is group BG-14, with its start date BT-73 and its end date BT-74. In CII: `ram:BillingSpecifiedPeriod` in `ram:ApplicableHeaderTradeSettlement`, with `ram:StartDateTime` and `ram:EndDateTime`; in UBL: `cac:InvoicePeriod`, with `cbc:StartDate` and `cbc:EndDate`. In UBL, a period that only carries the VAT point date code (BT-8, `cbc:DescriptionCode`) passes too.

## Official text

> If Invoicing period (BG-14) is used, the Invoicing period start date (BT-73) or the Invoicing period end date (BT-74) shall be filled, or both.

BR-CO-19, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-20](../BR-CO-20/): a line's period must have a start or an end date.
- [BR-FR-03](../BR-FR-03/): the period's dates, like the invoice's other dates, must have a year between 2000 and 2099.
