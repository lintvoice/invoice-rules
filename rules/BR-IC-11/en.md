# An intra-Community supply gives no delivery date

The invoice is for an intra-Community supply, but it gives neither the delivery date nor an invoicing period.

## What the rule checks

Category K covers goods sold and sent to a business in another EU country, which accounts for the VAT there. The date of the supply sets when the exemption and the buyer's VAT apply. The rule checks that an invoice with a breakdown in K gives the actual delivery date (BT-72). An invoicing period (BG-14) will do instead, with its start (BT-73) or end date (BT-74).

## Why it matters

BR-IC-11 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-IC-11 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the delivery date of the goods, or the period the invoice covers.
2. If the date is entered but missing from the e-invoice, report it to the software's publisher, quoting BR-IC-11.

## Common causes

- **A delivery date printed on the delivery note only**, not on the invoice.

## Technical details

The actual delivery date is BT-72, the invoicing period BG-14. In CII: `ram:ActualDeliverySupplyChainEvent/ram:OccurrenceDateTime` in `ram:ApplicableHeaderTradeDelivery`, or `ram:BillingSpecifiedPeriod` with `ram:StartDateTime` or `ram:EndDateTime` next to the breakdown; in UBL: `cac:Delivery/cbc:ActualDeliveryDate`, or `cac:InvoicePeriod`.

The example invoice is all in K, and has no delivery date; its fixed version gives it.

## Official text

> In an Invoice with a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Intra-community supply" the Actual delivery date (BT-72) or the Invoicing period (BG-14) shall not be blank.

BR-IC-11, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-IC-12](../BR-IC-12/): an invoice for an intra-Community supply (K) gives the country the goods are delivered to.
- [BR-IC-02](../BR-IC-02/): an invoice with a line in the VAT category K (intra-Community supply) must give the seller's and the buyer's VAT numbers.
- [BR-IC-10](../BR-IC-10/): the VAT breakdown in category K (intra-Community supply) gives the reason no VAT is charged, as text or as a code.
