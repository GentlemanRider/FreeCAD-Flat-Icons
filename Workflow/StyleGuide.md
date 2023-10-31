

### Legacy icons affinity
When creating an icons set it's strongly recommended to maintain visual affinity with the existing icons. The tooltip solves the issue in the end, but it should be relatively easy to follow tutorials and reference documentation, which tipycally include the classic UI.

### Flat slanted perspective
When representing a flat object, a slight skew is strongly recommended to give a common visual style.

Draw the overall outline squared, then apply skew -10 (right side high). Inkscape does not alter the X axis, so there will be some kind of elongation on circular path. To correct this, scale width 98.481%, height 100%.

Having the right side up it's not mandatory but strongly recommended for consistency. 

### Icon outlines

The standard outline for the element is (hex code), 1.5 px. The paths  shoud not have any stle property and belong to the *IconOutline* class.

A

## Common actions
To maintain consistency across icons and workbenches, it is necessary to adopt simular symbols for similar actions. Tihs chapter describes the patterns recognized so far and how are they presented on the icons. 

*Common symbols should be also categoryzed and collected in a reference file*

### Import -export
Import icons should have a green arrow on the left pointing to the center. The path must have the *ImportArrow* class and empty style attribute.

Export icons should have a red arrow on the left pointing to the border. The path must have the *ExportArrow* class and empty style attribute.

### Additive and subtractive operations
Operations that add items (or volume to solids) should be green. The paths must have the *AdditiveFill* class. They should also have the "+" icon on the bottom left corner.

Operations that remove items (or volume from solids) should be red. The paths must have the *SubtractiveFill* class. They should also have the "-" icon on the left corner.

Operations that create 'bigger' things can be differentiated using a centered "+" icon.
