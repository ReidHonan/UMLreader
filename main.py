import sys
import xml.etree.ElementTree as ET


# this method separates the various sections of a class and adds them to the map at the end.
def parseUMLClass(input):
    data2 = input.find('panel_attributes')
    data2 = data2.text.splitlines()
    title = data2[0].lstrip('_')
    title = title.rstrip('_')
    i = 0
    attributes = ""
    for line in data2:
        if i > 2:
            attributes = attributes + ";" + line
        i = i + 1
    attributes = attributes.lstrip(';')

    data2 = input.find('coordinates')
    x = data2.find('x').text
    y = data2.find('y').text
    h = data2.find('h').text
    w = data2.find('w').text
    data = {
        'title': title,
        'attributes': attributes,
        'X': x,
        'Y': y,
        'H': h,
        'W': w
    }
    return data


# this method separates the various sections of a relation and adds them to the map at the end.
def parseRelation(input):
    data2 = input.find('panel_attributes').text
    data2 = data2.splitlines()
    if len(data2) == 4:
        title = data2[0].lstrip('lt=')
        m1 = data2[1].lstrip('m1=')
        m2 = data2[2].lstrip('m2=')
        if m1 == '..*':
            m1 = '1..*'
        if m2 == '..*':
            m2 = '1..*'
        text = data2[3]

    else:
        title = data2[0].lstrip('lt=')
        m1 = None
        m2 = None
        text = None
    aa = input.find('additional_attributes').text
    aa = aa.split(';')
    aa = [','.join(i) for i in zip(aa[::2], aa[1::2])]
    data3 = input.find('coordinates')
    x = data3.find('x').text
    y = data3.find('y').text
    h = data3.find('h').text
    w = data3.find('w').text
    data = {
        'linetype': title,
        'multiplicity1': m1,
        'multiplicity2': m2,
        'text': text,
        'additional_attributes': aa,
        'X': x,
        'Y': y,
        'H': h,
        'W': w
    }
    return data


# this method reviews each relation and identifies the end points of the relation. Most relations end in 2 classes,
# however association classes ('.') end with 1 class and 1 relation.
def matchRelationToClasses(classes, relations):
    relMap = []
    for rel in relations:
        relout = classin = classout = "TBD"  # this is a dummy variable to make sure that something is in the data.

        # if the linetype is a single dot '.' then it will not join 2 classes, instead it will join a relation
        # and a single class. (this is because it is an association class)
        if rel['linetype'] != '.':
            relX = int(rel['X'])
            relY = int(rel['Y'])
            relAdd = rel['additional_attributes']
            relAddX1 = int(relAdd[0].split(",")[0])
            relAddY1 = int(relAdd[0].split(",")[1])
            relAddXLast = int(relAdd[len(relAdd) - 1].split(",")[0])
            relAddYLast = int(relAdd[len(relAdd) - 1].split(",")[1])
            for cla in classes:
                claX = int(cla['X'])
                claY = int(cla['Y'])
                claH = int(cla['H'])
                claW = int(cla['W'])
                # check for start of relation
                if claX <= relX + relAddX1 <= claX + claW:
                    if claY <= relY + relAddY1 <= claY + claH:
                        classin = cla

                # check for end of relation
                if claX <= relX + relAddXLast <= claX + claW:
                    if claY <= relY + relAddYLast <= claY + claH:
                        classout = cla

            relMapAdd = [rel, classin, classout]
            relMap.append(relMapAdd)
        else:
            print("Relation: " + str(rel))
            relX = int(rel['X'])
            relY = int(rel['Y'])
            relAdd = rel['additional_attributes']
            relXA = relX + int(relAdd[0].split(",")[0])  # the X coord of the start of the relationship
            relYA = relY + int(relAdd[0].split(",")[1])  # the Y coord of the start of the relationship
            relXB = relX + int(relAdd[len(relAdd) - 1].split(",")[0])  # the X coord of the end of the relationship
            relYB = relY + int(relAdd[len(relAdd) - 1].split(",")[1])  # the Y coord of the end of the relationship
            for cla in classes:
                claX = int(cla['X'])
                claY = int(cla['Y'])
                claH = int(cla['H'])
                claW = int(cla['W'])
                # check for start of relation
                if claX <= relXA <= claX + claW:
                    if claY <= relYA <= claY + claH:
                        classin = cla
                        # print("Classin update: " + str(cla))

                # check for end of relation
                if claX <= relXB <= claX + claW:
                    if claY <= relYB <= claY + claH:
                        classin = cla
                        # print("Classout update: " + str(cla))
            for rel2 in relations:
                if rel2['linetype'] != '.':
                    relAdd2 = rel2['additional_attributes']
                    rel2X = int(rel2['X'])
                    rel2Y = int(rel2['Y'])
                    for i in range(len(relAdd) - 1):
                        # we calculate the equation of the line based on the coords of the start and stop of each
                        # segment of the line. This accounts for lines being bounced around the diagram.
                        m, c = calculateLine(int(relAdd2[i].split(",")[0]) + rel2X,
                                             int(relAdd2[i].split(",")[1]) + rel2Y,
                                             int(relAdd2[i + 1].split(",")[0]) + rel2X,
                                             int(relAdd2[i + 1].split(",")[1]) + rel2Y)

                        # now that we have the equation of the line we can check if either end of the relationship
                        # matches a point on the line equation we just calculated.
                        if relYB == ((m * relXB) + c):
                            relout = rel2

                        if relYA == ((m * relXA) + c):
                            relout = rel2

            relMapAdd = [rel, classin, relout]
            relMap.append(relMapAdd)

    return relMap


# this method takes 2 sets of coordinates A and B and calculates the slope and intercept of a line.
# this is used to match relations to classes by predicting if an association relation ('.') touches another relation.
def calculateLine(coordAX, coordAY, coordBX, coordBY):
    deltaY = (coordBY - coordAY)
    deltaX = (coordBX - coordAX)
    m = 0
    if deltaX != 0:
        m = deltaY / deltaX
    c = coordBY - (m * coordBX)
    return m, c


# this method takes the filename of the .uxf file and elucidates the relevant information out of the diagram.
def parseUMLetino(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    UMLClasses = []
    relations = []
    # this section trawls the XML found inside the file and gets all the 'elements'
    for elements in root.iter('element'):
        # we then look at the id of each element and parse it as a class or a relation accordingly.
        for ids in elements.iter('id'):
            if ids.text == "UMLClass":
                UMLClasses.append(parseUMLClass(elements))
            if ids.text == "Relation":
                relations.append(parseRelation(elements))
    # from this function we have separated all the classes, the relations and finally matched the relations to their
    # end points
    return UMLClasses, relations, matchRelationToClasses(UMLClasses, relations)


# this is a default file name just in case one is not supplied.
filename = "Playschool Example 1.uxf"
if len(sys.argv) > 1:
    filename = sys.argv[1]
classes, relations, relToClasses = parseUMLetino(filename)

for item in classes:
    print(item)
print()

for item in relations:
    print(item)
print()

for mat in relToClasses:
    for item in mat:
        print(item)
    print()