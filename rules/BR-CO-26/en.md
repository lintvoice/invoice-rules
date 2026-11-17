# The seller has no identifier

The invoice gives no identifier of the seller.

## What the rule checks

For the buyer to recognise the supplier automatically, the invoice must identify the seller by at least one of these numbers: an identifier (in France, the SIRET), a registration number (in France, the SIREN) or a VAT identification number. The rule checks that at least one of the three is present.

## Why it matters

BR-CO-26 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-26 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. In your company's record, fill in your SIREN, your SIRET and your VAT number.
2. Check that they are sent in the e-invoice, not only printed on the PDF.
3. If your software does not send them, report it to the software's publisher, quoting BR-CO-26.

## Common causes

- **An incomplete company record** in the invoicing software.
- **Identifiers printed on the PDF** but missing from the e-invoice data.

## Technical details

The seller's identifiers are BT-29 (identifier, in France the SIRET with scheme 0009), BT-30 (legal registration identifier, in France the SIREN with scheme 0002) and BT-31 (VAT identifier). In CII, the rule looks for `ram:ID`, `ram:GlobalID`, `ram:SpecifiedLegalOrganization/ram:ID` or `ram:SpecifiedTaxRegistration/ram:ID` with `schemeID` `VA` in `ram:SellerTradeParty`; in UBL, `cac:PartyIdentification/cbc:ID` (except scheme `SEPA`), `cac:PartyLegalEntity/cbc:CompanyID` or `cac:PartyTaxScheme/cbc:CompanyID` (scheme `VAT`) in `cac:AccountingSupplierParty/cac:Party`.

In France, an invoice with no seller identifier at all also fails BR-FR-10, which requires the SIREN, and BR-S-02, which requires a seller VAT identifier when lines are at the standard rate. The example invoice therefore fails these three rules.

## Official text

> In order for the buyer to automatically identify a supplier, the Seller identifier (BT-29), the Seller legal registration identifier (BT-30) and/or the Seller VAT identifier (BT-31) shall be present.

BR-CO-26, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-FR-10](../BR-FR-10/): the seller's SIREN is required and must have 9 digits.
- [BR-CO-09](../BR-CO-09/): a VAT number must start with a country code.
