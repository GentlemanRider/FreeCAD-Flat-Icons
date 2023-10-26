# Inkscape workflow
This document describes the workflow and best practices.

## Prerequisites
- Latest dev version from the FreeCAD repository (link)
- Opendark Preference pack (install from addon manager) (link)
- Icon Themes Add-on (install from addon manager) (link)
- Inkscape 1.3 (other versions will do the job, but this guide refers to this particular version)


## Workflow goals
The aim of a unified workflow is to: 
- simplify icons creations and manintainability  
- ensure style consistency
- build future proof icons, with the possibility to be styled at runtime.

### How do we get there?
During this first development rush I found potential to be harvested in the following built in inkscape funtions:

- Multi page files
- CSS styling
- Batch export

### Starter kit
The folder (tbd) contains a file named (TBD) which contains two empty pages, a set of sample icons, and has the CSS style sheet already embedded. There is also a separate CSS file for reference.

![Sample page](./images/SamplePage.PNG "Sample Page")

![Sample CSS](./images/SampleCSV.PNG "Sample CSS")

## Starting a new workbench / add on set.

### Retrieving the page names

*Note: I did not manage to find an easy way to fetch the icons list from the source.
At the moment I am surviving by hovering on the icons on the toolbars and naming the pages with the funcion name, which is the last item onn the tooltip.*


### Creating pages in Inkscape
Select the page tool from the bottom of the left toolbar, the page toolbox appears on the top toolbar.

(screeenshots)

The master file should contain one page for each icon used ina given workbench or add-on. It is possible to move the pages around using the page tool. Elements can exist outside the pages, they will be ignored during export. I keep working copies and other miscellaneous stuff there if I need.

## Create a new icon
This chapter describes the step by step procedure to create an icon, according to the style guideline found here (link) and using CSS styling.

(screenshot of the sample icon)

## Create overall shapes
(screenshot of two shapes)

## Apply styles: shape fill
*Note: the native CSS selectors tool is buggy and lead to sudden Inkscape crashes. I always used the XML editor for this, it's less polished but more reliable.*

Working with CSS means that the fill / stroke toolbox on Inkscape is accessed very rarely. Instead, CSS classes are used to drive the shapes style eattributes. 

Select the element, assign it to a class from the XML editor (add a property named class type in one or more class names) and delete the 'style' property from the element itself.

(screenshot of the classes selection with properly colored shapes)

## Add thin outlines
Add the outline selectors to the overall shapes.

(screenshot of the classes selection with properly outlined shapes)

Draw the inner outlines, don't care about thicknesses, just make sure snapping is enabled and the paths are in the right places. 

(screenshot of the poorly styled inner outlines)

Then, go to the CSS selector toolbox and style the lines by assigning classes to the paths.

(screenshot of the properly styled inner outlines)

## Add dotted outlines

(---------------)

## Add shadow

Draw the shadow outline:

(screenshot of the poorly styled shadow)

Style it using the CSS selectors toolbox, then play around with stacking to place the shape at the required height for proper display.

(screenshot of the stack handling toolbar)

## Add overall outlines

The style guide states an overall outline thicker than the inner ones, and it must lineup internally (not on the path center).

#### Configure the default inset / outset

A simple way to achieve it is by growing the outline path by 0.75px. To do that on a single click, configure the outset offset in the inkscape preferences:
- Select *Edit / Preferences* from the inkscape menu
- *Behavior / steps* in the preference tree
- set *Inset/outset by:* to 0.75px

#### Create the overall outline path

Select the object backgound, copy, paste and merge them. Then add ThickOutline class.

Drag and snap the resulting shape on top of the icon, then select Path > Outset.

(-----------------)