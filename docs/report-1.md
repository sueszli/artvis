---
title: "Group 15: Exercise 1 - Information Visualization UE"
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

<!--
slides:

Your task is to design a concept for an interactive visualization and provide explanatory text describing your design.
In a first phase you will characterize the data as well as the user with their tasks and goals.
Based on this you will design a concept for an interactive visualization that you believe effectively communicates the data well according to the users and tasks.
A central element in this context are interaction methods to query, explore and analyze the data visually.
-->

In the first exercise we conceptualize an interactive information visualization for the ArtVis dataset.

# Data and User Characterization

## Data Characterization

The ArtVis dataset contains rich information about modern art exhibitions and artists in early 20th century Europe. The data is structured as a relational table connecting artists to their exhibitions through shared identifiers, with each row representing a unique artist-exhibition pairing.

The dataset is of spatiotemporal and multivariate nature and includes biographical information about artists such as their full names, gender, birth and death dates, birthplace, deathplace and nationality, all stored as a mix of text and standardized date fields.

- `a.id`: Discrete numerical (unique identifier)
- `a.firstname`, `a.lastname`: Nominal (text)
- `a.gender`: Binary categorical (M/F)
- `a.birthdate`, `a.deathdate`: Temporal (YYYY-MM-DD format)
- `a.birthplace`, `a.deathplace`: Nominal (city names)
- `a.nationality`: Nominal (country codes)

Exhibition details are captured through multiple parameters including the exhibition title, venue name, start date, type (group or solo), number of paintings displayed and precise geographic location using both city names and coordinates. The temporal coverage spans from 1905 to 1915, with dates stored in a standardized YYYY-MM-DD format for artist lifespans and YYYY format for exhibition dates. The geographic scope primarily encompasses European cities, with exhibition titles appearing in multiple languages including English, German, Russian and French, reflecting the international nature of the modern art scene. Some venue locations are marked as "exact location unknown," indicating gaps in the historical record.

- `e.id`: Discrete numerical (unique identifier)
- `e.title`: Nominal (text)
- `e.venue`: Nominal (text)
- `e.startdate`: Temporal (YYYY format)
- `e.type`: Nominal categorical (e.g., "group", "solo")
- `e.paintings`: Discrete numerical (count)
- `e.country`: Nominal (country codes)
- `e.city`: Nominal (text)
- `e.latitude`, `e.longitude`: Continuous numerical (geographic coordinates)

An interesting characteristic of the dataset is the presence of duplicate exhibition entries with different venues but the same exhibition ID, suggesting traveling exhibitions or shows that took place simultaneously in multiple locations.

The data structure allows for multiple types of analysis, including (1) **network analysis** through artist co-exhibition relationships, (2) **temporal patterns** in exhibition frequency and (3) **spatial distribution** of modern art activities. The dataset additionally exhibits both hierarchical aspects in the organization of exhibitions and venues and network characteristics in the connections between artists through shared exhibitions.

## User Characterization

The ArtVis dataset primarily serves art historians, museum curators and academic researchers studying early 20th-century modern art movements. These users typically hold advanced degrees in art history, museum studies, or related fields and are familiar with academic research methodologies:

- *Academic Researchers*: These users possess extensive knowledge of art historical methods and are comfortable with complex data visualizations. They regularly publish in peer-reviewed journals and need to support their arguments with empirical evidence. They are familiar with network analysis tools and geographic information systems.
- *Museum Professionals*: Curators and exhibition designers use this data to inform their understanding of historical exhibition practices. They have practical experience in exhibition organization and are particularly interested in understanding historical presentation contexts. They are comfortable with timeline-based visualizations and collection management systems.
- *Digital Humanities Scholars*: These users combine computational methods with traditional humanities research. They are experienced in working with structured data and visualization tools, particularly those focusing on temporal and spatial analysis. They regularly use data visualization software and are familiar with common visualization techniques.

In short, the users are domain experts with a need for a dense and detailed visualization that allows them to explore the dataset in depth and aren't easily cognitively overloaded by complex visualizations.

## Domain Characterization

The application domain is cultural heritage analytics, specifically focusing on exhibition history and artist networks in European modernism between 1905-1915. This period marks a crucial transition in art history, characterized by the emergence of avant-garde movements and changing exhibition practices. Domain specifics include the multilingual nature of exhibition titles (appearing in English, German, Russian and other European languages), the geographic distribution across multiple European cultural centers and the complex network of relationships between artists, venues and exhibition organizers.

A nice touch for our domain could be the use of serif fonts and a color palette inspired by the modernist art movements of the early 20th century, such as the Bauhaus school or the Russian avant-garde. This would help to create a visual connection between the data and the historical context it represents. The visualization could also be designed to accommodate the multilingual nature of the dataset, allowing users to switch between different languages for labels and annotations.

