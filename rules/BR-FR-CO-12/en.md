# An invoice in a foreign currency does not give the VAT in euros

The invoice is in a currency other than the euro, but does not give the VAT in euros.

## What the rule checks

An invoice may be issued in a currency other than the euro. In that case, the rule requires:

- the VAT accounting currency, equal to EUR;
- the VAT total expressed in euros.

## Why it matters

BR-FR-CO-12 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. For an invoice in a foreign currency, set EUR as the VAT accounting currency in your software.
2. Have the VAT total converted into euros and sent with the invoice.
3. If your software cannot do this, report it to the software's publisher, quoting BR-FR-CO-12.

## Common causes

- **An invoice in dollars or pounds** with no VAT converted.
- **The VAT accounting currency given**, but not the amount in euros.

## Technical details

If BT-5 (invoice currency) is not `EUR`: BT-6 (VAT accounting currency) = `EUR`, and BT-111 (VAT total in accounting currency) present with `currencyID="EUR"`. In CII, BT-111 is the second `ram:TaxTotalAmount`, in the accounting currency.

## Official text

> Si la devise de facture (BT-5) est différente de EUR, alors : - la devise de comptabilité (BT-6) doit être présente et égale à EUR, - le montant de TVA en devise de comptabilité (BT-111) doit être renseigné, - et sa devise (BT-111-1) doit être égale à EUR.

BR-FR-CO-12, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-CO-12_BT-5`.

## Related rules

No closely related rule.
