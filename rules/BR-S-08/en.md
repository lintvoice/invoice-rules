# A rate's taxable amount is not the sum of its lines

For one of the invoice's VAT rates, the taxable amount does not match the lines, allowances and charges at that rate.

## What the rule checks

In the VAT breakdown, each rate has its taxable amount. The rule checks that it is the sum of the net amounts of the lines at that rate, plus the charges and minus the allowances on the whole invoice that have the same rate.

## Why it matters

BR-S-08 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-S-08 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. For each rate, add up the net amounts of the lines at that rate, add the charges and subtract the allowances at the same rate: that is the expected taxable amount.
2. Attach each allowance and charge on the whole invoice to the right VAT rate: a wrong rate distorts the taxable amount of two rates.
3. Compute the taxable amounts again after any change to the invoice: a line added or removed, an allowance added.
4. If your software computes the taxable amount another way, report it to the software's publisher, quoting BR-S-08.

## Common causes

- **An allowance on the whole invoice** deducted from the total but not from its rate's taxable amount.
- **An allowance attached to another rate** than that of the lines it concerns.
- **A taxable amount computed back from the total with VAT**, which does not land exactly on the sum of the lines.

## Technical details

A category's taxable amount is BT-116, for category S (any rate above zero) and its rate BT-119. It must equal the sum of the net amounts of the category S lines at that rate (BT-131), plus the document level charges (BT-99) and minus the document level allowances (BT-92) of the same category and rate. In CII: `ram:BasisAmount` of each `ram:ApplicableTradeTax` in `ram:ApplicableHeaderTradeSettlement` whose `ram:CategoryCode` is `S`; in UBL: `cbc:TaxableAmount` of each `cac:TaxSubtotal` of category `S`.

In CII, the rule requires an exact match, each sum rounded to the cent. In UBL, it accepts a gap strictly below 1 (one unit of the currency).

The example invoice states a taxable amount of 1,026.00 € for 1,025.00 € of lines at 20%. Its VAT amount, 205.00 €, is 0.20 € off the taxable amount times the rate: within the tolerance of BR-CO-17 and BR-S-09, which therefore do not fail.

## Official text

> For each different value of VAT category rate (BT-119) where the VAT category code (BT-118) is "Standard rated", the VAT category taxable amount (BT-116) in a VAT breakdown (BG-23) shall equal the sum of Invoice line net amounts (BT-131) plus the sum of document level charge amounts (BT-99) minus the sum of document level allowance amounts (BT-92) where the VAT category code (BT-151, BT-102, BT-95) is "Standard rated" and the VAT rate (BT-152, BT-103, BT-96) equals the VAT category rate (BT-119).

BR-S-08, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-17](../BR-CO-17/): a rate's VAT must be its taxable amount times the rate.
- [BR-S-09](../BR-S-09/): the same check as BR-CO-17, for category S.
- [BR-CO-13](../BR-CO-13/): the total without VAT must be the sum of the lines, minus the allowances, plus the charges.
