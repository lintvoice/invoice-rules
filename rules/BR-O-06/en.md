# An allowance outside the scope of VAT has no VAT rate

An allowance outside the scope of VAT gives a VAT rate.

## What the rule checks

Category O covers operations no VAT applies to, such as a service supplied to a business outside the EU. VAT does not apply, so there is no rate to give. The rule checks that a document level allowance in O has no VAT rate (BT-96).

## Why it matters

BR-O-06 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-O-06 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Leave the VAT rate empty for items outside the scope of VAT: no rate, rather than 0 %.
2. If your software always writes a rate, report it to the software's publisher, quoting BR-O-06.

## Common causes

- **Software that always writes a rate**, 0 % when no VAT applies.

## Technical details

The document level allowance's VAT category is BT-95, its VAT rate BT-96. In CII: `ram:RateApplicablePercent` of the `ram:CategoryTradeTax` of each `ram:SpecifiedTradeAllowanceCharge` whose `ram:ChargeIndicator` is false; in UBL: `cbc:Percent` of the `cac:TaxCategory` of each `cac:AllowanceCharge` whose `cbc:ChargeIndicator` is false.

The example invoice is all outside the scope of VAT, and gives its allowance a 0 % rate; its fixed version gives none.

## Official text

> A Document level allowance (BG-20) where VAT category code (BT-95) is "Not subject to VAT" shall not contain a Document level allowance VAT rate (BT-96).

BR-O-06, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-O-05](../BR-O-05/): an invoice line outside the scope of VAT (O) gives no VAT rate, not even 0 %.
- [BR-O-07](../BR-O-07/): a document level charge outside the scope of VAT (O) gives no VAT rate, not even 0 %.
- [BR-S-05](../BR-S-05/): in the VAT category S (standard rate), the VAT rate of an invoice line is above zero: a 0 % rate belongs to another category.
