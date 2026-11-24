# An allowance on an export must have a 0 % rate

An allowance on an export has a VAT rate other than 0 %.

## What the rule checks

Category G covers goods sent to a buyer outside the European Union, exempt from VAT. No VAT is charged on the invoice, so the rate is 0 %. The rule checks that the rate (BT-96) of each document level allowance in G is 0.

## Why it matters

BR-G-06 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-G-06 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Set the VAT rate to 0 % on the items in category G.
2. If VAT does apply at another rate, the category is not G: give the item its right category.
3. If your software keeps the standard rate, report it to the software's publisher, quoting BR-G-06.

## Common causes

- **The category changed but not the rate**: an item's standard rate kept when it moves to another category.
- **A rate copied from the item's catalogue record**, whatever the invoice's category.

## Technical details

The document level allowance's VAT category is BT-95, its VAT rate BT-96. In CII: `ram:RateApplicablePercent` of the `ram:CategoryTradeTax` of each `ram:SpecifiedTradeAllowanceCharge` whose `ram:ChargeIndicator` is false; in UBL: `cbc:Percent` of the `cac:TaxCategory` of each `cac:AllowanceCharge` whose `cbc:ChargeIndicator` is false.

The example invoice is all in G, and its allowance keeps the standard rate while its category is G; the VAT breakdown is still at 0 %. Its fixed version gives 0 %.

## Official text

> In a Document level allowance (BG-20) where the Document level allowance VAT category code (BT-95) is "Export outside the EU" the Document level allowance VAT rate (BT-96) shall be 0 (zero).

BR-G-06, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-G-05](../BR-G-05/): in the VAT category G (export outside the EU), the VAT rate of an invoice line is 0 %.
- [BR-G-07](../BR-G-07/): in the VAT category G (export outside the EU), the VAT rate of a document level charge is 0 %.
- [BR-S-05](../BR-S-05/): in the VAT category S (standard rate), the VAT rate of an invoice line is above zero: a 0 % rate belongs to another category.
