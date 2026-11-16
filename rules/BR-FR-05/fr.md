# Une mention obligatoire manque : frais de recouvrement, pénalités de retard ou escompte

La facture électronique ne contient pas l'une des trois mentions de paiement obligatoires sous forme de note codée.

## Ce que vérifie la règle

La facture doit contenir trois notes, chacune repérée par un code :

- **PMT** : l'indemnité forfaitaire pour frais de recouvrement en cas de retard de paiement ;
- **PMD** : les pénalités de retard ;
- **AAB** : les conditions d'escompte pour paiement anticipé, ou leur absence.

Il ne suffit pas que le texte figure quelque part : chaque mention doit être dans une note qui porte son code.

## Pourquoi c'est important

BR-FR-05 fait partie des règles de la réforme française de la facturation électronique, publiées par le FNFE-MPE. Depuis le 1er octobre 2026, une facture qui y échoue n'est pas valide au regard de ces règles.

Ces trois mentions sont obligatoires sur les factures en France ([Code de commerce, article L441-9](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414397) ; [Service-Public](https://entreprendre.service-public.gouv.fr/vosdroits/F31808)). La règle exige qu'elles figurent dans des notes codées, que les logiciels peuvent lire.

## Comment corriger

1. Dans votre logiciel, vérifiez les mentions de paiement de vos factures : taux des pénalités de retard, indemnité forfaitaire de 40 €, escompte (ou « Escompte pour paiement anticipé : néant »).
2. Vérifiez qu'elles sont envoyées comme notes codées PMD, PMT et AAB dans la facture électronique, et pas seulement imprimées sur le PDF.
3. Si votre logiciel ne sait pas coder ces notes, signalez-le à son éditeur en citant BR-FR-05.

## Causes fréquentes

- **Les mentions sont dans le pied de page du PDF**, mais pas dans le fichier XML de la facture.
- **Les trois mentions sont regroupées dans une seule note**, sans code ou avec un seul code.
- **L'absence d'escompte n'est pas indiquée** : la mention AAB est exigée même sans escompte.

## Détails techniques

Les notes forment le groupe BG-1 : code du sujet BT-21, texte BT-22. En CII, un `ram:IncludedNote` dont le `ram:SubjectCode` vaut `PMT`, `PMD` ou `AAB` (codes UNTDID 4451). Les notes UBL n'ont pas de code de sujet : les fichiers officiels cherchent `#PMT#`, `#PMD#` et `#AAB#` dans le texte des notes (`cbc:Note`).

## Texte officiel

> La mention relative aux frais de recouvrement (code PMT) est absente. Elle est obligatoire dans les notes (BG-1).

BR-FR-05, [France_RFE 1.4.0.04](https://github.com/fnfempe/France_RFE/tree/97ba0f3d4ef2abed5780e9490d5c3a2be832ab1d), FNFE-MPE. Les validateurs la signalent sous les identifiants `BR-FR-05_BT-22-1`, `BR-FR-05_BT-22-2`, `BR-FR-05_BT-22-3`, `BR-FR-05_BT-22_AAB`, `BR-FR-05_BT-22_PMD`, `BR-FR-05_BT-22_PMT`.

## Règles voisines

- [BR-FR-06](../BR-FR-06/) : chaque mention codée n'apparaît qu'une fois.
