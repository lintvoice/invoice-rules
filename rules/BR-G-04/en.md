# A charge on an export requires the seller's VAT number

The invoice has a charge on the whole invoice in the VAT category G (export outside the EU), but the seller's VAT number is missing.

## What the rule checks

Category G covers goods sent to a buyer outside the European Union, exempt from VAT. A business that makes supplies in category G is identified for VAT, and its invoice says so. For each charge in G, the rule checks that the invoice gives the seller's VAT number (BT-31) or its tax representative's (BT-63).

## Why it matters

BR-G-04 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-G-04 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. In your company's record in your software, fill in your VAT number.
2. Check that it is sent in the e-invoice, not only printed on the PDF.
3. If your software does not send it, report it to the software's publisher, quoting BR-G-04.

## Common causes

- **A VAT number printed in the PDF's footer** but missing from the e-invoice data.
- **An incomplete company record** in the invoicing software.

## Technical details

The document level charge's VAT category is BT-102. The seller's VAT number is BT-31, its tax registration identifier BT-32, its tax representative's VAT number BT-63, the buyer's VAT number BT-48 and its legal registration identifier BT-47. In CII, the VAT numbers are `ram:SpecifiedTaxRegistration/ram:ID` with `schemeID` `VA` in `ram:SellerTradeParty`, `ram:SellerTaxRepresentativeTradeParty` and `ram:BuyerTradeParty`; in UBL, `cac:PartyTaxScheme/cbc:CompanyID` in `cac:AccountingSupplierParty`, `cac:TaxRepresentativeParty` and `cac:AccountingCustomerParty`. BR-G-02, BR-G-03 and BR-G-04 run the same test, from a line, an allowance and a charge: an invoice that fails this rule also fails BR-G-02 as soon as one of its lines is in G.

The example invoice is all in G, with a charge in G, and the seller has no VAT number; its fixed version gives it. It fails BR-G-02 too.

## Official text

> An Invoice that contains a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Export outside the EU" shall contain the Seller VAT Identifier (BT-31) or the Seller tax representative VAT identifier (BT-63).

BR-G-04, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-G-02](../BR-G-02/): an invoice with a line in the VAT category G (export outside the EU) must give the seller's VAT number, or its tax representative's.
- [BR-G-03](../BR-G-03/): an invoice with an allowance on the whole invoice in the VAT category G (export outside the EU) must give the seller's VAT number, or its tax representative's.
- [BR-S-02](../BR-S-02/): an invoice with lines subject to VAT must give the seller's VAT number in its data, not only on the PDF.
