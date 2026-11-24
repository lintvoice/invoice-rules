# An invoice outside the scope of VAT has another VAT breakdown

The invoice has a VAT breakdown outside the scope of VAT, and a VAT breakdown in another category.

## What the rule checks

Category O covers operations no VAT applies to, such as a service supplied to a business outside the EU. An invoice is outside the scope of VAT as a whole, or not at all. A supply that carries VAT, or is exempt from it, goes on another invoice. The rule checks that an invoice with a VAT breakdown in O does not have a VAT breakdown in another category.

## Why it matters

BR-O-11 is a rule of the European e-invoicing standard, EN 16931. The French, German (XRechnung) and European (Peppol) rules build on this standard, so an invoice that fails BR-O-11 also fails each of them.

In public procurement, buyers in the European Union must accept e-invoices that follow this standard ([Directive 2014/55/EU](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## How to fix it

1. Put the operations outside the scope of VAT on an invoice of their own, and the others on another.
2. Check the category of each line, allowance and charge: one outside the scope of VAT is in O, with no rate.
3. If your software adds another category on its own, report it to the software's publisher, quoting BR-O-11.

## Common causes

- **A template that always writes a standard-rate breakdown**, even empty.
- **A shipping charge or a discount left at the standard rate** by default.

## Technical details

The VAT category code of a breakdown is BT-118; those of a line, an allowance and a charge are BT-151, BT-95 and BT-102. In CII, BR-O-11 and BR-O-12 run one test, which refuses any VAT category other than O on a breakdown or a line, so they fail together; BR-O-13 and BR-O-14 run another, on any allowance or charge. UBL tells the four apart.

The example invoice is all outside the scope of VAT, and also has an empty VAT breakdown at the standard rate, as a template that always writes it would. BR-O-12 fails too: in CII, its test is the same.

## Official text

> An Invoice that contains a VAT breakdown group (BG-23) with a VAT category code (BT-118) "Not subject to VAT" shall not contain other VAT breakdown groups (BG-23).

BR-O-11, [EN 16931 validation artefacts 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII and UBL.

## Related rules

- [BR-O-12](../BR-O-12/): an invoice outside the scope of VAT (O) cannot also have a line in another VAT category.
- [BR-O-13](../BR-O-13/): an invoice outside the scope of VAT (O) cannot also have a document level allowance in another VAT category.
- [BR-O-01](../BR-O-01/): an invoice with a line, an allowance or a charge in the VAT category O (outside the scope of VAT) must have exactly one VAT breakdown for it.
