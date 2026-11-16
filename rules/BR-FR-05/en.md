# A mandatory statement is missing: recovery costs, late-payment penalties or discount

The e-invoice does not contain one of the three mandatory payment statements as a coded note.

## What the rule checks

The invoice must contain three notes, each marked with a code:

- **PMT**: the fixed indemnity for recovery costs in case of late payment;
- **PMD**: the late-payment penalties;
- **AAB**: the early-payment discount conditions, or the fact that there is none.

It is not enough for the text to appear somewhere: each statement must be in a note that carries its code.

## Why it matters

BR-FR-05 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

These three statements are mandatory on invoices in France ([Commercial Code, article L441-9, in French](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414397); [Service-Public, in French](https://entreprendre.service-public.gouv.fr/vosdroits/F31808)). The rule requires them as coded notes, which software can read.

## How to fix it

1. In your software, check the payment statements on your invoices: the late-payment penalty rate, the €40 fixed indemnity, the discount (or "Escompte pour paiement anticipé : néant").
2. Check that they are sent as coded notes PMD, PMT and AAB in the e-invoice, not only printed on the PDF.
3. If your software cannot code these notes, report it to the software's publisher, quoting BR-FR-05.

## Common causes

- **The statements are in the PDF footer** but not in the invoice's XML file.
- **The three statements are grouped in one note**, with no code or a single code.
- **The absence of a discount is not stated**: the AAB statement is required even with no discount.

## Technical details

Notes are group BG-1: subject code BT-21, text BT-22. In CII, a `ram:IncludedNote` whose `ram:SubjectCode` is `PMT`, `PMD` or `AAB` (UNTDID 4451 codes). UBL notes have no subject code: the official files look for `#PMT#`, `#PMD#` and `#AAB#` in the note text (`cbc:Note`).

## Official text

> La mention relative aux frais de recouvrement (code PMT) est absente. Elle est obligatoire dans les notes (BG-1).

BR-FR-05, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-05_BT-22-1`, `BR-FR-05_BT-22-2`, `BR-FR-05_BT-22-3`, `BR-FR-05_BT-22_AAB`, `BR-FR-05_BT-22_PMD`, `BR-FR-05_BT-22_PMT`.

## Related rules

- [BR-FR-06](../BR-FR-06/): each coded statement appears only once.
