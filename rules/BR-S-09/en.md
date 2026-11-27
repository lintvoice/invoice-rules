# The VAT of a standard rate is not its taxable amount times the rate

For one of the invoice's VAT rates in category S, the VAT amount is not its taxable amount times the rate.

## What the rule checks

Category S covers VAT charged at a rate above zero, the reduced rates included. In the VAT breakdown, each rate in S has its taxable amount and its VAT amount. The rule checks that the VAT amount is the taxable amount times the rate, with a gap of less than 1 allowed (one unit of the currency).

## Why it matters

BR-S-09 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-S-09 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. For each rate, multiply the taxable amount by the rate and round to the cent: that is the expected VAT amount.
2. Compute the VAT on the taxable amount of each rate, not line by line.
3. If your software computes it another way, report it to the software's publisher, quoting BR-S-09.

## Common causes

- **VAT rounded line by line** and then added up, on an invoice with many lines.
- **A VAT amount typed by hand**, or not computed again after a change.

## Technical details

A category's taxable amount is BT-116, its VAT amount BT-117, its rate BT-119. In CII: `ram:CalculatedAmount`, `ram:BasisAmount` and `ram:RateApplicablePercent` of each `ram:ApplicableTradeTax` of `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `S`; in UBL: `cbc:TaxAmount`, `cbc:TaxableAmount` and `cac:TaxCategory/cbc:Percent` of each `cac:TaxSubtotal` of category `S`. BR-CO-17 makes the same check for every category, with a tolerance of 0.01: an amount 1 off or more fails both.

The example invoice is BR-CO-17's: its VAT amount at the standard rate is 1 more than the taxable amount times the rate, so both rules fail.

## Official text

> The VAT category tax amount (BT-117) in a VAT breakdown (BG-23) where VAT category code (BT-118) is "Standard rated" shall equal the VAT category taxable amount (BT-116) multiplied by the VAT category rate (BT-119).

BR-S-09, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-17](../BR-CO-17/): for each rate, the VAT amount must be the taxable amount times the rate, rounded to the cent.
- [BR-S-08](../BR-S-08/): for each rate, the taxable amount must be the sum of the lines at that rate, plus the charges and minus the allowances at the same rate.
- [BR-CO-14](../BR-CO-14/): the VAT total must be exactly the sum of the VAT amounts computed for each rate, to the cent.
