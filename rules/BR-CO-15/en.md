# The total with VAT is not the total without VAT plus the VAT

The invoice total with VAT is not equal to the total without VAT plus the VAT total.

## What the rule checks

The rule compares three amounts on the invoice: the total without VAT, the VAT total and the total with VAT. The total with VAT must be exactly the sum of the other two, to the cent.

## Why it matters

BR-CO-15 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard: an invoice that fails BR-CO-15 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Round the total without VAT and the VAT total to the cent.
2. Compute the total with VAT by adding these two rounded amounts, rather than computing it separately.
3. If your invoicing software computes the total with VAT another way, report it to the software's publisher, quoting BR-CO-15.

## Common causes

- **The VAT is not added:** the total with VAT repeats the total without VAT.
- **A one-cent rounding gap:** the total with VAT is computed from unrounded amounts.
- **A total changed by hand**, without updating the others.
- **An invoice in a foreign currency:** the software adds the VAT converted to euros instead of the VAT in the invoice currency.

## Technical details

The three amounts are the total without VAT (BT-109), the VAT total (BT-110) and the total with VAT (BT-112). When the invoice gives a VAT accounting currency (BT-6), BT-110 is the VAT total in the invoice currency, not the one in BT-6.

In CII, the rule compares `ram:GrandTotalAmount` with `ram:TaxBasisTotalAmount` plus `ram:TaxTotalAmount` (the one in the invoice currency); in UBL, `cbc:TaxInclusiveAmount` with `cbc:TaxExclusiveAmount` plus `cac:TaxTotal/cbc:TaxAmount`.

## Official text

> Invoice total amount with VAT (BT-112) = Invoice total amount without VAT (BT-109) + Invoice total VAT amount (BT-110).

BR-CO-15, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-CO-13](../BR-CO-13/): the total without VAT must be the sum of the lines, minus allowances and plus charges at invoice level.
- [BR-CO-14](../BR-CO-14/): the VAT total must be the sum of the VAT for each rate.
- [BR-CO-16](../BR-CO-16/): the amount due must be the total with VAT, minus what is already paid, plus rounding.
