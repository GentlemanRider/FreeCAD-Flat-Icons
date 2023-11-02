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

- Icon set: a groups of icons, being from the same workbench  / add on if they are small (Mesh, spreadsheet for example) or parts of them (Sketcher Constraints, Sketcher Geometry).
- Icon package: the collection of all the exported icons
- Master file: a multipage SVG file that includes an icon set
- Batch export: exporting a single icon set from Inkscape GUI
- Action file: a file that instructs Inkscape what to render from CLI
- Package export: exporting several icon sets from the respective master files automatically (uses action files)
- CSS injection: automated CSS replacement on all the master files.
- Package render: the combination of CSS injection amd package export 

## What do we want to achieve by implementing CSS?

The idea is to use the same icon package for both dark and light themes.

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightGoal.png" alt="drawing" style="width:400px;"/>

To achieve this, there should be a common standard for CSS classes.

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightClasses.png" alt="drawing" style="width:500px;"/>

# Why are we adding such level of complexity on top of an aready huge task?

The sheer quantity of workbenches, modules and functions requires roles, coordination and efficent tool chains. There is also requirement for a quite wide skill set to do it, ranging from digging the source code, understanding svg, css, xml, scripting language, QCC compiling. I want to give the possibility to people that don't have the whole skill set to be able to contribute. For example: a brilliant Inkscape designer that has no clue of all the other aspects should be able to join and get support. He shouldn't forcefully dig on the other aspects (unless wants to): he should be put in a condition where he can put his skill at work immediately.



- Source code digger: a person who is familiar with the FreeCAD source and helps understanding which file goes rehdered where. Sometimes it's not trivial. Supports building templates for master files and action files. 
- Icon set artist: a person that takes charge of a workbench and draws symbols the corresponding master file according to the (style guide) and (CSS conventions)
- Tooling developer: a person that builds, maintains and documents scripts and best practices
- CSS maintainer: a person that ensures that the global CSS files are in sync with the master files. He also renders the package. 

# Where to go next

## Starting a new workbench / add on set.

So, I if someone wills to implement icons, what he should do? Refer to (CreatePackage.md)

### Action files

It seems possible to call inkscape from the command line and perform tasks defined in a 'action file'. I'm still trying to find documentation for that. The aim is to:

- call a single bash script
- the script creates two folders: one for QCC compiling and one for legacy mode
- calls inkscape with the action file as argument
- inkscape export the page in all master files to the output directories with proper names. Yes, sometimes they need to be diffferent. QCC uses the original icons names, legacy mode wants the function names.
- in the action file we can also specify to export an icon multiple times with different scales, different names, different format. I never faced that, but there is a function in Linkstage3 for multiple mappping. If that does not get ported, we will survive with multiple exports.

If we manage to build this, once we have proper master files the package building and / or re-render happens with two shell commands at max. Ideally, QCC compiling could be automated as well?

### Packing it all up

To implement the multipage / CSS workflow to the whole thing, we need to:

- merge the original single files into multipage documents (per module / workbench)
- refactor the original symbols by deleting style attributes from the elements and using classes instead
- define and document how the development of an icon set should start and how it should proceed to ensure compatibility with the workflow

## Icon Theme legacy mode

The icon theme add-on allows to use the icons in the actual program in legacy mode by just copying all of them into a specific folder. To be recognized, it needs the presence of a folder called license (_at least on my machine_). The addon github page has documentation for that.

_Note: the default setting directory is /home/user/.FreeCAD. Running appimage on Ubuntu 22 is located in /home/user/.local/share/FreeCAD_
