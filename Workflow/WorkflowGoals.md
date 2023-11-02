# Workflow goals

The aim of a unified workflow is to:

- simplify icons creations and manintainability
- ensure style consistency
- build future proof icons, with the possibility to be styled at runtime.

## How do we get there?

During this first development rush I found potential to be harvested in the following built in inkscape funtions:

- Multi page files
- CSS styling
- Batch export

## Terminology
Since the scope of this codumentation is growing, let's make clear what refers to what:

- Icon set: a groups of icons, being from the same workbench / add on if they are small (Mesh, spreadsheet for example) or parts of them (Sketcher Constraints, Sketcher Geometry).
- Icon package: the collection of all the exported icons
- Master file: a multipage SVG file that includes an icon set
- Master file template: a multipage SVG without actual icons but with all the required pages in place with correct names and the master CSS already embedded.
- Batch export: exporting a single icon set from Inkscape GUI
- Action file: a file that instructs Inkscape what to render from CLI
- Package export: exporting several icon sets from the respective master files automatically (uses action files)
- CSS injection: automated CSS replacement on all the master files.
- Package render: the combination of CSS injection amd package export 

## What do we want to achieve by implementing CSS?

The idea is to use the same master files for both dark and light themes (and whatever theme will spawn in the future).

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightGoal.png" alt="drawing" style="width:400px;"/>

To achieve this, there should be a common standard for CSS classes. (see CssClasses.md)

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightClasses.png" alt="drawing" style="width:500px;"/>

# Why are we adding such level of complexity on top of an aready huge task?

The sheer quantity of workbenches, modules and functions requires roles, coordination and efficent tool chains. There is also requirement for a quite wide skill set to do it, ranging from digging the source code, understanding svg, css, xml, scripting language, QCC compiling. I want to give the possibility to people that don't have the whole skill set to be able to contribute. For example: a brilliant Inkscape designer that has no clue of all the other aspects should be able to join and get support. He shouldn't forcefully dig on the other aspects (unless wants to): he should be put in a condition where he can express his skill.

- Source code digger: a person who is familiar with the FreeCAD source and helps understanding which file goes rehdered where. Sometimes it's not trivial. Supports building master file templates and tuning action files
- Icon set artist: a person that takes charge of a workbench and draws symbols in the corresponding master file according to the (style guide) and (CSS conventions)
- Tooling developer: a person that builds, maintains and documents scripts and best practices
- CSS maintainer: a person that ensures that the global CSS files are in sync with the master files. He also renders the package(s) using the scripts. 

# Where we are

The style guide can be found here.
Instructions on how to implement icon sets can be found here (CreatePackage.md)
A description of the foreeseen maintenance prctice and required tools can be foung here (WorkflowMaintenance.md)

## Where to go next

- harmonize CSS definitions in the current under development sets
- build a svg with the style pattern elements (import export arrows, etc) that serves as reference
- merge the original single files into multipage documents (per module / workbench)
- refactor the original symbols by deleting style attributes from the elements and using classes instead

### Further ideas
