# it-architecture-diagrams
IBM IT architecture diagrams are available with IBM v2 in diagrams.net desktop currently in [Mac beta (internal use only)](https://github.ibm.com/acs-sa/it-architecture-diagrams/releases/tag/v30.2.45-ibm2beta2), which is subject to change until a final version from draw.io is available in [drawio-desktop](https://github.com/jgraph/drawio-desktop).  

After unzipping, the Mac beta can be installed as a normal Mac app or can be run directly.  
When running for the first time:
* For the error message that the developer cannot be verified, go to System Preferences -> Security and select the Open File Anyway.
* For the JavaScript message that BrowserWindow cannot be created before app is ready, go to Privacy & Security -> Developer Tools and select the ibm2beta2 app.

The IBM Design language includes details on the IBM v2 diagrams in [Technical Diagrams Design](https://www.ibm.com/design/language/infographics/technical-diagrams/design/) and [Technical Diagrams Usage](https://www.ibm.com/design/language/infographics/technical-diagrams/usage/).

Diagram-as-Code is available for IBM v2 diagrams with [drawIT](https://github.com/IBM/drawit) which helps users focus on the content rather than the actual layout, especially as future changes are made to diagrams.

<details><summary>Base</summary>
<p>

IBM IT architecture diagrams are based on the following:
* [IBM Design Language](https://www.ibm.com/design/language/infographics/technical-diagrams/design)
* [IBM Color Palette](https://www.ibm.com/design/language/color/)
* [IBM Plex Fonts](https://www.ibm.com/plex/)
* [Carbon Design System](https://carbondesignsystem.com/)

</p>
</details>

<details><summary>Colors</summary>
   
When an IBM Sidebar is first selected the top bar turns blue indicating use of the IBM colors, fonts, shapes, and properties:

![Top Bar](/images/top-bar.png "Top Bar")

The Format Panel Style tab includes the IBM colors which can be set with the color schemes or individual colors:

![style-tab](/images/style-tab.png "Style Tab")

The recommended method of setting colors is with the color schemes at the top of the Style tab which includes all 
combinations of line colors (medium colors on top row and dark colors on bottom row) and fill colors (white or light color of same color family 
as the line color).

The secondary method of setting colors is with the individual line and fill colors under the color schemes which
brings up the entire color palette:

![Color Palette](/images/color-palette.png "Color Palette")

The top row are the recently selected colors.

Followed by a group of 3 rows where:
* First row are light colors for fills.
* Second row are medium colors for lines.
* Third row are dark colrs for lines.
  
Followed by a group of 10 rows where:
* First row are Transparent, White, Greys, and Black.
* Second row through tenth row are the entire set of IBM colors minus swatch 100.

Notes:
* Each IBM color has a tooltip that shows the color family, color swatch, and intended use.
* For IBM Icons,
  * Collapsed shapes and expanded target system default to solid color but changable to white or light fill.
  * Other expanded shapes default to solid color behind the icon and white fill for the rest of the shape.
* For dropin images, 
  * Collapsed shapes and expanded target system default to white fill but changable to solid or light fill.
  * Other expanded shapes default to white fill behind the icon and the rest of the shape but can be changed to light fill.
   
</details>

<details><summary>Fonts</summary>
<p>
   
The Format Panel Text tab is configured with fonts from Google Fonts for all of the current IBM Plex Sans:
* IBM Plex Sans
* IBM Plex Sans Arabic
* IBM Plex Sans Devanagar
* IBM Plex Sans Hebrew
* IBM Plex Sans JP
* IBM Plex Sans KR
* IBM Plex Sans Thai

![Plex Tab](/images/plex-tab.png "Plex Tab")

Buttons in the Text tab are configured for IBM Plex Sans as follows:

| Button | Weight |
| --- | --- |
| No Button | Regular 400 |
| I Button | Regular 400 Italic |
| B Button | Bold 700 |
| B+I Button | Bold 700 Italic |

Shape labels are configured for IBM Plex Sans as follows:

| Label | Weight | Size |
| --- | --- | --- |
| Shape Primary Label | SemiBold 600 | 14 |
| Shape Secondary Text | Regular 400 | 14 |
| Item Primary Label | Regular 400 | 12 |
| Item Secondary Text | Regular 400 | 12 |
| DU Primary Label | Regular 400 | 14 |
| Badge Label | Regular 400 | 12`|
| Legend Label | SemiBold 600 | 14 |

The lang parameter enables the country code corresponding to the fonts.
   
</p> 
</details>

<details><summary>Guidelines</summary>
<p>

* Use the provided line styles only to temporarily differentiate changes and describe the purpose in a legend:

![Line Styles](/images/line-styles.png "Line Styles")
 
* Alternate white fill and light fill between consecutive nested groups to enable each group to stand out.

![Alternate Fills](/images/alternate-fills.png "Alternate Fills")

* Include a single legend with each diagram to help explain the diagram:

![Single Legend](/images/single-legend.png "Single Legend")

* For connection lines consider use gaps for line jumps, curved elbows, and solid straight triangle arrows:

![Connector Styles](/images/connector-styles.png "Connector Styles")

* Use badges sparingly as needed to not adversely affect the overall diagram.

</p>
</details>

<details><summary>Examples</summary>
<p>

[webappvpc-infrastructure](/images/webappvpc-infrastructure.png "IBM WebApp VPC Infrastructure")

[webappvpc-application](/images/webappvpc-application.png "IBM WebApp VPC Application")

</p>
</details>

<!--
## References

- [IBM Design Language](https://www.ibm.com/design/language/infographics/technical-diagrams/design)
- [IBM Color Palette](https://www.ibm.com/design/language/color/)
- [IBM Plex Fonts](https://www.ibm.com/plex/)
- [Carbon Design System](https://carbondesignsystem.com/)
-->

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