## User Tasks/Goals

The primary tasks and goals of users interacting with the ArtVis dataset include:

- *Historical Network Analysis*:

    Users need to analyze and visualize the connections between artists through shared exhibitions. This includes identifying key figures in artistic movements, understanding collaboration patterns and mapping the spread of artistic influences across Europe. For example, tracking how artists like Kandinsky participated in multiple exhibition groups across different cities.

- *Geographic Movement Patterns*:

    Researchers aim to understand the spatial distribution of modern art exhibitions across Europe. This involves mapping exhibition locations, analyzing artists' travel patterns and identifying major cultural centers. The data shows significant activity in cities like Berlin, Paris and Moscow, with varying degrees of international exchange.

- *Exhibition Practice Evolution*:

    Users seek to understand how exhibition formats and venues changed during this period. This includes analyzing the frequency of group versus solo shows, the emergence of new exhibition spaces and the relationship between traditional and avant-garde venues. The data reveals a predominance of group exhibitions and the importance of certain galleries like Der Sturm in Berlin.

- *Temporal Development Analysis*:

    Researchers need to track changes in exhibition practices over the decade 1905-1915. This includes identifying peak exhibition years, understanding seasonal patterns and analyzing how political events affected exhibition schedules. The data shows varying levels of activity across different years and seasons.

- *Institutional Network Mapping*:

    Users want to understand the relationships between different exhibition venues and organizations. This includes analyzing how certain galleries specialized in particular artistic movements and how institutional networks facilitated the spread of modern art. The data reveals important roles played by venues like the Berliner Secession and various artist-run spaces.

- *Cultural Exchange Documentation*:

    Researchers aim to document and analyze international cultural exchange patterns. This includes tracking how artists exhibited across national boundaries and how different artistic movements spread throughout Europe. The data shows significant cross-border activity, particularly among avant-garde artists.

# Concept Designs

## Concept Design 1: Artist Tracker

![Artist Tracker](docs/assets/concept1.png)

The "Artist Tracker" visualization concept presents an innovative approach to exploring the geographic and temporal patterns.

#### Core Visualization Components

The central element is a geographic time-series visualization combining a map of Europe with temporal tracking of artists' movements. The design emphasizes the spatial relationships between exhibition venues while maintaining temporal context through animated paths and a timeline interface.

The main map employs a light, minimalist base design that clearly shows country boundaries and major cities without overwhelming the movement data. Artist trajectories are represented as colored paths connecting exhibition locations chronologically, with each artist assigned a distinct color to maintain visual distinction.

#### Visual Encodings and Mappings

The temporal dimension is encoded through multiple complementary methods. The primary encoding appears in the path animations showing artists' movements across Europe, while a secondary encoding exists in the timeline bar chart at the bottom showing exhibition frequency over time. This dual representation allows users to understand both the spatial and temporal patterns simultaneously.

Exhibition locations are encoded as points on the map, with their size potentially varying based on the number of exhibitions held at each venue. The color-coding system assigns unique colors to each selected artist, maintaining consistency across all visualization components including the paths, timeline highlights and the selection interface.

#### Interactive Features and User Support

The interface supports several key interaction methods: (1) The artist selection panel allows users to choose which artists to track, with a scrollable list showing all available artists. Selected artists are indicated with colored checkboxes matching their trajectory colors. (2) A timeline slider at the bottom serves dual purposes - it shows the total exhibition activity through bar heights while allowing users to filter the time period of interest. Users can drag the slider to focus on specific years or months. (3) The "Most exhibited" section provides a dynamic bar chart showing the relative exhibition frequencies in major cities, updating based on the selected artists and time period. This helps users identify important cultural centers for different artists or movements.

#### Design Specifics and Rationale

The visualization prioritizes clarity in showing movement patterns while maintaining access to detailed information. The paths use curved lines rather than straight connections to better represent travel routes and reduce visual clutter when multiple paths cross.

The timeline component uses a consistent height scale to show exhibition frequency, with subtle gridlines helping users align temporal patterns. The bars are segmented by artist colors when multiple selected artists exhibited in the same period.

The city comparison bars use a horizontal layout to accommodate city names clearly while showing relative exhibition frequencies through length. The bars maintain the artist color-coding scheme to show which artists exhibited most frequently in each location.

#### Potential Improvements

Several enhancements could strengthen the visualization:

