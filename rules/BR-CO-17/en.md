# A rate's VAT is not its taxable amount times the rate

For one of the invoice's VAT rates, the VAT amount is not its taxable amount times the rate.

## What the rule checks

In the VAT breakdown, each rate has its taxable amount and its VAT amount. The rule checks that this amount matches the taxable amount times the rate, rounded to the cent, with a small tolerance (see the technical details).

## Why it matters

BR-CO-17 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-17 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. For each rate, multiply the taxable amount by the rate and round the result to the cent.
2. Compute the VAT again after any change to the taxable amount: an allowance added, a line removed.
3. If your software computes the VAT another way, report it to the software's publisher, quoting BR-CO-17.

## Common causes

- **A taxable amount changed without computing the VAT again**, after an allowance was added or a line removed.
- **A wrong rate used** in the computation, while the breakdown shows the right one.
- **Another rate's VAT carried** onto this rate.

## Technical details

A category's VAT amount is BT-117, its taxable amount BT-116 and its rate BT-119. In CII: `ram:CalculatedAmount`, `ram:BasisAmount` and `ram:RateApplicablePercent` of each `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement`; in UBL: `cbc:TaxAmount`, `cbc:TaxableAmount` and `cac:TaxCategory/cbc:Percent` of each `cac:TaxSubtotal`.

The rule accepts a gap of up to 1 (one unit of the currency, 1 € for an invoice in euros), bounds included. When the rate is zero, it requires a zero VAT amount. For the standard rate, BR-S-09 makes the same check with a gap strictly below 1: a gap of exactly 1 € fails BR-S-09 alone, and beyond that both rules fail, as in the example invoice (a 2 € gap).

## Official text

> VAT category tax amount (BT-117) = VAT category taxable amount (BT-116) x (VAT category rate (BT-119) / 100), rounded to two decimals.

BR-CO-17, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-14](../BR-CO-14/): the VAT total must be the sum of the VAT for each rate.
- [BR-S-09](../BR-S-09/): the same check as BR-CO-17, for the standard rate.
