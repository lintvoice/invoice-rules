# An intra-Community supply gives no delivery country

The invoice is for an intra-Community supply, but it does not give the country of delivery.

## What the rule checks

Category K covers goods sold and sent to a business in another EU country, which accounts for the VAT there. The exemption rests on the goods leaving the seller's country for another EU country: the invoice says which. The rule checks that an invoice with a breakdown in K gives the deliver-to country code (BT-80).

## Why it matters

BR-IC-12 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-IC-12 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give the delivery address, with its country, even when it is the buyer's address.
2. If the address is entered but missing from the e-invoice, report it to the software's publisher, quoting BR-IC-12.

## Common causes

- **No delivery address written** when the goods go to the buyer's own address.

## Technical details

The deliver-to country code is BT-80, in the deliver-to address BG-15. In CII: `ram:CountryID` of `ram:ShipToTradeParty/ram:PostalTradeAddress` in `ram:ApplicableHeaderTradeDelivery`; in UBL: `cac:Delivery/cac:DeliveryLocation/cac:Address/cac:Country/cbc:IdentificationCode`.

The example invoice is all in K, and has no deliver-to party, so no deliver-to country; its fixed version has both, in the buyer's country.

## Official text

> In an Invoice with a VAT breakdown (BG-23) where the VAT category code (BT-118) is "Intra-community supply" the Deliver to country code (BT-80) shall not be blank.

BR-IC-12, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-IC-11](../BR-IC-11/): an invoice for an intra-Community supply (K) gives the actual delivery date, or the invoicing period.
- [BR-IC-02](../BR-IC-02/): an invoice with a line in the VAT category K (intra-Community supply) must give the seller's and the buyer's VAT numbers.
- [BR-IC-10](../BR-IC-10/): the VAT breakdown in category K (intra-Community supply) gives the reason no VAT is charged, as text or as a code.
