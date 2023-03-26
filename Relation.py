class Relation:

    def __init__(self, inTitle: str, inM1: str, inM2: str, inText: str, inAddAtt, inX: int, inY: int, inH: int, inW: int):
        self.Linetype = inTitle
        self.M1 = inM1
        self.M2 = inM2
        self.Text = inText
        self.AA = inAddAtt
        self.X = int(inX)
        self.Y = int(inY)
        self.H = int(inH)
        self.W = int(inW)
        self.EndA = None
        self.EndB = None

    def __str__(self):
        return f"Linetype: {self.Linetype}, M1: {self.M1}, M2: {self.M2}, Text: {self.Text}, AA: {self.AA}," \
               f" X: {self.X}, Y: {self.Y}, H: {self.H}, W: {self.W}, EndA: {self.EndA}, EndB: {self.EndB}"