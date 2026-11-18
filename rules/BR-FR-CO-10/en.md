# A party identifier does not state its type, or a type is repeated

An identifier of a party does not state its type, or the party has two identifiers of the same type.

## What the rule checks

A party (seller, buyer, payee, delivery place…) may have identifiers, each with a scheme code that says what it is: 0009 for a SIRET, 0088 for a GLN, 0224 for a private identifier… The rule checks that:

- every identifier has its scheme code;
- one party does not have two identifiers with the same scheme.

## Why it matters

BR-FR-CO-10 is one of the rules of the French e-invoicing reform, published by FNFE-MPE. Since 1 October 2026, an invoice that fails it is not valid under these rules.

## How to fix it

1. In the party's record, check that every identifier has its type.
2. Delete repeated identifiers: keep one SIRET per party, for example.
3. If your software sends identifiers without their scheme, report it to the software's publisher, quoting BR-FR-CO-10.

## Common causes

- **An identifier entered without its type.**
- **Two SIRETs for one party**, such as an old and a new establishment.

## Technical details

An identifier's type is its `schemeID` attribute. In CII, the rule checks only the global identifiers `ram:GlobalID`: an identifier in `ram:ID`, without a scheme, passes. In UBL, it checks every `cac:PartyIdentification/cbc:ID`, and the delivery place's `cbc:ID`. Parties checked: BT-29 (seller), BT-46 (buyer), BT-60 (payee), BT-71 (delivery place) and the French extension's parties. Ids ending in `-1`: scheme missing; `-2`: scheme repeated.

## Official text

> Si l’identifiant global du vendeur (BT-29) est renseigné, alors son schéma (BT-29-1) doit également être renseigné.

BR-FR-CO-10, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. In French in the official files. Validators report it as `BR-FR-CO-10_BT-29-1`, `BR-FR-CO-10_BT-29-2`, `BR-FR-CO-10_BT-46-1`, `BR-FR-CO-10_BT-46-2`, `BR-FR-CO-10_BT-60-1`, `BR-FR-CO-10_BT-60-2`, `BR-FR-CO-10_BT-71-1`, `BR-FR-CO-10_BT-71-2`, `BR-FR-CO-10_EXT-FR-FE-06-1`, `BR-FR-CO-10_EXT-FR-FE-06-2`, `BR-FR-CO-10_EXT-FR-FE-115-1`, `BR-FR-CO-10_EXT-FR-FE-115-2`, `BR-FR-CO-10_EXT-FR-FE-146-1`, `BR-FR-CO-10_EXT-FR-FE-146-2`, `BR-FR-CO-10_EXT-FR-FE-46-1`, `BR-FR-CO-10_EXT-FR-FE-46-2`, `BR-FR-CO-10_EXT-FR-FE-69-1`, `BR-FR-CO-10_EXT-FR-FE-69-2`, `BR-FR-CO-10_EXT-FR-FE-92-1`, `BR-FR-CO-10_EXT-FR-FE-92-2`.

## Related rules

- [BR-FR-09](../BR-FR-09/): a SIRET starts with its party's SIREN.
- [BR-FR-24](../BR-FR-24/): the characters allowed in a private identifier.
