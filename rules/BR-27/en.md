# A line's net price is negative

A line of the invoice has a negative net unit price.

## What the rule checks

A line's net unit price cannot be negative: it may be zero, never less. A discount, a deducted advance payment or a returned item is therefore not written as a line at a negative price.

## Why it matters

BR-27 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-27 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. For a discount, use your software's allowance: on the line concerned, or on the whole invoice.
2. For an advance payment already received, enter it as an amount already paid: it is deducted from the amount due.
3. For an item taken back or returned, enter a negative quantity at a positive price, or issue a credit note.
4. If your software only allows discounts as lines at a negative price, report it to the software's publisher, quoting BR-27.

## Common causes

- **A discount entered as a line** at a negative price.
- **A deducted advance payment** written as a negative line.
- **A returned item** invoiced at a negative price instead of a negative quantity.

## Technical details

The net unit price is BT-146. In CII: `ram:NetPriceProductTradePrice/ram:ChargeAmount` in `ram:SpecifiedLineTradeAgreement`; in UBL: `cac:Price/cbc:PriceAmount` of each `cac:InvoiceLine`. The rule accepts a zero price. A negative quantity (BT-129) remains possible: the French rule BR-FR-DEC-02 accepts the sign "-".

In France, rule BR-FR-DEC-03 also requires a price without a "-" sign, except for the billing frames S9, M9 and B9: the example invoice, a French invoice that enters a discount as a line at −50.00 €, therefore fails both rules. Its fixed version carries the same discount on the whole invoice.

## Official text

> The Item net price (BT-146) shall NOT be negative.

BR-27, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-26](../BR-26/): each line must give its net unit price.
- [BR-FR-DEC-03](../BR-FR-DEC-03/): in France, a unit price is written without a "-" sign.
- [BR-CO-21](../BR-CO-21/): an allowance on the whole invoice must give its reason.
