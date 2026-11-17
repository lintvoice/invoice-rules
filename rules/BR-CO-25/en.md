# An amount due has neither a due date nor payment terms

The invoice leaves an amount to pay, but gives neither its payment due date nor its payment terms.

## What the rule checks

When the invoice leaves an amount to pay, it must say when or how to pay it: with a payment due date, with payment terms (for example "30 days end of month"), or both. An invoice already paid, whose amount due is zero, is not concerned.

## Why it matters

BR-CO-25 is a rule of the European e-invoicing standard, EN 16931. Since their version 1.3.16 (April 2026), the validation files published for this standard no longer check it ([release notes](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.16)); a public request opened on 18 October 2026 disputes this removal ([#541](https://github.com/ConnectingEurope/eInvoicing-EN16931/issues/541)). The rule is still applied, as blocking, by the rules of the EXTENDED-CTC-FR profile, one of the profiles the French reform admits, by the rules of the Factur-X EXTENDED profile and by the Peppol BIS Billing specification ([rule BR-CO-25](https://docs.peppol.eu/poacc/billing/3.0/rules/ubl-tc434/BR-CO-25/)).

Whatever rule is checked, the French Commercial Code requires the invoice to state the date by which payment is due ([article L441-9](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414397)).

## How to fix it

1. Give the invoice's payment due date, its payment terms, or both.
2. Check that they are sent in the e-invoice, not only printed on the PDF.
3. If your software does not send them, report it to the software's publisher, quoting BR-CO-25.

## Common causes

- **Payment terms printed on the PDF** but missing from the e-invoice data.
- **An invoice template without a due date** in the invoicing software.

## Technical details

The amount due for payment is BT-115, the payment due date BT-9 and the payment terms BT-20. In CII, the rule looks for `ram:DueDateDateTime` or `ram:Description` in `ram:SpecifiedTradePaymentTerms` when `ram:DuePayableAmount` is positive; in UBL, `cbc:DueDate` or `cac:PaymentTerms/cbc:Note` when `cac:LegalMonetaryTotal/cbc:PayableAmount` is positive. In UBL, it covers invoices only, not credit notes; in CII, every document type.

The example invoice is in the EXTENDED-CTC-FR profile, since an invoice in the EN 16931 profile is no longer checked on this rule by the current validation files.

## Official text

> In case the Amount due for payment (BT-115) is positive, either the Payment due date (BT-9) or the Payment terms (BT-20) shall be present.

BR-CO-25, [France_RFE EXTENDED-CTC-FR rules 1.4.0.04](https://github.com/fnfempe/France_RFE/blob/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d/FNFE_RFE_INVOICE/CII/EXTENDED-CTC-FR/schematron/EXTENDED-CTC-FR-CII.sch), CII and UBL.

## Related rules

- [BR-CO-16](../BR-CO-16/): the amount due must be the total with VAT, minus what is already paid, plus rounding.
- [BR-FR-CO-09](../BR-FR-CO-09/): an invoice already paid must give its payment due date and a zero amount due.
- [BR-FR-05](../BR-FR-05/): the invoice must carry the payment mentions (recovery indemnity, late-payment penalties, discount).
