# A VAT category has no rate

A VAT breakdown gives no rate.

## What the rule checks

The VAT breakdown gives, for each VAT category and rate of the invoice, its taxable amount, its VAT amount, its category and its rate. The rule checks that each one gives its rate, 0 for an exempt category; only the category O, outside the scope of VAT, has none.

## Why it matters

BR-48 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-48 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. For an exempt category, or a rate of 0 %, write the rate 0.
2. Check that the e-invoice writes the VAT breakdown in full, one block per category and rate.
3. If it is missing from the e-invoice, report it to the software's publisher, quoting BR-48.

## Common causes

- **A rate left out because it is 0**, for an exempt line.
- **A VAT breakdown built by hand** in an export, field by field.

## Technical details

A VAT breakdown is group BG-23, here its VAT rate BT-119. In CII, it is `ram:RateApplicablePercent` of each `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`; in UBL, `cac:TaxCategory/cbc:Percent` of each `cac:TaxSubtotal`.

The rule makes one exception: the category O, services outside the scope of VAT, which has no rate. An exempt category, E, has one: 0.

The example invoice has an exempt line whose VAT breakdown gives no rate, so it fails BR-48 alone.

## Official text

> Each VAT breakdown (BG-23) shall have a VAT category rate (BT-119), except if the Invoice is not subject to VAT.

BR-48, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-47](../BR-47/): each VAT breakdown must give its VAT category: standard rate, exempt, reverse charge…
