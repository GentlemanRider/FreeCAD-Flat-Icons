# Introducion
The defaault inkscape behavior when copy /paste CSS style elements is to embed the style property on the pasted element syyle field. This overrides the global definition and prevents pasted elements from updating the style properlu when modifying the CSS classes. See (PrerequisitesAndSettings.md) in order to tweak the inkscape setting to disable this behavior.

Ideally, all the paths should not have element specific style attributes an rely on being members of the proper classes for styling. However, if the needs for overriding some style aspects arises, it is tolerated if it not conflicts with the classes attributes. 

# References
This document goes into the CSS implementation detail, refer to the  style guide for design choices and patterns.

# Common classes for all the icon sets

## Outlines
The stroke color and default stroke width are defined in a single class. Additional classes can be added to implement thicker line or dots. This allows to change the outline color in a single class for all the elements.

### IconOutline
This class is applied to all the icon outlines. It defines stroke color and width.

    .IconOutline { stroke:#f5f4f4;  fill:none;  stroke-width:1.5 }

### ThickOutline
This class is applied together with *IconOutline* to the general contour and sets a thicker stroke.

    .ThickOutline { stroke-width:3; }

### ThinDotOutline
This class is applied together with *IconOutline* to inner dotted lines.

    .ThinDotOutline { stroke-dasharray:0.1, 2.5;  stroke-linecap:round; }

## Filled areas

### OutlineAsFill
This class is used to fill areas with outline color. For example, the additive - subctractive corner indication shape.

    .OutlineAsFill { fill: #f5f4f4; }

### BgFillArea
This class is used to fill areas with a color that maximizes contrast with the outline. For example, the additive - subctractive corner inner symbol.

    .BgFillArea { fill: #495057; }

### AdditiveFillArea
This class is used for icons that add items, volume to solids.

    .AdditiveFillArea { fill: #40c057 }

### SubtractiveFillArea
This class is used for icons that remove items, volume to solids.

    .SubtractiveFillArea { fill: #f03e3e; }

### IntersectFillArea
This color is used for intersections, datum planes?

    .IntersectFillArea { fill: #4c6ef5; }

# Icon set specific classes
When a new icon set is started, it is possible to create specifiv classes for fill colors. Once the package is included in the master set for automated styling and rendering, it necessary to coordinate with the package maintainers to ensure the global CSS is updated with the relevant classes and the master file is properly integrated in the toolchain. 

This are the classes that are born during the development of mesh. For that particular set two fill colors have been used to give some kind of triangulation effect.

    .MeshFillArea { fill:#7950f2 }
    .MeshFillAreaDark { fill:#6b4cc8 }

Dynamic data only has a single specific fill:

    .DynDataFillArea { fill:#aea72c; }




