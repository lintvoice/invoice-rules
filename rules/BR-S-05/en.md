# A standard-rated line must have a rate above zero

A standard-rated line has a VAT rate of 0 %.

## What the rule checks

Category S covers VAT charged at a rate above zero, the reduced rates included. A supply at 0 % belongs to another category: Z if it is taxed at a rate of zero, E if the law exempts it. AE, K and G are for reverse charge, intra-Community supplies and exports. The rule checks that the rate (BT-152) of each invoice line in S is above zero.

## Why it matters

BR-S-05 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-S-05 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Give the item its real VAT rate, the standard or a reduced one.
2. If no VAT applies, give it the category that says why (Z, E, AE, K, G or O), with a reason if needed.
3. If your software writes 0 % under category S, report it to the software's publisher, quoting BR-S-05.

## Common causes

- **A free or exempt item** left in the default category S with a 0 % rate.
- **Category S used for every line**, whatever the rate, by a template or an export.

## Technical details

The invoice line's VAT category is BT-151, its VAT rate BT-152. In CII: `ram:RateApplicablePercent` of the line's `ram:ApplicableTradeTax`; in UBL: `cbc:Percent` of `cac:Item/cac:ClassifiedTaxCategory`.

The example invoice gives the first line the category S and a 0 % rate, and its VAT breakdown follows: a row for S at 0 %. Its fixed version applies the standard rate.

## Official text

> In an Invoice line (BG-25) where the Invoiced item VAT category code (BT-151) is "Standard rated" the Invoiced item VAT rate (BT-152) shall be greater than zero.

BR-S-05, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-S-06](../BR-S-06/): in the VAT category S (standard rate), the VAT rate of a document level allowance is above zero: a 0 % rate belongs to another category.
- [BR-S-07](../BR-S-07/): in the VAT category S (standard rate), the VAT rate of a document level charge is above zero: a 0 % rate belongs to another category.
- [BR-Z-05](../BR-Z-05/): in the VAT category Z (zero rate), the VAT rate of an invoice line is 0 %.
