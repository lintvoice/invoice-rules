# A line's gross price is negative

A line gives a gross price below zero.

## What the rule checks

A line can give the item's gross price, its catalogue price, and the price discount that leads to the net price. The rule checks that the gross price is not negative. A return or a refund is written as a credit note, or as a negative quantity, not as a negative price.

## Why it matters

BR-28 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-28 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Check the sign of the gross price in your software: it is always zero or more.
2. For a return, issue a credit note, or a line with a negative quantity.
3. If the gross price comes out negative, report it to the software's publisher, quoting BR-28.

## Common causes

- **A minus sign carried over** from the price discount to the gross price.
- **A return typed with a negative price** instead of a negative quantity.

## Technical details

The item gross price is BT-148. In CII, it is `ram:ChargeAmount` of `ram:GrossPriceProductTradePrice` in the line's `ram:SpecifiedLineTradeAgreement`; in UBL, `cbc:BaseAmount` of the `cac:AllowanceCharge` in the line's `cac:Price`.

The example invoice writes its first line's gross price with a minus sign; its price discount and net price stay right, so it fails BR-28 alone.

## Official text

> The Item gross price (BT-148) shall NOT be negative.

BR-28, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-27](../BR-27/): a line's net unit price cannot be negative: enter a discount as an allowance, not as a line at a negative price.
- [BR-FR-DEC-03](../BR-FR-DEC-03/): unit prices must have at most 6 decimals and no minus sign, except with the billing framework B9, S9 or M9.
