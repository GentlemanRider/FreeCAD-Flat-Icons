# Flat icon pack: a mid term maintenance plan

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/WorkflowOverview.svg" alt="drawing" style="width:800px;"/>

## Components description

### SVG Masters

Multi page, CSS based Inkscape files. One per workbench, add on, or whatever category makes sense. See (CreatePackage.md) for instructions on how to implement a package.

### CSS themes

Cascading style sheet files. The classes must match the ones used in the SVG masters. For this reason, each SVG master file will contain ALL the classes.

### Action files

These files (bash or Inkscape action files) contain the mapping between the SVG master and the output folders. Legacy mode (which is very handy for testing) requires different file names in some cases. This also allows to export an icon with different names and formats: for example, one for toolbar and one for tree view.

### Set theme

A script that takes a CSS file as parameter and injects it into the SVG Masters.

### Render

A script that calls the action files an explodes all the pages in the SVG master into the Legacy mode and QSS folders.

# Development and maintenance

## Adding icons

refer to (CreateIconSet.md)

## Porting existing stuff

There will be two steps:

- include all the existing icons into master files (CreateIconSet.md)
- refactor them with CSS styles.

Grouping them can be done as soon as we want, CSS refactoring is postponed until there is some kind of rigidity and peer review in the CSS classes definition.

## Scripting

There will be necessity to generate the package in the following scenarios:

- re-render with new / updated styles
- commit of new / updated icon sets

The package creation should be automated to the greatest possible extent. It sould not be necessary to manually open all the master files manually and batch export from Inlscape GUI. Then redo with different CSS when there will be more styles.

### Centralized CSS (Set theme)

Inkscape includes the CSS part in the master files. They should all derive from a common template and no manual work should be required to make them ready. However if this is not the case, they can be manually fixed by changing 2 IDs from the XML editor.

The def part shold be called _FlatIconDefs_ and the style entry should be called _FlatIconsStyle_

The style entry in inkscape is embraced in a ![CDATA[]] construct:

    id="FlatIconDefs"><style
        id="FlatIconStlyle"><![CDATA[
        .IconOutline { stroke:#f5f4f4;  fill:none;  stroke-width:1.5; }
        .ThinDotOutline { stroke-dasharray:0.1, 2.5;  stroke-linecap:round;
    }]]></style>

A python script will load the CSS file given as parameter, add the CDATA header and footer, inject it on the XML tree of all SVG files in a given directory.

Changing theme should happen with a single command:

    python3 setStyle.py dark.css

### Automated export

This can be pure bash, with a series of entries like this, one for each master file:

    inkscape --without-gui --actions-file=DynamicData.iact DynamicData.svg

The Inkscape action file will contain entries for each page:

    "export-id:page01; export-id-only; export-filename:DynamidDataLogo.svg; export-do;"
    "export-id:page02; export-id-only; export-filename:DynamidCreateObject.svg; export-do;"

Building the actual package should happen calling a single command:

    ./build.sh
