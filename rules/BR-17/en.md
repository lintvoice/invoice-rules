# The payee has no name, or is the seller itself

The invoice names a payee that has no name, or that is the seller itself.

## What the rule checks

An invoice can say that the payment goes to someone other than the seller, a factoring company for example: the payee. When it does, the rule checks that the payee has a name, and that the payee differs from the seller: not the seller's name, nor its identifier, nor its legal registration number.

## Why it matters

BR-17 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-17 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. If the seller is paid itself, leave the payee out of the invoice.
2. If someone else is paid, give that payee's name and its own identifiers.
3. If your software fills in the payee with the seller's details, report it to the software's publisher, quoting BR-17.

## Common causes

- **The seller's details copied into the payee** by software that always fills it in.
- **A payee given by its identifier only**, without its name.

## Technical details

The payee is group BG-10, its name BT-59. In CII, the rule reads `ram:Name`, `ram:ID` and `ram:SpecifiedLegalOrganization/ram:ID` of `ram:PayeeTradeParty`, in `ram:ApplicableHeaderTradeSettlement`, and compares them with the seller's; in UBL, `cac:PayeeParty`.

The example invoice names the seller again as payee, with its own name, so it fails BR-17 alone.

## Official text

> The Payee name (BT-59) shall be provided in the Invoice, if the Payee (BG-10) is different from the Seller (BG-4).

BR-17, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-FR-CO-10](../BR-FR-CO-10/): each identifier of a party must state its type (SIRET, GLN…), and a party cannot have two identifiers of the same type.
- [BR-06](../BR-06/): every invoice must give the seller's name.
