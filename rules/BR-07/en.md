# The buyer's name is missing

The buyer's name is empty.

## What the rule checks

An invoice names its buyer: the company's name, or the person's for a sole trader. The rule checks that the e-invoice gives it.

## Why it matters

BR-07 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-07 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Fill in the buyer's name in your software's customer record.
2. Check that the name printed on the PDF is also in the e-invoice.
3. If the name is missing from the e-invoice, report it to the software's publisher, quoting BR-07.

## Common causes

- **A customer record created from an e-mail address**, without a name.
- **A name printed on the PDF** but not written in the e-invoice data.

## Technical details

The buyer's name is BT-44. In CII, it is `ram:Name` of `ram:BuyerTradeParty`; in UBL, `cbc:RegistrationName` of the party's `cac:PartyLegalEntity`.

The example invoice leaves the buyer's name empty.

## Official text

> An Invoice shall contain the Buyer name (BT-44).

BR-07, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-06](../BR-06/): every invoice must give the seller's name.
- [BR-10](../BR-10/): every invoice must give the buyer's postal address, with at least its country.
