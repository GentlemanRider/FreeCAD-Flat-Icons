# Workflow goals

The aim of a unified workflow is to:

- simplify icons creation and maintenance
- ensure style consistency
- build future proof icons, with the possibility to be styled at runtime and / or easily exported using different themes.

## How do we get there?

During this first development rush I found potential to be harvested in the following built in inkscape functions:

- Multi page files
- CSS styling
- Batch export
- external CSS injection
- automated export using action files

## Why Inkscape?
It's FOSS. And it works.

## Terminology
Since the scope of this documentation is growing, let's make clear what refers to what:

- **Icon set**: a group of icons, being from the same workbench / add on if they are small (Mesh, spreadsheet for example) or parts of them (Sketcher Constraints, Sketcher Geometry).
- **Icon package**: the collection of all the exported icons
- **Master file**: a multipage SVG file that includes an icon set
- **Master file template**: a multipage SVG without actual icons but with all the required pages in place with correct names and the master CSS already embedded.
- **Batch export**: the process of exporting a single icon set from Inkscape GUI
- **Action file**: a file that instructs Inkscape what to export from CLI
- **Package export**: exporting several icon sets from the respective master files automatically (uses action files)
- **CSS injection**: automated CSS replacement on all the master files in a given folder.
- **Package render**: the combination of CSS injection amd package export
- **Design pattern**: a functionality that is repeated, although with different nuances, in different places. Import - export is a bright example. 

## What do we want to achieve by implementing CSS?

The idea is to use the same master files for both dark and light themes (and whatever theme will spawn in the future).

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightGoal.png" alt="dark vs light" style="width:400px;"/>

To achieve this, there should be a common standard for CSS classes. 

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightClasses.png" alt="dark vs light classes" style="width:500px;"/>

# Why are we adding such level of complexity on top of an already huge task?

The sheer quantity of workbenches, modules and functions requires roles, coordination and efficent tool chains. 

The required skill set to approach the task ranges from digging the source code, understanding svg, css, xml, scripting languages, qss. Very few got them all.

I want to give the possibility to people that don't have the whole skill set to be able to contribute. For example: a brilliant Inkscape designer that has no clue of all the other aspects should be able to join and get support. He shouldn't forcefully dig on the other aspects (unless wants to): he should be put in a condition where he can express his skill.

- **Source code analysis**: understanding which file goes rendered where. Sometimes it's not trivial. Support building master file templates and tuning action files
- **Icon set drawing**: taking charge of a workbench and draws symbols in the corresponding master file according to the style guide and CSS conventions
- **Tooling development**: build, maintain and document scripts and best practices
- **CSS maintaining**: Ensuring that the global CSS files are in sync with the master files. Rendering the package(s) using the scripts. 

# Where we are

*Note: the folowing documents are still under development*

The [style guide](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/StyleGuide.md) focuses on UI/UX design aspects.

The [Prerequisites and settings](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/PrerequisitesAndSettings.md) contains the reference software versions and settings. __Some Inkscape settings are crucial to work with CSS properly__. Please do not skip this step.

The instructions for [how to implement an icon set](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/CreatePackage.md) dives into the CSS / multipage inkscape file handling and how to find the original icons.

The [CSS classes reference](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/CssClasses.md) goes into details of what classes are used where, how and why. How to create new ones if needed, how to keep it all together.

A description of the foreeseen [maintenance workflow](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/WorkflowPlan.md) and required tools is the place where I am trying to figure out how to maintain and extend the package. I think that keeping that in mind since the early stages of development helps taking wise design choices that won't bite in the future.

## Where to go next

- harmonize CSS definitions in the current under development sets (Mesh, Dynamic Data, Spreadsheet, Arch)
- build a svg with the style pattern elements (import export arrows, etc) that serves as reference for new sets
- consolidate CSS classes and the main design patterns
- Define a way to clearly state if somebody has taken charge of a given workbench. Let's avoid doing the work twice
- Prepare a starter kit and release it into the wild. (If we manage to go ahead with the style guide, we can think of a call for designers / developers. At Fosdem24?)
- merge the original single files into multipage documents (per module / workbench)
- refactor the original symbols by deleting style attributes from the elements and using classes instead



