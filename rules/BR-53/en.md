# The VAT total in the VAT accounting currency is missing

The invoice names a VAT accounting currency, but gives no VAT total in it.

## What the rule checks

An invoice in a foreign currency, US dollars for example, can name the currency in which the seller accounts for VAT, euros for example. When it does, the rule checks that the invoice also gives its VAT total in that currency. In CII, that currency must also differ from the invoice's own.

## Why it matters

BR-53 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-53 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. For an invoice in a foreign currency, give the VAT total converted into your accounting currency.
2. For an invoice in your own currency, leave the VAT accounting currency out.
3. If your software writes it anyway, report it to the software's publisher, quoting BR-53.

## Common causes

- **The accounting currency filled in by default**, on every invoice, even in the invoice's own currency.
- **The VAT converted on the PDF only.**

## Technical details

The VAT accounting currency code is BT-6, the VAT total in that currency BT-111. In CII, the rule looks for a `ram:TaxTotalAmount` whose `currencyID` is `ram:TaxCurrencyCode`, and requires that code to differ from `ram:InvoiceCurrencyCode`: with the same currency, the VAT total in the accounting currency cannot be told apart from the VAT total in the invoice currency (BT-110), which BR-CO-15 allows once. In UBL, it looks for a `cac:TaxTotal` whose `cbc:TaxAmount` is in `cbc:TaxCurrencyCode`.

The example invoice names its own currency as VAT accounting currency, so it fails BR-53 alone.

## Official text

> If the VAT accounting currency code (BT-6) is present, then the Invoice total VAT amount in accounting currency (BT-111) shall be provided.

BR-53, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-DEC-15](../BR-DEC-15/): the VAT total in the VAT accounting currency must be rounded to the cent, with at most 2 decimals.
- [BR-CL-05](../BR-CL-05/): the currency in which the seller accounts for VAT must be a three-letter ISO 4217 code, such as EUR.
- [BR-FR-CO-12](../BR-FR-CO-12/): when the invoice is not in euros, it must give the VAT accounting currency (EUR) and the VAT total in euros.
