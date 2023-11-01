# Flat icon pack expansion campaign

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/WorkflowOverview.svg" alt="drawing" style="width:800px;"/>

## Components description

### SVG Masters
Multi page, CSS based Inkscape files. One per workbench, add on, or whatever category makes sense.

### CSS themes
Cascading style sheet files. The classes must match the ones used in the SVG masters. For this reason, each SVG master file will contain ALL the classes.

### Action files
These files (bash or Inkscape action files) contain the mapping between the SVG master and the output folders. Legacy mode (which is very handy for testing) requires different file names in some cases. This also allows to export an icon with different names and formats: for example, one for toolbar and one for tree view.

### Set theme
A script that takes a CSS file as parameter and injects it into the SVG Masters. Being them all derived from a starting document, the style will (must) be defined in the same namespace of the XML Tree. It is possible to take it further and alter the inkscape page, border and color settings so it's possible to draw directly in the preferred theme. 

### Render
A script that calls the action files an explodes all the pages in the SVG master into the Legacy mode and QSS folders.

# Development and maintenance

## Creating a package
The bare minimum package development happens with a SVG file, derived from an existing package or from the template file. This ensures that the CSS part contains the standard classes.

### Creating the scope
The first step is to understand which icons will be part of the package. Depending on the target, there are three possible places to look at. For add ons is usually enough  to have them installed. 

#### Add-ons
It's recommended to start from a relatively small add on to familiarize with the processes and tools.
Navigate to the FreeCAD preference folder, then Mod/<desired_addon>. Look for SVG files in the folder structure by typing 
    
    find -name '*.svg' 
    
in the add on folder. For Dynamic Data, this is the result:

    ./Resources/icons/Settings.svg
    ./Resources/icons/DynamicDataCreateConfiguration.svg
    ./Resources/icons/DynamicDataSVGLogo.svg
    ./Resources/icons/DynamicDataLogo.svg
    ./Resources/icons/CreateObject.svg
    ./Resources/icons/AddProperty.svg
    ./Resources/icons/DynamicDataPreferencesLogo.svg
    ./Resources/icons/ImportAliases.svg
    ./Resources/icons/CopyProperty.svg
    ./Resources/icons/DynamicDataEditEnumerations.svg
    ./Resources/icons/ImportNamedConstraints.svg
    ./Resources/icons/RemoveProperty.svg

Create all the required pages in Inkscape (see Inkscape guide TBD). The page labels must match the original file names:

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/WorkflowInkscapePages.png" alt="drawing" style="width:800px;"/>

#### Standard icons
It is possible to look for SVG files from the github web interface, gowever I recommend cloning the source report to your machine:

    git clone https://github.com/FreeCAD

Follow the step as per the add ons in the 

### Importing reference material
There can be reference material in the master file as long as it is outside the pages borders. A quick way is to navigate to the icons folder with the file manager and grab a screenshot:

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DynDataRefScreenshot.png" alt="drawing" style="width:400px;"/>

A more tedious way is to grab the actual svg files and drag them into the inkscape pages. This requires more work but allows to export incomplete sets (the original icons will be exported if not done yet).

### Creating the icons
Refer to the Style Guide. Try to reuse shapes from the (patterns file TBD) wherever possible. Use only the included classes for outlines. It's okay to create classes for fill colors, as long as they are consistent with the style guide and have only fill attributes. 

### Exporting the icons
Select file / export from the Inkscape menu, then batch export trom the tabs on top of the export toolbox. Give the expott a short name since the result will be name+pagename

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DynDataPageExport.png" alt="drawing" style="width:400px;"/>

leave suffix blank, select 'plain svg' as file format. Click on the folder in the export path, choose the desired output directory and filename (2 letters). Navigate to the output folder and trim away the filenema prexif with:

    rename 's/^...//' *.svg

If you with to remove more characters, add dots.

### Preview your icons live on FreeCAD
Download the (legacy mode folder) and add your files to the content. Refer to the Icon Theme add on documentation for futher details.





