# Flat icons pack style guide
<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/LogoTransition.png" alt="drawing" style="width:800px;"/>

# Design language
(add screenshot of some icons from different WBs)

The icons should have a common look and feel that can be obtained through the definition of policies and constraints.
- fixed outline thickness and color, with a thicker outline on the shapes contour
- no gradients, nowhere.
- avoid strongly saturated colors
- simple shapes with sharp corners
- 'orthographic view' feeling for 3D elements

## Legacy icon affinity
<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/LegacyVsNewMesh.png" alt="drawing" style="width:600px;"/>
To avoid confusion, the icons shoud recall somehow the existing ones. The tooltip solves the issue in the end, but it should be relatively easy to follow tutorials and reference documentation, which include the classic UI. The logo on top of this page should give an idea. In this example, green was discarded for mesh since it's already used for other things (see patterns below) and purple was choosen instead. The outline similarities in this case shouls help users to not get lost.

## Minimalism
<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/MeasureOldVsNew.png" alt="drawing" style="width:400px;"/>

The simpler the shape, the better the readability at all scales. If the original icon represent a phisycal object, try to use a simpler equivalent instead.

*Note: that particular icon is NOT consistent with this guide*

## Patterns, common actions
(Screenshot of some additive vs subtractive functions)

Development should keep focus on recognizing common actions and represent them visualy in a consistent, recognizable style.

### Import - export
Import icons should have a green arrow on the left pointing to the center. The path must have the *ImportArrow* class and empty style attribute.

Export icons should have a red arrow on the left pointing to the border. The path must have the *ExportArrow* class and empty style attribute.

### Additive and subtractive operations
Operations that add items (or volume to solids) should be green. They should have the "+" icon on the bottom left corner.

Operations that remove items (or volume from solids) should be red. They should have the "-" icon on the left corner.

Operations that create 'bigger' things can be differentiated using a centered "+" icon.

# Implementation details

## CSS driven styles
Inkscape and QT both support CSS styling on SVG elements. This is beneficial because it enforces style consistency and also allows to alter the style at a later stage in a centralized manner. (if you are thinking about a future light version, you are right). The provided (path and filename) CSS file includes all the classes referenced in this guide.

## Flat slanted perspective
<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DynamicDataExamples.png" alt="drawing" style="width:800px;"/>

- dynamic data workbench icon.
- add property icon (falls into the additive style pattern)
- delete property icon (falls into the subtractive style pattern)
- copy property (falls close to copypaste command)
  
When representing a physical flat object (a notebook page, in the example above), a slight skew is strongly recommended to give a common visual style. To obtain the effect: 

- draw the overall outline squared, then apply skew -10 (right side high).
- Inkscape does not alter the X axis, so there will be some kind of elongation on circular path. To correct this, scale width 98%, height 100%. It might require to apply the scale more times, depending on the shape to make it loook 'right'.
- Please keep the same angle for visual consistency when icons from different packages appears at the same time on the screen.
- Also, try to always have the right side higher.

## Icon outlines
<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/LineThicknessOriginal.png" alt="drawing" style="width:400px;"/>
The standard outline for the element is 1.5 px. The paths  shoud not have any stle property and belong to the *IconOutline* class.
A thicker outline of 3px across the overall shape is used to increase readability at small scales. The overall outline should match the regular outline on the inside, so it needs to be offset. To achieve this:

- select all the shapes then copy, paste and merge them (*ctrl + c, v, +*).
- set the resulting path with no style and add the *IconOutline* and *ThickOutline* classes.
- snap the path on top of the icon
- select *path / outset* from the Inkscape menu.
  

