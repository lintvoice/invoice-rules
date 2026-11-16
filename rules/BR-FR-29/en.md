# An invoiced object reference of type AFL or AVV is repeated or empty

The invoice gives two invoiced object references of the same type AFL or AVV, or one of them is empty.

## What the rule checks

An invoice may cite "invoiced objects": references to what the invoice is based on, such as a subscription number or a meter point. Two types of these references, coded AFL and AVV, may each appear only once, and must not be empty.

## Why it matters

BR-FR-29 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. Find the repeated or empty reference: the validation report says AFL or AVV.
2. Keep one reference of each type, with its value filled in.
3. If your software repeats or empties these references, report it to the software's publisher, quoting BR-FR-29.

## Common causes

- **The same reference sent twice.**
- **A reference type set with no value.**

## Technical details

Invoiced object identifier BT-18 with its scheme BT-18-1: in CII, `ram:AdditionalReferencedDocument` with type code `130` and `ram:ReferenceTypeCode` `AFL` or `AVV`; the value is `ram:IssuerAssignedID`. An empty AFL or AVV reference also fails EN 16931 rule BR-52.

## Official text

> Parmi les identifiants d’objets facturés (BT-18), les schémas d’identification "AFL" et "AVV" ne doivent être présents qu’une seule fois chacun.

BR-FR-29, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-29_AFL`, `BR-FR-29_AVV`, `BR-FR-29_BT-18`.

## Related rules

No closely related rule.
