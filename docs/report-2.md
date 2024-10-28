---
title: "Group 15: Exercise 2 - Information Visualization UE"
subtitle: "Code: [`https://github.com/sueszli/artvis/`](https://github.com/sueszli/artvis/)"
author:
    - "Godun Alina, 01569197"
    - "Lin Tingyu, 12334199"
    - "Jabary Yahya, 11912007"
output: pdf_document
# number_sections: true
# toc: true
toc_depth: 3
documentclass: article
papersize: a4
fontsize: 8pt
geometry:
    - top=10mm
    - bottom=15mm
    - left=10mm
    - right=10mm
header-includes:
    # smaller code
    - \usepackage{fancyvrb}
    - \fvset{fontsize=\scriptsize}
    - \usepackage{listings}
    - \lstset{basicstyle=\scriptsize\ttfamily}
    - \RecustomVerbatimEnvironment{verbatim}{Verbatim}{fontsize=\scriptsize}
---

In this project we visualize the ArtVis dataset[^dataset] derived from the Database of Modern Exhibitions (DoME) from the University of Vienna. This dataset contains information about approximately 14,000 modern painters, their exhibitions and the paintings they exhibited between between the years 1905 and 1915. It is provided in a structured CSV format and accessible in this project's public GitHub page in addition to documentation, code and a reproducible environment.

[^dataset]: Bartosch C., Mulloli N., Burckhardt D., Döhring M., Ahmad W., Rosenberg R.: The database of modern exhibitions (DoME): European paintings and drawings 1905-1915. Routledge, 2020, ch. 30, pp. 423–434.

# Exercise 2

<!--
slides:

The goal with this assignment is not only for you to gain hands-on experience implementing a visualization technique, but also for you to think about the effectiveness of the specific visualization techniques you re-implement in the context of the data domain you work with.
You should use a visualization software toolkit and use the visualization techniques provided by the toolkit. Explore the different examples and demos and adapt them for your purposes. Therefore, it is not necessary to implement a visualization technique from scratch.
-->

## Preprocessing

During the data preprocessing phase, a significant number of records had to be omitted due to formatting issues in the original CSV file. The preprocessing script identified 10,472 invalid lines out of a total of 72,078 records, representing approximately 14.5% of the dataset. The main issue stemmed from unquoted delimiters within text fields, particularly in location entries such as "US, Pittsburgh" which caused incorrect splitting of the data rows. The cleaning process enforced strict data validation rules for various fields and also handled quotation mark standardization and delimiter issues where possible, but complex cases involving embedded commas in unquoted fields could not be automatically resolved. These problematic records, which would have required manual inspection and correction, were excluded from the final cleaned dataset to maintain data integrity. The resulting cleaned dataset contains 61,606 valid exhibition records, providing a reliable foundation for subsequent analysis while acknowledging the trade-off between data completeness and quality.

```
...

invalid in line 72072: expected 19 but got 20
 0: a.id -> 13997
 1: a.firstname -> Louis David
 2: a.lastname -> Vaillant
 3: a.gender -> M
 4: a.birthdate -> 1875-01-01
 5: a.deathdate -> 1944-01-01
 6: a.birthplace -> Cleveland
 7: a.deathplace -> Ohio
 8: a.nationality -> null
 9: e.id -> US
10: e.title -> 296
11: e.venue -> Fourteenth Annual Exhibition
12: e.startdate -> Carnegie Institute
13: e.type -> 1910
14: e.paintings -> group
15: e.country -> 1
16: e.city -> US
17: e.latitude -> Pittsburgh
18: e.longitude -> 40.4333
19: null -> -79.9833


total: 61606, invalid: 10472
```
