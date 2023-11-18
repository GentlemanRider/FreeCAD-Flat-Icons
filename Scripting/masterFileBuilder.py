# ----------------------------------------------------------------
#--------------------- Svg head generation -----------------------
# ----------------------------------------------------------------

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   width="48"
   height="48"
   viewBox="0 0 48.000001 48"
   version="1.1"
   id="svg1387"
   sodipodi:docname="DynamicData.svg"
   inkscape:version="1.3 (1:1.3+202307231459+0e150ed6c4)"
   xml:space="preserve"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"><sodipodi:namedview
     id="namedview10"
     pagecolor="#505050"
     bordercolor="#ffffff"
     borderopacity="1"
     inkscape:showpageshadow="0"
     inkscape:pageopacity="0"
     inkscape:pagecheckerboard="1"
     inkscape:deskcolor="#505050"
     showgrid="false"
     inkscape:zoom="1.2727922"
     inkscape:cx="-199.56125"
     inkscape:cy="-181.0979"
     inkscape:window-width="1711"
     inkscape:window-height="1022"
     inkscape:window-x="709"
     inkscape:window-y="383"
     inkscape:window-maximized="0"
     inkscape:current-layer="layer2"
     showguides="true">"""

def insertDefs():
    return """<defs
     id="FlatIconDefs"><style
       id="FlatIconStlyle"><![CDATA[{css}
]]></style></defs>""".format(css= insertCSS())

def insertCSS():
    return """
.IconOutline { stroke:#f5f4f4;  fill:none;  stroke-width:1.5; }
.ThinDotOutline { stroke-dasharray:0.1, 2.5;  stroke-linecap:round; }
.ThickDotOutline { stroke-dasharray:0.1, 5;  stroke-linecap:round;  stroke-width:3; }
.ThickOutline { stroke-linejoin:miter;  stroke-miterlimit:3;  stroke-width:3; }
.CornerButton { stroke-width: 8;  stroke-linejoin: round; }
.OutlineAsFill { fill: #f5f4f4; }
.MeshFillArea { fill:#7950f2; }
.MeshFillAreaDark { fill:#6b4cc8; }
.DynDataFillArea { fill:#aea72c; }
.PartFillArea { fill:#3769ff }
.BgFillArea { fill: #495057; }
.AdditiveFillArea { fill: #40c057 }
.SubtractArea { fill: #f03e3e; }
.IntersectArea { fill: #4c6ef5; }
.ImportArrow { fill:#40c057; }
.ExportArrow { fill:#f03e3e; }
.GenericArrow { fill:#F5F4F4; }
.SketchFill { fill: #f5f4f4; }
.SketckOutline { stroke:#f03e3e; }
.SpreadsheetFill { fill: #868e96; }
.SpreadsheetLines { stroke:#495057; }
.PlaceHolder{ fill: #555555; fill-opacity: 0.5;}"""

# ----------------------------------------------------------------
#-------------------- Service Functions --------------------------
# ----------------------------------------------------------------

def genPage(id, count):
    return """<inkscape:page
       x="0"
       y="{y}"
       width="48"
       height="48"
       id="page{c}"
       margin="0"
       bleed="0"
       inkscape:label="{i}" />""".format(i= id, c = count, y = int(count * 96))

def genPlaceHolder(id, count):
    return """<rect
         width="48"
         height="48"
         class="PlaceHolder"
         id="PH_{i}"
         x="0"
         y="{y}" />""".format(i= id, c = count, y = int(count * 96))

def genActFileQSS(id):
    return "select-by-id:PH_{i};fit-canvas-to-selection;export-area-page;export-plain-svg;export-filename:Render/{i}.svg;export-do;select-clear;\n".format(i= id)

def genActFileLegacy(id):
    return "select-by-id:PH_{i};fit-canvas-to-selection;export-area-page;export-plain-svg;export-filename:Legacy/{i}.svg;export-do;select-clear;\n".format(i= id)

# ----------------------------------------------------------------
#----------------------- Input handling --------------------------
# ----------------------------------------------------------------
import argparse

parser = argparse.ArgumentParser(description='Generate a master file with pages')
parser.add_argument('fList', metavar='fList', type=str, help ='File list')
#parser.add_argument('outFile', metavar = 'outFile', type= str, help ='output file name')
args = parser.parse_args()

# ----------------------------------------------------------------
#-----------------------  --------------------------
# ----------------------------------------------------------------

import os.path

pages = ""
placeholders = ""
actionFile = ""

if not os.path.isfile(args.fList):
    print('CSS file does not exist. Aborting')
else:
    f = open(args.fList,"r")
    iconList = f.readlines()

    count = 0
    for icon in iconList:
        if ".svg" in icon:
            splitpath = icon.split("/")
            iconName = splitpath[len(splitpath)-1]
            iconName = iconName.split(".")[0]
            pages += genPage(iconName, count)
            placeholders += genPlaceHolder(iconName, count)
            actionFile +=  genActFileQSS(iconName)
            actionFile += genActFileLegacy(iconName) + "\n"
            count += 1
    
    svg += pages +"</sodipodi:namedview>"
    svg += insertDefs()
    svg += """<g
        inkscape:label="Placeholders"
        inkscape:groupmode="layer"
        id="layer1">
        sodipodi:insensitive="true"
        style="display:none">"""
    svg += placeholders + """ </g><g
        inkscape:groupmode="layer"
        id="layer2"
        inkscape:label="Icons" />
    </svg>"""

    outSvg = open("out.svg", "w")
    outSvg. write(svg)
    outSvg.close()

    outAct = open("out.act", "w")
    outAct.write(actionFile)
    outAct.close()
