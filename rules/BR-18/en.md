# The tax representative has no name

The invoice names a tax representative of the seller, but its name is empty.

## What the rule checks

Some sellers act through a tax representative, a company that handles their VAT in a country where they are not established. When the invoice names one, the rule checks that it gives the representative's name.

## Why it matters

BR-18 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-18 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the tax representative's name in your software.
2. Check that the e-invoice gives the representative's name, postal address with its country, and VAT number.
3. If they are missing from the e-invoice, report it to the software's publisher, quoting BR-18.

## Common causes

- **The representative's name kept only in a letterhead**, not in the software's data.
- **A representative entered with its VAT number only**, its other details left in another tool.

## Technical details

The seller tax representative is group BG-11, its name BT-62. In CII, it is `ram:Name` of `ram:SellerTaxRepresentativeTradeParty`, in `ram:ApplicableHeaderTradeAgreement`; in UBL, `cbc:Name` of `cac:PartyName` in `cac:TaxRepresentativeParty`.

The example invoice names a tax representative whose name is empty, so it fails BR-18 alone.

## Official text

> The Seller tax representative name (BT-62) shall be provided in the Invoice, if the Seller (BG-4) has a Seller tax representative party (BG-11).

BR-18, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-19](../BR-19/): when the seller has a tax representative, the invoice must give its postal address.
- [BR-20](../BR-20/): when the seller has a tax representative, its postal address must give its country, with its two-letter code.
- [BR-56](../BR-56/): when the seller has a tax representative, the invoice must give the representative's VAT number.
