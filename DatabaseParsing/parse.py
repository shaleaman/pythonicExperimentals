import os
from collections import Counter
""" DEFINITIONS """

def formatline(line):
    sline = line.rstrip()
    fline = sline.split('\t')
    return fline

def tally(list):
    c = Counter(list)
    return c

""" VARIABLES """

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'Code_Violation_Cases.txt')

keys = ""
cells = []
val = []
searchkey = ""
subkeys = ""
vallist = []
maindict = {}

""" MAIN """

file = open(filename)

#BUILD 2D TABLE FROM FILE
for ind,i in enumerate(file):
    if ind == 0:
        keys = formatline(i)
    else:
        cells.append(formatline(i))

#DEFINE OUR SEARCH KEY
searchkey = keys.index("Case Type")

#GET ALL VALUE TYPES FROM searchkey AND GET UNIQUE VALUES
for cl in cells:
    val.append(cl[searchkey])

subkeys = (tally(val)).keys()

#RETURN THE INDICIES OF TABLE ROWS INTO SEPARATE LISTS BASED ON UNIQUE VALUES
for skey in subkeys:
    for indx,cel in enumerate(cells):
        if cel[searchkey] in skey:
            vallist.append(indx)
    maindict[skey] = vallist
    vallist = []
print(maindict)
print(cells[597])
