# it-architecture-diagrams
Implementation and examples of IBM IT architecture diagrams.

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

<details><summary>Introduction</summary>
   
<details><summary>IBM Color Palette</summary>
<p>
   
The Format Panel for IBM Diagrams is configured with the [IBM Color Palette](https://www.ibm.com/design/language/color/).
   
Three colors in each color family are available for use with IBM Diagrams:
* Light Fill (swatch 10)
* Medium Line (swatch 50 or 60)
* Dark Line (swatch 70 or 80)
   
The following colors are also available for use with IBM Diagrams:
* White
* Black
* Transparent
   
</p>
</details>

<details><summary>IBM Color Schemes</summary>
<p>
   
The IBM Color Schemes at the top of the Format Panel are the recommended method of using the IBM Color Palette:
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

The IBM Preset Colors are the secondary method of using the IBM Color Palette with the group of three rows at the top of the IBM Colors:
![IBM Preset Colors](/images/IBMPresetColors.png "IBM Preset Colors")

Where,
* First row are dark colors for lines.
* Second row are medium colors for lines.
* Third row are light colors for fills.
  
Additionally,
* First row in bottom group of 10 rows has Transparent, White, and Black.
* Second row through last row in bottom group of 10 rows are the entire IBM Color Palette minus swatch 100.

Tooltips,
* Each color in the IBM Colors has a tooltip that shows the color family, color swatch, and intended use.

</p>
</details>

<details><summary>IBM Plex Fonts</summary>
<p>
   
The Format Panel for IBM Diagrams is configured with the [IBM Plex Fonts](https://www.ibm.com/plex/) and Arial Fonts.

The buttons in the Format Panel are configured as follows for Plex fonts:
* No button is Regular font.
* B button is Semi Bold font.
* I button is Italic font.
* B+I buttons are Semi Bold Italic font.

Where a font doesn't have a corresponding Bold or Italic the system Bold or Italic is applied to the Plex font or Arial font.

The lang parameter is used to select the country code corresponding to the fonts.

The fonts available in IBM Diagrams are:

| Font Name | Regular | Semi Bold | Italic | Semi Bold Italic |
| --- | --- | --- | --- | --- |
| IBM Plex Sans | X | X | X | X |
| IBM Plex Sans Arabic | X | X | | |
| Arial | X | | | |

Labels in IBM Diagrams have pre-defined Plex fonts as follows:

| Name | Font | Size |
| --- | --- | --- |
| Primary Label | Semi Bold | 10pt |
| Secondary Text | Regular | 10pt |
| Badge Label | Regular | 8pt`|
| Legend Label | Semi Bold | 8pt |
| Item Label | Regular | 8pt |
| DU Label | Regular | 8pt |
   
</p> 
</details>
