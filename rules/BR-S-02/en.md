# The seller's VAT number is missing

Lines of the invoice are subject to VAT, but the invoice does not give the seller's VAT number.

## What the rule checks

As soon as a line is subject to VAT at a rate above zero, the invoice must identify the seller for VAT: their VAT number, or their tax representative's if they have one.

## Why it matters

BR-S-02 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-S-02 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. In your company's settings, fill in your VAT number.
2. Check that it is sent in the e-invoice, not only printed on the PDF.
3. If your business charges no VAT (the French VAT franchise, for example), your lines must not be declared as subject to VAT: they are exempt, with the reason of the franchise (see BR-E-10).
4. If your software does not send your VAT number, report it to the software's publisher, quoting BR-S-02.

## Common causes

- **A VAT number printed in the PDF footer** but missing from the e-invoice data.
- **Incomplete company settings** in the invoicing software.
- **A seller under the VAT franchise**, without a VAT number, whose software declares the lines as subject to VAT.

## Technical details

A line's VAT category is BT-151. Category S ("Standard rated") is the one for any rate above zero, reduced rates included (BR-S-05 requires a positive rate). The seller's VAT number is BT-31, their tax registration identifier BT-32, their tax representative's VAT number BT-63.

In CII, the rule starts from each line `ram:ApplicableTradeTax` whose `ram:CategoryCode` is `S`, and looks for `ram:SpecifiedTaxRegistration/ram:ID` with `schemeID` `VA` or `FC` in `ram:SellerTradeParty`, or with `schemeID` `VA` in `ram:SellerTaxRepresentativeTradeParty`; in UBL, for `cac:PartyTaxScheme/cbc:CompanyID` in `cac:AccountingSupplierParty/cac:Party`, or that of `cac:TaxRepresentativeParty`. BR-S-03 and BR-S-04 make the same check for an allowance or a charge on the whole invoice.

For the French VAT franchise, the VATEX list of exemption reason codes (BT-121) has `VATEX-FR-FRANCHISE`. An invoice without any seller identifier also fails BR-CO-26 and, in France, BR-FR-10; the example invoice keeps the seller's SIREN and SIRET and fails BR-S-02 only.

## Official text

> An Invoice that contains an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Standard rated" shall contain the Seller VAT Identifier (BT-31), the Seller tax registration identifier (BT-32) and/or the Seller tax representative VAT identifier (BT-63).

BR-S-02, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-26](../BR-CO-26/): the seller must have at least one identifier.
- [BR-CO-09](../BR-CO-09/): a VAT number must start with a country code.
- [BR-E-10](../BR-E-10/): a VAT exemption must give its reason.
