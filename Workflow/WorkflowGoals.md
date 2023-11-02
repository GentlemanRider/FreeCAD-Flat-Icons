# Workflow goals

The aim of a unified workflow is to:

- simplify icons creations and manintainability
- ensure style consistency
- build future proof icons, with the possibility to be styled at runtime and / or easily exported using different themes.

## How do we get there?

During this first development rush I found potential to be harvested in the following built in inkscape funtions:

- Multi page files
- CSS styling
- Batch export
- external CSS injection
- automated export using action files

## Terminology
Since the scope of this documentation is growing, let's make clear what refers to what:

- Icon set: a group of icons, being from the same workbench / add on if they are small (Mesh, spreadsheet for example) or parts of them (Sketcher Constraints, Sketcher Geometry).
- Icon package: the collection of all the exported icons
- Master file: a multipage SVG file that includes an icon set
- Master file template: a multipage SVG without actual icons but with all the required pages in place with correct names and the master CSS already embedded.
- Batch export: the process of exporting a single icon set from Inkscape GUI
- Action file: a file that instructs Inkscape what to export from CLI
- Package export: exporting several icon sets from the respective master files automatically (uses action files)
- CSS injection: automated CSS replacement on all the master files in a given folder.
- Package render: the combination of CSS injection amd package export
- Design pattern: a functionality that is repeated, although with different nuances, in different places. Import - export is a bright example. 

## What do we want to achieve by implementing CSS?

The idea is to use the same master files for both dark and light themes (and whatever theme will spawn in the future).

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightGoal.png" alt="dark vs light" style="width:400px;"/>

To achieve this, there should be a common standard for CSS classes. 

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightClasses.png" alt="dark vs light classes" style="width:500px;"/>

# Why are we adding such level of complexity on top of an already huge task?

The sheer quantity of workbenches, modules and functions requires roles, coordination and efficent tool chains. There is also requirement for a quite wide skill set to do it, ranging from digging the source code, understanding svg, css, xml, scripting language, QCC compiling. I want to give the possibility to people that don't have the whole skill set to be able to contribute. For example: a brilliant Inkscape designer that has no clue of all the other aspects should be able to join and get support. He shouldn't forcefully dig on the other aspects (unless wants to): he should be put in a condition where he can express his skill.

- Source code digger: a person who is familiar with the FreeCAD source and helps understanding which file goes rendered where. Sometimes it's not trivial. Supports building master file templates and tuning action files
- Icon set artist: a person that takes charge of a workbench and draws symbols in the corresponding master file according to the style guide and CSS conventions
- Tooling developer: a person that builds, maintains and documents scripts and best practices
- CSS maintainer: a person that ensures that the global CSS files are in sync with the master files. He also renders the package(s) using the scripts. 

# Where we are

The [style guide](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/StyleGuide.md) focuses on UI/UX design aspects.

The [Prerequisites and settings](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/PrerequisitesAndSettings.md) contains the reference software versions and settings. _Some Inkscape settings are crucial to work with CSS properly_.

The instructions for [how to implement an icon set](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/CreateIconSet.md) dives into the CSS / multipage inkscape file handling and how to find the original icons.

The [CSS classes reference](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/CssClasses.md) goes into details of what classes are used where, how and why. How to create new ones if needed, how to keep it all together.

A description of the foreeseen [maintenance workflow](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/WorkflowPlan.md) and required tools is the place where I am trying to figure out how to maintain and extend the package. I think that keeping that in mind since the early stages of development helps taking wise design choices that won't bite in the future.

## Where to go next

- harmonize CSS definitions in the current under development sets
- build a svg with the style pattern elements (import export arrows, etc) that serves as reference
- consolidate CSS classes and design patterns
- Prepare a starter kit and release it into the wild
- merge the original single files into multipage documents (per module / workbench)
- refactor the original symbols by deleting style attributes from the elements and using classes instead



