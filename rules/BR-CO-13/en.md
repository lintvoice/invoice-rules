# The total without VAT is not the lines minus allowances plus charges

The invoice's total without VAT is not equal to the sum of the lines, minus the allowances on the whole invoice, plus its charges.

## What the rule checks

The total without VAT comes from three amounts: the sum of line net amounts, the total of allowances given on the whole invoice and the total of charges added to the whole invoice. The rule checks that the total without VAT is exactly the sum of the lines, minus the allowances, plus the charges, to the cent.

## Why it matters

BR-CO-13 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CO-13 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Compute the total without VAT from the totals already rounded: sum of the lines, minus the allowance total, plus the charge total.
2. Check that no allowance or charge was added after the total without VAT was computed.
3. If your software computes the total without VAT another way, report it to the software's publisher, quoting BR-CO-13.

## Common causes

- **An allowance or charge left out** of the total without VAT, or counted twice.
- **A prepayment taken off the total without VAT**, while an amount already paid comes off the amount due.
- **A rounding gap:** the total without VAT is computed from unrounded amounts.

## Technical details

The total without VAT is BT-109, the sum of line net amounts BT-106, the allowance total BT-107 and the charge total BT-108; when the last two are absent, the rule does not count them. The official message speaks of the sum of the lines (BT-131), but the test uses the sum of line net amounts (BT-106), which [BR-CO-10](../BR-CO-10/) ties to that sum. In CII: `ram:TaxBasisTotalAmount`, `ram:LineTotalAmount`, `ram:AllowanceTotalAmount` and `ram:ChargeTotalAmount` of `ram:SpecifiedTradeSettlementHeaderMonetarySummation`; in UBL: `cbc:TaxExclusiveAmount`, `cbc:LineExtensionAmount`, `cbc:AllowanceTotalAmount` and `cbc:ChargeTotalAmount` of `cac:LegalMonetaryTotal`.

## Official text

> Invoice total amount without VAT (BT-109) = Σ Invoice line net amount (BT-131) - Sum of allowances on document level (BT-107) + Sum of charges on document level (BT-108).

BR-CO-13, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-10](../BR-CO-10/): the sum of line net amounts must be the total of each line's net amount.
- [BR-CO-11](../BR-CO-11/): the allowance total must be the sum of the allowances on the whole invoice.
- [BR-CO-12](../BR-CO-12/): the charge total must be the sum of the charges on the whole invoice.
- [BR-CO-15](../BR-CO-15/): the total with VAT must be the total without VAT plus the VAT.
