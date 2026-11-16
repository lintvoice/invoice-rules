# The VAT total is not the sum of the VAT for each rate

The invoice's VAT total is not equal to the sum of the VAT amounts computed for each rate.

## What the rule checks

The invoice details its VAT by rate, for example 20% and 5.5%: for each, the taxable amount and the VAT amount. This is the VAT breakdown. The rule checks that the invoice's VAT total is exactly the sum of these amounts, to the cent.

## Why it matters

BR-CO-14 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-14 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Compute the VAT amount for each rate, rounded to the cent.
2. Add these amounts up to get the VAT total, rather than computing the VAT on the total without VAT.
3. If your software computes the VAT total another way, report it to the software's publisher, quoting BR-CO-14.

## Common causes

- **VAT computed on the total without VAT** instead of added up rate by rate: the rounding can differ by a cent.
- **VAT computed line by line** and added up, while the breakdown computes it by rate.
- **A VAT total in another currency** (see the technical details).

## Technical details

The VAT total is BT-110, each category's VAT amount BT-117 (group BG-23). In CII, the rule compares the `ram:TaxTotalAmount` whose `currencyID` is the invoice currency with the sum of the `ram:CalculatedAmount` of the `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`; a second `ram:TaxTotalAmount`, in the VAT accounting currency (BT-111), is not part of this comparison. In UBL, it compares `cac:TaxTotal/cbc:TaxAmount` with the sum of the `cac:TaxSubtotal/cbc:TaxAmount` in the same `cac:TaxTotal`.

## Official text

> Invoice total VAT amount (BT-110) = Σ VAT category tax amount (BT-117).

BR-CO-14, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-15](../BR-CO-15/): the total with VAT must be the total without VAT plus the VAT.
- [BR-CO-17](../BR-CO-17/): the VAT for each rate must be its taxable amount times the rate.
