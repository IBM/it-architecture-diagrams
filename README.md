# it-architecture-diagrams
Build technical diagrams for IT architecture based on the [IBM Design Language](https://www.ibm.com/design/language/infographics/technical-diagrams/design) and [Carbon Design System](https://carbondesignsystem.com/) featuring the [IBM Color Palette](https://www.ibm.com/design/language/color/) and [IBM Plex Fonts](https://www.ibm.com/plex/).

<details><summary>Guidelines</summary>
<p>

* Use the provided line styles only to temporarily differentiate changes and describe the purpose in a legend:

![Line Styles](/images/line-styles.png "Line Styles")
 
* Alternate white fill and light fill between consecutive nested groups to enable each group to stand out.

![Alternate Fills](/images/alternate-fills.png "Alternate Fills")

* Include a single legend with each diagram to help explain the diagram:

![Single Legend](/images/single-legend.png "Single Legend")

* For connection lines consider using gaps for line jumps, curved elbows, and solid straight triangle arrows:

![Connector Styles](/images/connector-styles.png "Connector Styles")

* Use badges sparingly as needed to not adversely affect the overall diagram.

</p>
</details>

<details><summary>Examples</summary>

<details><summary>IBM WebApp VPC</summary>
<p>

Infrastructure:

![webappvpc-infrastructure](/images/webappvpc-infrastructure.png "IBM WebApp VPC Infrastructure")

Application:

![webappvpc-application](/images/webappvpc-application.png "IBM WebApp VPC Application")

Source:

[IBM WebApp VPC Source](/examples/ibm_vpc_architecture.xml)

</p>
</details>

</details>

<details><summary>Sidebars</summary>
<p>

![IBM Sidebars](/images/sidebar-ibmshape.png "IBM Sidebars")

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
* Third row are dark colors for lines.
  
Followed by a group of 10 rows where:
* First row are Transparent, White, Greys, and Black.
* Second row through tenth row are the entire IBM colors minus swatch 100.

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
   
The Format Panel Text tab is configured with fonts for IBM Plex Sans and Arial:

![Plex Tab](/images/plex-tab.png "Plex Tab")

The buttons are configured according to the following:

| Family | Weight | Use |
| --- | --- | --- |
| IBM Plex Sans | Regular 400 | Other Labels |
| | Regular 400 Italic | I button on Other Labels |
| | SemiBold 600 | Shape Primary Label |
| | SemiBold 600 Italic | I button on Shape Primary Label |
| | Bold 700 | B button |
| | Bold 700 Italic | B+I buttons |

Labels are defined with IBM Plex Sans Regular and IBM Plex Sans SemiBold:

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

Other IBM Global Plex Sans fonts planned to be added.
   
</p> 
</details>

<details><summary>Setup</summary>
<p>
To access and start the latest IBM pre-release diagrams.net application binary for Mac: 
   
1. Download the [zip](https://github.com/IBM/it-architecture-diagrams/releases).
2. Extract and open the application binary. 
3. When you run the first time Mac will ask about security:
    * Go to **System Preferences**.
    * Select **Security & Privacy**.
    * Click on **Open Anyway** for this app.
4. After opening the application binary click on "+ More Shapes" in the bottom left panel.
5. Select IBM and click Apply to finish.
6. IBM Sidebars are now available.
</p>
</details>

<details><summary>Issues</summary>
<p>

1. Dropin size issue - dropping in an image to a shape increases the shape size, for example collapsed shape should remain at 48x48 but dropping in an image changes the size to 48x52 which can then be manually decreased back to 48x48:

![dropin-size-issue](/images/dropin-size-issue.png "Dropin Size Issue")

2. Global fonts issue - de, en, es, fr correctly set fontFamily=IBM Plex Sans but other languanges incorrectly set fontFamily=undefined, eventually all global fonts are planned to be supported.

</p>
</details>
