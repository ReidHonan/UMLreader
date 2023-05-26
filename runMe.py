# this is a default file name just in case one is not supplied.
import sys
from Parser import Parser
filename = "Playschool Example 1.uxf"
if len(sys.argv) > 1:
    filename = sys.argv[1]
p1 = Parser()
p1.parseUMLetino(filename)
p1.printClasses()
p1.printRelations()
p1.printDiagram()
p1.classPlurals()


