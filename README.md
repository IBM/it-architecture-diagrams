# it-architecture-diagrams
Implementation and details of [IBM IT architecture diagrams](https://www.ibm.com/design/language/infographics/technical-diagrams/design).

## IBM Diagrams

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
    * IBM Icons (active icons)
    * IBM Shapes (basic shapes)
    * IBM Cloud (cloud shapes)
    * IBM Core (core shapes)
    * IBM Industry (industry shapes)
    * IBM Helpers (helper sets)
    * IBM Starters (starter sets)
</p>
</details>
   
<details><summary>Windows</summary>
</details>

</details>

<details><summary>Colors</summary>
   
<details><summary>IBM Color Palette</summary>
<p>

When any IBM sidebar is first selected the menu bar turns blue indicating that IBM customizations are enabled.
   
The Format Panel under Style is configured with the [IBM Color Palette](https://www.ibm.com/design/language/color/).
   
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
* First row in top group are dark colors for lines.
* Second row in top group are medium colors for lines.
* Third row in top group are light colors for fills.
  
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
   
The Format Panel under Text is configured with the [IBM Plex Fonts](https://www.ibm.com/plex/) and Arial Fonts.

The buttons under Font are configured for Plex:
* No button is Regular font.
* B button is Semi Bold font.
* I button is Italic font.
* B+I buttons are Semi Bold Italic font.

Where a font doesn't have a corresponding Bold or Italic the system Bold or system Italic is applied to the Plex font or Arial font.

The lang parameter is used to select the country code corresponding to the fonts.

The fonts available in IBM Diagrams are currently:

| Font Family | Regular | Semi Bold | Italic | Semi Bold Italic |
| --- | --- | --- | --- | --- |
| IBM Plex Sans | X | X | X | X |
| Arial | X | | | |

Labels in IBM Diagrams have pre-defined Plex fonts:

| Name | Font | Size |
| --- | --- | --- |
| Shape Primary Label | Semi Bold | 14px |
| Shape Secondary Text | Regular | 14px |
| Item Primary Label | Regular | 12px |
| Item Secondary Text | Regular | 12px |
| DU Primary Label | Regular | 14px |
| Badge Label | Regular | 12px`|
| Legend Label | Semi Bold | 14px |
   
</p> 
</details>

<details><summary>Guidelines</summary>
<p>

Recommended guidelines include:
* Always include one legend with each diagram - no legend won't explain the diagram and multiple legends can overpower the diagram.
* Alternate white fill and light fill between consecutive nested groups -  alternate fills helps each group stands out.

</p>
</details>
