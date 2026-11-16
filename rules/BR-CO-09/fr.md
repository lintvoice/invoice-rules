# Un numéro de TVA ne commence pas par un code pays

Un numéro de TVA de la facture ne commence pas par le code du pays qui l'a attribué.

## Ce que vérifie la règle

La règle regarde les numéros de TVA intracommunautaire de la facture : celui du vendeur, celui de son représentant fiscal s'il en a un, et celui de l'acheteur. Chacun doit commencer par les deux lettres du pays qui l'a attribué, par exemple FR pour la France ou DE pour l'Allemagne.

## Pourquoi c'est important

BR-CO-09 est une règle de la norme européenne de facturation électronique, EN 16931. Les règles françaises, allemandes (XRechnung) et européennes (Peppol) reprennent cette norme, donc une facture qui échoue à BR-CO-09 échoue aussi à chacune d'elles.

Dans les marchés publics, les acheteurs de l'Union européenne doivent accepter les factures électroniques qui suivent cette norme ([directive 2014/55/UE](https://eur-lex.europa.eu/eli/dir/2014/55/oj)).

## Comment corriger

1. Vérifiez le numéro de TVA dans la fiche de votre entreprise et dans celle de votre client : il commence par les deux lettres du pays, puis le numéro.
2. Ne mettez ni espace ni autre caractère avant ces deux lettres.
3. N'indiquez pas un SIREN ou un SIRET à la place du numéro de TVA.
4. Si le numéro est juste dans votre logiciel mais pas dans la facture électronique, signalez-le à son éditeur en citant BR-CO-09.

## Causes fréquentes

- **Le numéro saisi sans son préfixe pays**, seulement les chiffres.
- **Un SIREN ou un SIRET mis à la place du numéro de TVA.**
- **Un espace ou un autre caractère avant le numéro**, car la règle lit ses deux premiers caractères.
- **Un numéro grec écrit avec EL** (voir les détails techniques).

## Détails techniques

Les numéros vérifiés sont ceux du vendeur (BT-31), de son représentant fiscal (BT-63) et de l'acheteur (BT-48). La règle compare leurs deux premiers caractères à une liste de codes pays ISO 3166-1 alpha-2, complétée par 1A et XI. En CII, elle lit chaque `ram:SpecifiedTaxRegistration/ram:ID` dont `schemeID` vaut `VA` ; en UBL, `cac:PartyTaxScheme/cbc:CompanyID` quand le schéma fiscal est `VAT`.

Le message officiel autorise le préfixe EL pour la Grèce, mais la liste des fichiers 1.3.17 ne le contient pas : un numéro qui commence par EL y échoue à BR-CO-09, et GR passe. Nous l'avons vérifié sur la facture d'exemple valide, numéro du vendeur remplacé par EL123456789.

## Texte officiel

> The Seller VAT identifier (BT-31), the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48) shall have a prefix in accordance with ISO code ISO 3166-1 alpha-2 by which the country of issue may be identified. Nevertheless, Greece may use the prefix ‘EL’.

BR-CO-09, [artefacts de validation EN 16931 1.3.17](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17), CII et UBL. Le message officiel est en anglais.

## Règles voisines

- [BR-CO-26](../BR-CO-26/) : le vendeur doit avoir au moins un identifiant : identifiant, numéro d'immatriculation ou numéro de TVA.
