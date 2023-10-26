# Flat icon pack expansion campaign

This file describes the (definition ongoing) workflow to develop additional icons for the Flat icons package.

## Multiple pages on inkscape

Working on all the icons for a given workbench on a single file is very handy because often we reuse elements from one commad to another. Here's how I am making it work:

There is a 'page' tool on the left toolbar. Select it and then it's possible to add pages from the toolbar under the general menu.
The pages can be named and the name should be consistent with the expected file name.
_I am using the information from the tooltip at the moment, I guesss there is a more elegant option to get a list?_

By default, the pages are added in a row with very little spacing. When the page tool is active it's possible to move them around. All the elements outside the page boxes are not exported, so it's possible to keep working versions nearby.

### Icon preview

Unfortunately (at least on InkScape 1.2) the Icon preview function shows the first page that was created in the document. It could be overcome by naming it 'preview'
and then moving into it the icon that we are working on / wish to see at different scales.

### Export all the icons to single files

- Select file / export from the Inkscape Menu.
- Select 'batch export' and then 'pages' on top of the toolbox.
- leave suffix blank, select 'plain svg' as file format.
- Click on the folder in the export path, choose the desired output directory and filename\*
- \*The exported files are named <filenamename>\_pageName.svg. I tried leaving it blank with no success. I need to investigate further, or create a bash script to remove this prefix.

## General Inkscape tricks

### handling line thickness

The style guide imposes 1.5px on the internal detail and 3px for the outline. I gound out that there's a quick hack to make them lineout with minimal effort:

- go to inkscape preferences and search 'outset'
- set 'Inset / Outset By:' to 0.75px
- draw all with 1.5px outline
- copy, paste ahd then merge all the shapes that contribute to the icon outline. Set the resulting shape with no fill, 3px outline and snap it on top of the design.
- Scale you icon to size inside the box
- select the general outline and then Path / outset, it should line up beautifully.

### handling dotted lines

There is a numeric field close to the dash parameters. Increasing it shifts the dots along the path, this is useful, for example, if there is a corner on a dotted line and we want to put one of the dots exactly on the corner.

## CSS

Inkscape has the ability to move the style from the object to an embedded stylesheet in the <svg:defs> part of the file. Is is tricky to master in the beginning but once learned is gold. This could be also harvested fo runtime styling of the icons, but it needs to be tested. Let's see if icon files generated this way are rendered properly before migrating everything to CSS.

The Mesh source file now has some CSS classes:

- MeshFillArea and MeshFillAreaDark drive the fill colors of mesh objects
- IconOutline sets the color and default thickness to 1.5
- ThinDotOutline sets the dash according to the style guide
- ThickOutline sets the stroke width to 3 PX.

There will be a small refacoring of the outline classes to allow using the dots also in thick lines. I also need to style the small + / - icon in the bottom right corner since it will be part of the 'dynamic' color change' for using the icons on light themes.

### Where I can find the CSS in Inkscape?

open the XML editor, scroll all the way up to the beginning of the file

    <svg:defs id="MeshDefs">
    <svg:style id="GR-Mesh>

## TODO

- Create an empty template with some examples and the style pallette to copy colors from
- test if embedding CSS renders properly as is, and refine the workfloww accordingly (class names, etc).
- implement some work tracking metodology (trello? github project?) and let's make clear who is working on what

Don't hesitate to ping me (GentlemanRider) here, on the discord channel or FreeCAD forum.
