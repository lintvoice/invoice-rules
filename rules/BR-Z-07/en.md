# A zero-rated charge must have a 0% rate

A zero-rated charge has a VAT rate other than 0%.

## What the rule checks

Category Z covers supplies taxed at a rate of 0%, such as solar panels sold to their operator in Germany. No VAT is charged in this category, so the rate is 0%. The rule checks that the rate (BT-103) of each document level charge in Z is 0.

## Why it matters

BR-Z-07 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-Z-07 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Set the VAT rate to 0% on the items in category Z.
2. If VAT does apply at another rate, the category is not Z: give the item its right category.
3. If your software keeps the standard rate, report it to the software's publisher, quoting BR-Z-07.

## Common causes

- **The category changed but not the rate**: an item's standard rate kept when it moves to another category.
- **A rate copied from the item's catalogue record**, whatever the invoice's category.

## Technical details

The document level charge's VAT category is BT-102, its VAT rate BT-103. In CII: `ram:RateApplicablePercent` of the `ram:CategoryTradeTax` of each `ram:SpecifiedTradeAllowanceCharge` whose `ram:ChargeIndicator` is true; in UBL: `cbc:Percent` of the `cac:TaxCategory` of each `cac:AllowanceCharge` whose `cbc:ChargeIndicator` is true.

The example invoice is all in Z, and its charge keeps the standard rate while its category is Z; the VAT breakdown is still at 0%. Its fixed version gives 0%.

## Official text

> In a Document level charge (BG-21) where the Document level charge VAT category code (BT-102) is "Zero rated" the Document level charge VAT rate (BT-103) shall be 0 (zero).

BR-Z-07, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-Z-05](../BR-Z-05/): in the VAT category Z (zero rate), the VAT rate of an invoice line is 0%.
- [BR-Z-06](../BR-Z-06/): in the VAT category Z (zero rate), the VAT rate of a document level allowance is 0%.
- [BR-S-05](../BR-S-05/): in the VAT category S (standard rate), the VAT rate of an invoice line is above zero: a 0% rate belongs to another category.
