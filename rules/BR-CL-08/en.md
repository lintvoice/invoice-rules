# A note's subject is not a valid code

The code that gives a note's subject is not in the official list.

## What the rule checks

An invoice can carry notes, and each note can give its subject with a code: AAI for general information, PMT for payment information, AAB for payment terms… Some countries use them for required notes: in France, PMT, PMD and AAB carry the notes the law requires on late payment. The rule checks that a note's code comes from the official list, not a word such as "INFO".

## Why it matters

BR-CL-08 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-CL-08 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Choose each note's subject in your software from its list, or leave it out.
2. Check that the e-invoice writes a code from the list, such as AAI.
3. If your software writes another value, report it to the software's publisher, quoting BR-CL-08.

## Common causes

- **A word instead of the code**, such as INFO or NOTE.
- **A code in lower case**, while the list's codes are in capitals.

## Technical details

The invoice note subject code is BT-21. In CII, it is `ram:SubjectCode` of each `ram:IncludedNote` in `rsm:ExchangedDocument`. In UBL, a note has no element for it: the rule reads a code written between the first two `#` of `cbc:Note`, as in `#AAI#Thank you`, and lets a note without that pattern pass. The list is part of UNTDID 4451.

The example invoice adds a note with the subject code `INFO`; its fixed counterpart gives `AAI`. The Factur-X EN 16931 profile checks the same list with its own rule `FX-SCH-A-000553`, which fails next to it in a Factur-X invoice.

## Official text

> Subject Code MUST be coded using a restriction of UNTDID 4451.

BR-CL-08, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-FR-05](../BR-FR-05/): the invoice must carry three statements, each in a coded note: the fixed indemnity for recovery costs (PMT), late-payment penalties (PMD) and the early-payment discount or its absence (AAB).
