# Flat icon pack: a mid term maintenance plan

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/WorkflowOverview.svg" alt="original to flat logo" style="width:800px;"/>

## Components description

### SVG Masters

Multi page, CSS based Inkscape files. One per workbench, add on, or whatever category makes sense. 

### CSS themes

Cascading style sheet files. The classes must match the ones used in the SVG masters. For this reason, each SVG master file will contain ALL the classes and we have a [CSS classes reference](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/CssClasses.md).

### Action files

These files (bash or Inkscape action files) contain the mapping between the SVG master and the output folders. Legacy mode (which is very handy for testing) requires different file names in some cases. This also allows to export an icon with different names and formats: for example, one for toolbar and one for tree view.

### Set theme

A script that takes a CSS file as parameter and injects it into the SVG Masters.

### Render

A script that calls the action files an explodes all the pages in the SVG master into the Legacy mode and QSS folders.

# Development and maintenance

## Adding icons

See [how to implement an icon set](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/CreatePackage.md) for detailed instructions, and follow the [style guide](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/StyleGuide.md).

## Porting existing stuff

There will be two steps:

- include all the existing icons into master files (CreateIconSet.md)
- refactor them with CSS styles.

Grouping them can be done as soon as we want, CSS refactoring is postponed until there is some kind of rigidity and peer review in the design patterns and CSS classes definition.

## Scripting

There will be necessity to generate the package in the following scenarios:

- re-render with new / updated styles
- commit of new / updated icon sets

The package creation should be automated to the greatest possible extent. It sould not be necessary to manually open all the master files manually and batch export from Inlscape GUI. Then redo with different CSS when there will be more styles.

### Centralized CSS

Inkscape includes the CSS part in the header section of the files. They should all derive from a common template and no manual work should be required to make them ready. However if this is not the case, they can be manually fixed by changing 2 IDs from the XML editor.

The def part shold be called _FlatIconDefs_ and the style entry should be called _FlatIconsStyle_

The style entry in inkscape is embraced in a ![CDATA[]] construct:

    id="FlatIconDefs"><style
        id="FlatIconStlyle"><![CDATA[
        .IconOutline { stroke:#f5f4f4;  fill:none;  stroke-width:1.5; }
        .ThinDotOutline { stroke-dasharray:0.1, 2.5;  stroke-linecap:round;
    }]]></style>

A python script will load the CSS file given as parameter, add the CDATA header and footer, inject it on the XML tree of all SVG files in a given directory. This can happen in the master files or utput files. 

Changing theme should happen with a single command:

    python3 cssInjector.py dark.css

### Building action files
The inkscape CLI does not support pages yet, so it will be necessary to add geometry for placeholders. Since the files are on XML format, it should be possible to implement a python script that will modify the master svg file:

- scans the XML tree and fetches the label and coordinates from all the inkscape:page nodes
- creates a series of rectangles with matching IDs, size and placement. Those rectangles will all belong to a specific class that makes them invisible. If manual adjustment is necessary, altering the fill-opacity attribute in that class makes them visible all together.
- all the references will be on a specific, hidden and locked layer to they won't mess the design process.

While it's looping through the pages, it will create the action file as well.

It is possible to manually fine tune the action files if necessary, for example exporting the same icon with different names or even different file formats. 

_Note: during icon set development, batch export and legacy mode usually get the work done. The action files are meant as a step where a icon set is done and enter the pool for automated rendering._

### Batch export
After applying the desired CSS theme to the master files, having all the action files created, an iteration of 

    inkscape --actions-file=setName.iact setName.svg

for all the master files will produce all the single icons.



