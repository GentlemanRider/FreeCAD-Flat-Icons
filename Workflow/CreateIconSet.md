# Creating an icon set

The bare minimum package development happens with a master SVG file, derived from an existing package or from the template file. This ensures that the CSS part contains the standard classes.

## Creating the scope

The first step is to understand which icons will be part of the package. Depending on the target, there are three possible places to look at. For add ons is usually enough to have them installed.

### Add-ons

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

### Standard icons

It is possible to look for SVG files from the github web interface, gowever I recommend cloning the source report to your machine:

    git clone https://github.com/FreeCAD

Follow the step as per the add ons in the previous section.

### Importing reference material

There can be reference material in the master file as long as it is outside the pages borders. A quick way is to navigate to the icons folder with the file manager and grab a screenshot:

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DynDataRefScreenshot.png" alt="drawing" style="width:400px;"/>

A more tedious way is to grab the actual svg files and drag them into the inkscape pages. This requires more work but allows to export incomplete sets (the original icons will be exported if not done yet).

### Creating the icons

Refer to the Style Guide. Try to reuse shapes from the (patterns file TBD) wherever possible. Use only the included classes for outlines. It's okay to create classes for fill colors, as long as they are consistent with the style guide and have only fill attributes.

### Exporting the icons

Select _file / export_ from the Inkscape menu, then _batch export_ trom the tabs on top of the export toolbox. Give the export a short name since the result will be name+pagename

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DynDataPageExport.png" alt="drawing" style="width:400px;"/>

leave suffix blank, select _plain svg_ as file format. Click on the folder in the export path, choose the desired output directory and filename (2 letters). Navigate to the output folder and trim away the filename prefix with:

    rename 's/^...//' *.svg

If you with to remove more characters, add dots.

### Preview your icons live on FreeCAD

The icon theme add-on allows to use the icons in the actual program in legacy mode by just copying all of them into a specific folder. To be recognized, it needs the presence of a folder called license (_at least on my machine_). The addon github page has documentation for that.

Download the (legacy mode folder TBD) and add your files to the content. Refer to the Icon Theme add on documentation for futher details.

_Note: the default setting directory is /home/user/.FreeCAD. Running appimage on Ubuntu 22 is located in /home/user/.local/share/FreeCAD_
