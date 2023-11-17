import argparse
import os.path
import re
import xml.etree.ElementTree as ET

def scand(direc,excludes):
    excludes = excludes or []
    excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'
    resources = []
    for path, dirs, files in os.walk(direc):
        # exclude files
        files = [os.path.join(path, f) for f in files]
        files = [f for f in files if not re.match(excludes, f)]
        resources += files
    return resources


mClasses= ['IconOutline','DotOutline']

parser = argparse.ArgumentParser(description='replaces CSS on SVG Files')
parser.add_argument('CSS', metavar='CSS', type=str, help ='Style sheet to be injected')
args = parser.parse_args()

if not os.path.isfile(args.CSS):
    print('CSS file does not exist. Aborting')
else:
    f = open(args.CSS,"r")
    CSSlines = f.readlines()
    CSSContent =""
    
    for line in CSSlines:
        CSSContent += line #+ "\n"
    
    classCount = 0
    for mClass in mClasses:
        if mClass in CSSContent:
            classCount += 1

    if (classCount < len(mClasses)):
    #if True:
        print(len(mClasses))
        print(classCount)
        print('{} mandatory classes are missing in the CSS File. Aborting'.format( len(mClasses)-classCount ))
    else:
        print('\n-------CSS Style--------\n')
        print(CSSContent)
        print('\n-------CSS Style--------\n')
        choice = input('are you sure? Y/n  ')
        if choice == "" or choice == "y" or choice == "Y":
            res = scand(".", [])
            fileCount = 0
            for r in res:
                if ".svg" in r:
                    fileCount += 1
                    print('Injecting -> {}'.format(r)) #show me the file name
                    tree = ET.parse(r)
                    root = ET.parse(r).getroot()
                    for child in root[0]: 
                        if (child.tag == '{http://www.w3.org/2000/svg}style'):
                            child.text = CSSContent #replace the CSS entry
                    tree._setroot(root)
                    tree.write(r) #save file
            print('\n{} files processed\n'.format(fileCount))
        else:
            print('\nGoodbye\n')
