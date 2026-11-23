# A line's invoiced object reference of type AFL or AVV is repeated or empty

An invoice line gives an invoiced object reference of the same type, AFL or AVV, twice, or an empty one.

## What the rule checks

A line can cite "invoiced objects": references to what it is about, such as a subscription number or a metering point. On each line, the two types of references coded AFL and AVV may appear only once each, and must not be empty. BR-FR-29 checks the same for the references of the whole invoice.

## Why it matters

BR-FR-30 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. On each line, keep a single reference of type AFL and a single one of type AVV.
2. Remove the empty references, or fill them in.
3. If your software repeats these references by itself, report it to the software's publisher, quoting BR-FR-30.

## Common causes

- **Two subscription or metering point numbers on one line**, instead of one line per invoiced object.
- **A reference created without a value.**

## Technical details

Line invoiced object identifier BT-128 with its scheme BT-128-1. In UBL, the rule reads `cbc:ID` of each `cac:DocumentReference` of a `cac:InvoiceLine` (or `cac:CreditNoteLine`), by its `schemeID`, `AFL` or `AVV`.

In CII, the rule looks for a `ram:AdditionalReferencedDocument` directly under `ram:IncludedSupplyChainTradeLineItem`, where no CII schema puts it (Factur-X 1.09.2 EN 16931 and EXTENDED, CII D22B), because BT-128 sits under `ram:SpecifiedLineTradeSettlement`. So in the 1.4.0.04 files the rule never fires on a Factur-X or CII invoice.

In the UBL file, the id `BR-FR-30_BT-21` is on another check, BR-FR-31's (a single billing framework note).

## Official text

> Parmi les identifiants d’objets facturés à la ligne (BT-128), les schémas d’identification "AFL" et "AVV" ne doivent être présents qu’une seule fois chacun.

BR-FR-30, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-30_AFL`, `BR-FR-30_AVV`, `BR-FR-30_BT-128`.

## Related rules

- [BR-FR-29](../BR-FR-29/): the same rule for the invoiced object references of the whole invoice.
