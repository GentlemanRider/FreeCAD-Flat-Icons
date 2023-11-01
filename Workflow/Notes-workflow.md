# Flat icon pack expansion campaign

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/WorkflowOverview.svg" alt="drawing" style="width:800px;"/>

## Components description

### SVG Masters

Multi page, CSS based Inkscape files. One per workbench, add on, or whatever category makes sense. See (CreatePackage.md) for instructions on how to implement a package.

### CSS themes

Cascading style sheet files. The classes must match the ones used in the SVG masters. For this reason, each SVG master file will contain ALL the classes.

### Action files

These files (bash or Inkscape action files) contain the mapping between the SVG master and the output folders. Legacy mode (which is very handy for testing) requires different file names in some cases. This also allows to export an icon with different names and formats: for example, one for toolbar and one for tree view.

### Set theme

A script that takes a CSS file as parameter and injects it into the SVG Masters. Being them all derived from a starting document, the style will (must) be defined in the same namespace of the XML Tree.

_Maybe t is possible to take it further and alter the inkscape page, border and color settings so it's possible to draw directly in the preferred theme._

### Render

A script that calls the action files an explodes all the pages in the SVG master into the Legacy mode and QSS folders.

# Development and maintenance
