# An exempt line must have a 0 % rate

An exempt line has a VAT rate other than 0 %.

## What the rule checks

Category E covers supplies the law exempts from VAT, such as the transport of goods being exported. No VAT is charged on the invoice, so the rate is 0 %. The rule checks that the rate (BT-152) of each invoice line in E is 0.

## Why it matters

BR-E-05 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-E-05 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Set the VAT rate to 0 % on the items in category E.
2. If VAT does apply at another rate, the category is not E: give the item its right category.
3. If your software keeps the standard rate, report it to the software's publisher, quoting BR-E-05.

## Common causes

- **The category changed but not the rate**: an item's standard rate kept when it moves to another category.
- **A rate copied from the item's catalogue record**, whatever the invoice's category.

## Technical details

The invoice line's VAT category is BT-151, its VAT rate BT-152. In CII: `ram:RateApplicablePercent` of the line's `ram:ApplicableTradeTax`; in UBL: `cbc:Percent` of `cac:Item/cac:ClassifiedTaxCategory`.

The example invoice is all in E, and its first line keeps the standard rate while its category is E; the VAT breakdown is still at 0 %. Its fixed version gives 0 %.

## Official text

> In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Exempt from VAT", the Invoiced item VAT rate (BT-152) shall be 0 (zero).

BR-E-05, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-E-06](../BR-E-06/): in the VAT category E (exempt), the VAT rate of a document level allowance is 0 %.
- [BR-E-07](../BR-E-07/): in the VAT category E (exempt), the VAT rate of a document level charge is 0 %.
- [BR-S-05](../BR-S-05/): in the VAT category S (standard rate), the VAT rate of an invoice line is above zero: a 0 % rate belongs to another category.
