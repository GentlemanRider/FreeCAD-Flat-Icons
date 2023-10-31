# Inkscape workflow
This document describes the workflow and best practices. (by who? for who? for what?)

## Prerequisites
- Latest dev version from the FreeCAD repository (link)
- Opendark Preference pack (installs from addon manager) (link)
- Icon Themes Add-on (installs from addon manager) (link)
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

### What do we want to achieve by implementing CSS?
The idea is to use the same icon set for both dark and light themes.

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightGoal.png" alt="drawing" style="width:400px;"/>

To achieve this, there should be a common standard for CSS classes. To minimize the effort and the error potential, I suggest using only two mandatory classes: 
- one specifies the outline color
- one specifies a background fill (not the actual background, elements that we want maximum contrast against the outline).

<img src="https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/DarkVsLightClasses.png" alt="drawing" style="width:500px;"/>

### Why are we adding such level of complexity on top of an aready huge task?
To my understanding, the development of the flat icon pack has been mostly a one man show with the occasional pull request. I like the theme, want to contribute and want other to be able to join without driving the original author crazy. Scaling up with workforce requires coordination and efficent tool chains.

The folder (tbd) contains a file named (TBD) which contains two empty pages, a set of sample icons, and has the CSS style sheet already embedded.

![Sample page](https://github.com/GentlemanRider/FreeCAD-Flat-Icons/blob/wip_GR_newIcons/Workflow/Images/SamplePage.PNG "Sample Page")


# Starting a new workbench / add on set.
So, I if someone wills to implement icons, what he should do?

### Retrieving the file (page) names
First, we need to know what icons a given package will implement.

I grabbed a list by running: find -name '*.svg on the root of the source repository. 1935 results. 

*Next step can be a scanner.ipynb that generats SVG files with the pages already defined?*

### Creating pages in Inkscape
Start from the template file (or any of the master files fom the directory (link)). Create / rename the pages according to the module required file names.

*Note: the list generation and the actual icon drawing can be done by different people? Guys familiar with the source code can populate the lists and other can draw the icons*

Select the page tool from the bottom of the left toolbar, the page toolbox appears on the top toolbar.

(screeenshots TBD)

The master file should contain one page for each icon used ina given workbench or add-on. It is possible to move the pages around using the page tool. Elements can exist outside the pages, they will be ignored during export. I keep working copies and other miscellaneous stuff there if I need.

*Note: it might be helpflul in the long ran to have md files paired to the SVGs to track the working status. Or whatever tracking tool (github issues?) is more efficient* 

## Create the icons
(------ instructions on how to handle CSS in a separate file -----)



# Batch export
## Doing it from inkscape GUI

Once the multipage document is ready it is possible to export all the pages as single files using the batch export option.

The output file name corresponds to the page name. Seems like Inkscape wants to add a prefix to the exported files; the files then need to be renamed or they will not be seen by the theme add on. I foud a workaround doing batch rename on the terminal: rename 's/^...//' *.svg will rename all the svg files in a directory removing the first three characters. 

*Note: having empty pages in the file will result in empty output files. Deselect them from the batch export toolbox or use some kind of placeholder in Inkscape*

## Doing it properly (WIP)
The master files folder should contain:
- the multi page SVG files
- one (or more) CSS style files (dark, light, etc)
- a script that inserts a CSS file in all the masters (takes the CSS file as argument)
- a script that launches the export
  
### Centralized CSS
The CSS is defined in the <defs <style>> part of the SVG. It is an XML so it is manageable from pytnon, as XML tree or raw text file. The script gets called with something like *python3 setStyle.py -s prodark.css*

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
The icon theme add-on allows to use the icons in the actual program in legacy mode by just copying all of them into a specific folder. To be recognized, it needs the presence of a folder called license (*at least on my machine*). The addon github page has documentation for that.

*Note: the default setting directory is /home/user/.FreeCAD. Running appimage on Ubuntu 22 is located in /home/user/.local/share/FreeCAD* 

