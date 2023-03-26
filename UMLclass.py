class UMLClass:

    def __init__(self, inTitle, inAttributes, inX, inY, inH, inW):
        self.Title = inTitle
        self.Attributes = inAttributes
        self.X = int(inX)
        self.Y = int(inY)
        self.H = int(inH)
        self.W = int(inW)
        self.Neighbours = []


    def __str__(self):
        return f"Title: {self.Title}, Attributes: {self.Attributes}, X: {self.X}, Y: {self.Y}, H: {self.H}," \
               f" W: {self.W}, Degree: {self.getDegree()}, Neighbours: {self.Neighbours}"

    def getDegree(self):
        return len(self.Neighbours)

    def addNeighbour(self, neigh: str):
        self.Neighbours.append(neigh)

    def removeNeighbour(self, neigh: str):
        self.Neighbours.remove(neigh)

