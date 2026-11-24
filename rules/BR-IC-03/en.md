# An allowance on an intra-Community supply requires both VAT numbers

The invoice has an allowance on the whole invoice in the VAT category K (intra-Community supply), but the buyer's VAT number is missing.

## What the rule checks

Category K covers goods sold and sent to a business in another EU country, which accounts for the VAT there. The exemption rests on the buyer's VAT number in another EU country. It shows that the buyer is a business that will account for the VAT. For each allowance in K, the rule checks that the invoice gives both VAT numbers. For the seller: its own (BT-31) or its tax representative's (BT-63). For the buyer: its VAT number (BT-48).

## Why it matters

BR-IC-03 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-IC-03 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Ask the buyer for its VAT number in its own country, and check it in the European Commission's VIES service.
2. Fill it in the buyer's record in your software, so that every invoice to that buyer carries it.
3. If the number is entered but missing from the e-invoice, report it to the software's publisher, quoting BR-IC-03.

## Common causes

- **A buyer's record without its VAT number**, created before the first sale abroad.
- **The buyer's VAT number printed on the PDF** but missing from the e-invoice data.

## Technical details

The document level allowance's VAT category is BT-95. The seller's VAT number is BT-31, its tax registration identifier BT-32, its tax representative's VAT number BT-63, the buyer's VAT number BT-48 and its legal registration identifier BT-47. In CII, the VAT numbers are `ram:SpecifiedTaxRegistration/ram:ID` with `schemeID` `VA` in `ram:SellerTradeParty`, `ram:SellerTaxRepresentativeTradeParty` and `ram:BuyerTradeParty`; in UBL, `cac:PartyTaxScheme/cbc:CompanyID` in `cac:AccountingSupplierParty`, `cac:TaxRepresentativeParty` and `cac:AccountingCustomerParty`. BR-IC-02, BR-IC-03 and BR-IC-04 run the same test, from a line, an allowance and a charge: an invoice that fails this rule also fails BR-IC-02 as soon as one of its lines is in K.

The example invoice is all in K, with an allowance in K, and the buyer has no VAT number; its fixed version gives it. It fails BR-IC-02 too.

## Official text

> An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Intra-community supply" shall contain the Seller VAT Identifier (BT-31) or the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48).

BR-IC-03, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-IC-02](../BR-IC-02/): an invoice with a line in the VAT category K (intra-Community supply) must give the seller's and the buyer's VAT numbers.
- [BR-IC-04](../BR-IC-04/): an invoice with a charge on the whole invoice in the VAT category K (intra-Community supply) must give the seller's and the buyer's VAT numbers.
- [BR-S-02](../BR-S-02/): an invoice with lines subject to VAT must give the seller's VAT number in its data, not only on the PDF.
