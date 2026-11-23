# The seller's name is missing

The seller's name is empty.

## What the rule checks

An invoice names its seller: the company's name, or the person's for a sole trader. The rule checks that the e-invoice gives it.

## Why it matters

BR-06 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-06 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the seller's name in your software settings.
2. Check that the name printed on the PDF is also in the e-invoice.
3. If the name is missing from the e-invoice, report it to the software's publisher, quoting BR-06.

## Common causes

- **A logo instead of a name** on the PDF, with no name in the settings.
- **A name printed on the PDF** but not written in the e-invoice data.

## Technical details

The seller's name is BT-27. In CII, it is `ram:Name` of `ram:SellerTradeParty`; in UBL, `cbc:RegistrationName` of the party's `cac:PartyLegalEntity`.

The example invoice leaves the seller's name empty.

## Official text

> An Invoice shall contain the Seller name (BT-27).

BR-06, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-07](../BR-07/): every invoice must give the buyer's name.
- [BR-08](../BR-08/): every invoice must give the seller's postal address, with at least its country.
