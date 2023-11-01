# Inkscape workflow

This document describes the workflow and best practices. (by who? for who? for what?)

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

### What do we want to achieve by implementing CSS?

The idea is to use the same icon set for both dark and light themes.

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightGoal.png" alt="drawing" style="width:400px;"/>

To achieve this, there should be a common standard for CSS classes.

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightClasses.png" alt="drawing" style="width:500px;"/>

### Why are we adding such level of complexity on top of an aready huge task?

To my understanding, the development of the flat icon pack has been mostly a one man show with the occasional pull request. I like the theme, want to contribute and want other to be able to join without driving the original author crazy. Scaling up with workforce requires coordination and efficent tool chains.

![Sample page](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/SamplePage.PNG "Sample Page")

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
