---
title: "Group 15: Information Visualization UE 2024W"
subtitle: "Code: [`https://github.com/sueszli/artvis/`](https://github.com/sueszli/artvis/)"
author:
    - "Godun Alina, 01569197"
    - "Lin Tingyu, 12334199"
    - "Jabary Yahya, 11912007"
output: pdf_document
number_sections: true
toc: true
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

\newpage

In this project we visualize the ArtVis dataset[^dataset]. This dataset contains information about approximately 14,000 modern painters and their exhibitions between the years 1905 and 1915. The dataset is derived from the Database of Modern Exhibitions (DoME) from the University of Vienna and provided in the project's public GitHub repository.

[^dataset]: Bartosch C., Mulloli N., Burckhardt D., Döhring M., Ahmad W., Rosenberg R.: The database of modern exhibitions (DoME): European paintings and drawings 1905-1915. Routledge, 2020, ch. 30, pp. 423–434.

<!--
dataset:

- spatiotemporal and multivariate

- Artist properties start with an "a.", exhibition properties with an "e."
- The gener of an artist (a.gender) can be either "M" or "F" 
- There might be uncertainty in the birth- and death dates (a.birthdate, a.deathdate) of the artists, i.e. missing months or days (e.g., "1866-01-01"). It is fine, if you only use the years and leave days and months out.
- The exhibition type (e.type) might be group, solo, or auction. In group exhibitions and auctions multiple artists were featured, while in solo exhibitions only one artist exhibited their paintings.
e.paintings denotes the number of paintings an artist exhibited in a certain exhibition
- Be careful about the format of the exhibitions' latitude and longitude columns (e.latitude, e.longitude) when importing the csv into other programs! Check if they are still correct, otherwise you might get incorrect positions on a map.


when you can't fit all information into a single visualization:

- Select a time interval instead of the full range
- Aggregate by calendar interval, e.g., by year
- Select a smaller region in space instead of the whole extent, e.g., exhibitions in certain countries
- Aggregate by spatial hierarchy, e.g., cities, countries, or continents
- Select a subset of the data, e.g., artists with certain nationalities, male/female artists, certain film types
- Aggregate by such data subsets, e.g., exhibition locations over time for female/male artists

what to include: 

- the temporal component needs to be considered in any case
- you can simplify and aggregate spatial dimension
- you can look at single or groups of data cases (artists, exhibitions, films)
-->

# Exercise 1

<!--
slides:

Your task is to design a concept for an interactive visualization and provide explanatory text describing your design.
In a first phase you will characterize the data as well as the user with their tasks and goals.
Based on this you will design a concept for an interactive visualization that you believe effectively communicates the data well according to the users and tasks.
A central element in this context are interaction methods to query, explore, and analyze the data visually.
-->






# Exercise 2

<!--
slides:

The goal with this assignment is not only for you to gain hands-on experience implementing a visualization technique, but also for you to think about the effectiveness of the specific visualization techniques you re-implement in the context of the data domain you work with.
You should use a visualization software toolkit and use the visualization techniques provided by the toolkit. Explore the different examples and demos and adapt them for your purposes. Therefore, it is not necessary to implement a visualization technique from scratch.
-->
