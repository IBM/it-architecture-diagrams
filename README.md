# it-architecture-diagrams
Build technical diagrams for IT architecture based on the [IBM Design Language](https://www.ibm.com/design/language/infographics/technical-diagrams/design) and [Carbon Design System](https://carbondesignsystem.com/), and also featuring the [IBM Color Palette](https://www.ibm.com/design/language/color/) and [IBM Plex Fonts](https://www.ibm.com/plex/).

## IBM Diagrams

<details><summary>Guidelines</summary>
<p>

Recommended guidelines include:
* Always include one legend with each diagram - no legend won't explain the diagram and multiple legends can overpower the diagram.
* Alternate white fill and light fill between consecutive nested groups -  alternating fills enables each group to stand out visually.

</p>
</details>

<details><summary>Setup</summary>
   
<details><summary>Mac</summary>
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
6. IBM Sidebars are now available:
    * Base:
        * IBM Icons *(Generic list of all icons)*
        * IBM Shapes *(Generic list of all shapes)*
    * Cloud:
        * IBM Cloud *(Customized icons & groups)*
        * IBM Core *(Customized icons & groups)*
        * IBM Industry *(Customized icons & groups)*
    * Sets:
        * IBM Helpers *(Preconfigured collections)*
        * IBM Starters *(Preconfigured arrangements)*
</p>
</details>

</details>

<details><summary>Colors</summary>
   
<details><summary>IBM Color Palette</summary>
<p>

When any IBM sidebar is first selected the menu bar turns blue indicating that IBM customizations are enabled.
   
The Format Panel under Style is configured with the IBM Color Palette.
   
Three colors in each color family are available for use with IBM Diagrams:
* Light Fill (swatch 10)
* Medium Line (swatch 50 or 60)
* Dark Line (swatch 70 or 80)
   
Additionally,
* White
* Black
* Transparent

Defaults,
* Collapsed shapes and expanded target system shape default to no fill, which can be changed to white fill or light fill.
* Remaining expanded shapes default to white fill for container shapes and no fill for non-container shapes, which can be changed to white fill or light fill.`.
   
</p>
</details>

<details><summary>IBM Color Schemes</summary>
<p>
   
The IBM Color Schemes at the top of the Format Panel under Style are the recommended method of using the IBM Color Palette:
![IBM Color Schemes](/images/IBMColorSchemes.png "IBM Color Schemes")

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
![IBM Preset Colors](/images/IBMPresetColors.png "IBM Preset Colors")

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
   
The Format Panel under Text is configured with the IBM Plex Sans fonts on Google Fonts and Arial fonts:

| Family | Weight | Use |
| --- | --- | --- |
| IBM Plex Sans | Regular 400 | Other Labels |
| | Regular 400 Italic | I button |
| | SemiBold 600 | Primary Label |
| | SemiBold 600 Italic | Not Used |
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
   
</p> 
</details>

</p>
</details>
