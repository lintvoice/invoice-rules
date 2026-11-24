# An allowance outside the scope of VAT, yet a VAT number on the invoice

The invoice has an allowance on the whole invoice outside the scope of VAT, but it gives a VAT number.

## What the rule checks

Category O covers operations no VAT applies to, such as a service supplied to a business outside the EU. Outside the scope of VAT, the invoice is not about VAT at all. It gives no VAT number: not the seller's, its tax representative's or the buyer's. The rule checks it from each allowance in O.

## Why it matters

BR-O-03 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-O-03 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check that the operation is really outside the scope of VAT. If it is a taxed, exempt or zero-rated supply, give it that category instead of O.
2. If it is outside the scope of VAT, leave the VAT numbers out of this invoice, the seller's included. A tax registration identifier (BT-32), such as a German tax number, is allowed.
3. If your software writes the seller's VAT number anyway, report it to the software's publisher, quoting BR-O-03.

## Common causes

- **The seller's VAT number written on every invoice** by the software, from the company's settings.
- **Category O used for an exempt supply**, which would be category E, with the seller's VAT number.

## Technical details

The document level allowance's VAT category is BT-95. The seller's VAT number is BT-31, its tax registration identifier BT-32, its tax representative's VAT number BT-63, the buyer's VAT number BT-48 and its legal registration identifier BT-47. In CII, the VAT numbers are `ram:SpecifiedTaxRegistration/ram:ID` with `schemeID` `VA` in `ram:SellerTradeParty`, `ram:SellerTaxRepresentativeTradeParty` and `ram:BuyerTradeParty`; in UBL, `cac:PartyTaxScheme/cbc:CompanyID` in `cac:AccountingSupplierParty`, `cac:TaxRepresentativeParty` and `cac:AccountingCustomerParty`. BR-O-02, BR-O-03 and BR-O-04 run the same test, from a line, an allowance and a charge: an invoice that fails this rule also fails BR-O-02 as soon as one of its lines is in O.

The example invoice is all outside the scope of VAT, with an allowance in O, and the seller gives its VAT number; its fixed version leaves it out and keeps the seller's German tax number (Steuernummer) as its tax registration identifier (BT-32, `schemeID` `FC` in CII), which the rule allows. It fails BR-O-02 too.

## Official text

> An Invoice that contains a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Not subject to VAT" shall not contain the Seller VAT identifier (BT-31), the Seller tax representative VAT identifier (BT-63) or the Buyer VAT identifier (BT-48).

BR-O-03, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-O-02](../BR-O-02/): an invoice with a line outside the scope of VAT (O) must give no VAT number: not the seller's, not its tax representative's, not the buyer's.
- [BR-O-04](../BR-O-04/): an invoice with a charge on the whole invoice outside the scope of VAT (O) must give no VAT number: not the seller's, not its tax representative's, not the buyer's.
- [BR-S-02](../BR-S-02/): an invoice with lines subject to VAT must give the seller's VAT number in its data, not only on the PDF.
