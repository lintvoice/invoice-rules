# More than one attachment is described as LISIBLE

Two or more attachments to the invoice are described as LISIBLE.

## What the rule checks

An attachment described as LISIBLE is the readable version of the invoice, such as a PDF attached to an XML invoice. The rule allows only one per invoice.

## Why it matters

BR-FR-18 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Keep a single LISIBLE attachment: the readable copy of the invoice itself.
2. Describe the other attachments with their own code, such as DOCUMENT_ANNEXE or BON_LIVRAISON.
3. If your software marks every attachment LISIBLE, report it to the software's publisher, quoting BR-FR-18.

## Common causes

- **The readable PDF attached twice.**
- **Every attachment described LISIBLE** by default.

## Technical details

The rule counts the supporting documents (group BG-24) whose description BT-123 is `LISIBLE`: at most one.

## Official text

> Il ne peut y avoir **qu’un seul** document additionnel (BG-24) dont la description (BT-123) est "LISIBLE".

BR-FR-18, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-18_BT-123`.

## Related rules

- [BR-FR-17](../BR-FR-17/): the codes allowed to describe an attachment.