- Adding filters for exhibition types (solo vs. group shows) could reveal different patterns in artists' career trajectories.
- Implementing a brushing and linking feature between the map and timeline would allow users to select specific time periods or locations and see related information highlighted across all components.
- Including additional metadata about exhibitions (such as number of works shown or exhibition duration) could be encoded through variations in path thickness or point size. This could also be provided on hover in addition to color encoding to avoid visual clutter.
- The interface could benefit from a search function in the artist selection panel to help users quickly find specific artists of interest.
- Adding the ability to compare different time periods side by side could help users identify changes in exhibition patterns over time.

This design successfully balances the complexity of the underlying data with accessibility and usability, though there remains room for additional features that could provide even deeper insights into the patterns of early modern art exhibitions.

## Concept Design 2: Artist-Exhibition Network

![Artist-Exhibition Network](docs/assets/concept2.png)

The "Artist-Exhibition Knowledge Graph / Ontology" concept sketch presents a visualization system designed to explore and analyze the complex network of artists and exhibitions.

#### Core Visualization Components

The visualization integrates three main components working in concert: a geographic map of Europe, a network graph visualization and a temporal timeline. This combination allows users to explore the spatial, relational and temporal aspects of the exhibition data simultaneously.

The geographic map serves as the primary spatial reference, displaying exhibition locations across Europe. The map employs a minimalist design with subtle country boundaries and focuses on the relevant geographic region. This design choice helps users maintain spatial context while minimizing visual clutter.

The network visualization represents the relationships between artists and exhibition groups. The visualization uses a force-directed layout where nodes represent either artists or exhibition groups and edges represent participation relationships. The decision to use different edge styles (solid lines for exhibition relationships and dashed lines for frequent collaborations) helps users distinguish between different types of artistic connections.

The timeline component at the bottom provides temporal context and filtering capabilities. It displays exhibition frequency through bar heights, with a draggable selection window that allows users to focus on specific time periods. This design enables users to observe temporal patterns while maintaining the broader historical context.

#### Visual Encodings and Mappings

The system employs several careful visual encoding decisions: The network visualization uses circles for nodes, with consistent sizing to maintain visual clarity. The choice to keep node sizes uniform rather than mapping them to variables like exhibition count helps maintain readability in the force-directed layout.

Edge thickness in the network could represent the number of shared exhibitions, though this isn't explicitly shown in the mockup. The distinction between solid and dashed lines for different relationship types provides clear categorical separation without requiring color differentiation.

The hover functionality reveals detailed information about artists, including birth dates, death dates and age information. This information is displayed in a dark overlay card with white text, ensuring good contrast and readability while maintaining visual hierarchy.

#### Interaction Design

The system implements multiple levels of user interaction:

- *Geographic Navigation*: Users can hover and click on locations in the map to focus on specific cities or regions. This interaction likely filters or highlights relevant connections in the network visualization.
- *Temporal Selection*: The timeline includes a draggable selection window that allows users to focus on specific time periods. This selection presumably updates both the map and network visualizations to show only exhibitions within the selected timeframe.
- *Network Exploration*: Users can interact with the network visualization through hover interactions that reveal detailed information about artists and their relationships. The current selection shows details about an artist named "Male" with specific birth and death dates.
- *Coordinated Views*: All three visualization components are linked, meaning interactions in one component affect the others. For example, selecting a time period in the timeline likely updates both the map and network displays.

#### Design Specifics and Rationale

The layout places the map and network visualization side by side, with the timeline spanning the full width below. This arrangement allows users to easily compare geographic and network patterns while maintaining temporal context.

The choice of a light background with dark features ensures good contrast and readability. The minimal use of color helps avoid visual overload, allowing the structure of the relationships to take precedence.

The current selection indicator in the title ("Current Selected Graph: Vienna, 1908-1910") provides clear context about the visualization's current state. This helps users maintain awareness of their current focus within the broader dataset.

#### Potential Improvements

Several enhancements could further strengthen the visualization:

- The system could incorporate additional filtering capabilities based on artist nationality, exhibition type, or artistic movement. This would help users explore specific aspects of the artistic network.
- The network visualization could benefit from community detection algorithms to highlight clusters of closely connected artists and exhibition groups.
- The map component could use sized markers to indicate the number of exhibitions in each location, providing immediate visual feedback about important artistic centers.
- The timeline could incorporate additional visual encodings, such as color-coding for different types of exhibitions or overlays showing political events that might have influenced artistic activities.

These improvements would enhance the system's analytical capabilities while maintaining its current clarity and usability.

While the proposed visualization concepts differ in their focus and design, both aim to provide users with a powerful tool for exploring the rich ArtVis dataset. By combining spatial, relational and temporal perspectives, the visualizations offer a comprehensive view of early 20th-century European art history. The designs prioritize clarity, interactivity and user control, ensuring that domain experts can extract valuable insights from the data while maintaining a high level of engagement.
