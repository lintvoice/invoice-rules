# An invoice line has no VAT category

An invoice line does not give its VAT category.

## What the rule checks

Each line must give its VAT category: standard rate, zero rate, exemption, reverse charge… This is what lets the VAT be broken down by category and the totals be checked. The rule checks that each line carries a VAT category.

## Why it matters

BR-CO-04 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-04 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. In your software, check that each item or service has a VAT category, most often the standard rate.
2. Also check that the line's tax is declared as VAT, not as another tax.
3. If your software does not send the lines' VAT category, report it to the software's publisher, quoting BR-CO-04.

## Common causes

- **An item created without a VAT category** in the software.
- **A line tax declared with another type than VAT**, so its category is not read as a VAT category.

## Technical details

A line's VAT category is BT-151. In CII, the rule looks for `ram:CategoryCode` in the `ram:ApplicableTradeTax` of `ram:SpecifiedLineTradeSettlement` whose `ram:TypeCode` is `VAT`; in UBL, `cbc:ID` of `cac:Item/cac:ClassifiedTaxCategory` whose tax scheme is `VAT`.

A line with no category at all does not pass the Factur-X XML schema. The example invoice therefore declares the line's tax with the type `GST` instead of `VAT`, which also fails the CII syntax rule CII-DT-037 and a Factur-X profile rule.

## Official text

> Each Invoice line (BG-25) shall be categorized with an Invoiced item VAT category code (BT-151).

BR-CO-04, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-18](../BR-CO-18/): the invoice must have at least one VAT breakdown.
- [BR-CO-17](../BR-CO-17/): the VAT for each rate must be its taxable amount times the rate.
