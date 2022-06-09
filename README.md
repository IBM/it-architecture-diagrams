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

* Use badges sparingly as needed to not adversely affect the viewability of the overall diagram.

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
   
<details><summary>IBM Color Palette</summary>
<p>

Three colors in each color family are available for use with IBM Diagrams:
* Light Fill (swatch 10)
* Medium Line (swatch 50 or 60)
* Dark Line (swatch 70 or 80)
   
Additionally,
* White
* Black
* Transparent

For IBM Icons: 

| Shape | Icon Area | Body Fill | Container |
| --- | --- | --- | --- |
| Collapsed and Expanded Target System | Solid changable to white or light | N/A | No |
| Expanded Component and Node | Solid  | White changable to light | Yes |
| Location and Subsystem | Same as Body Fill | White changable to light | Yes |
| Zone | No fill |  No fill | No |

For dropin images:

| Shape | Icon Area | Body Fill | Container |
| --- | --- | --- | --- |
| Collapsed and Expanded Target System | White changable to light or solid | N/A | No |
| Expanded Component and Node | Same as Body Fill  | White changable to light | Yes |
| Location and Subsystem | Same as Body Fill | White changable to light | Yes |
| Zone | No fill |  No fill | No |
   
</p>
</details>

<details><summary>IBM Color Schemes</summary>
<p>
   
The IBM Color Schemes at the top of the Format Panel under Style are the recommended method of using the IBM Color Palette:

![IBM Color Schemes](/images/color-schemes.png "IBM Color Schemes")

Where,
* Top row are medium color lines with white fill followed by light fill.
* Bottom row are dark color lines with white fill followed by light fill.
   
Example,
| Column 1 | Column 2 | Column 3 | Column 4 |
| --- | --- | --- | --- |
| Medium Red<br>White Fill | Medium Red<br>Light Fill | Medium Magenta<br>White Fill | Medium Magenta<br>Light Fill |
| Dark Red<br>White Fill | Dark Red<br>Light Fill | Dark Magenta<br>White Fill | Dark Magenta<br>Light Fill |

</p>
</details>

<details><summary>IBM Preset Colors</summary>
<p>

The IBM Preset Colors are the secondary method of using the IBM Color Palette with the top group of 3 rows:

![IBM Preset Colors](/images/preset-colors.png "IBM Preset Colors")

Where,
* First row in top group are light colors for fills.
* Second row in top group are medium colors for lines.
* Third row in top group are dark colors for lines.
  
Additionally,
* First row in bottom group has Transparent, White, and Black.
* Second row through tenth row in bottom group are the entire IBM Color Palette minus swatch 100.

Tooltips,
* Each color in the IBM Colors has a tooltip that shows the color family, color swatch, and intended use.

</p>
</details>

</details>

<details><summary>Fonts</summary>
<p>
   
The Format Panel under Text is configured with fonts for IBM Plex Sans and Arial:

| Family | Weight | Use |
| --- | --- | --- |
| IBM Plex Sans | Regular 400 | Other Labels |
| | Regular 400 Italic | I button on Other Labels |
| | SemiBold 600 | Shape Primary Label |
| | SemiBold 600 Italic | I button on Shape Primary Label |
| | Bold 700 | B button |
| | Bold 700 Italic | B+I buttons |

Labels in IBM Diagrams are pre-defined with IBM Plex Sans Regular and IBM Plex Sans SemiBold:
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
