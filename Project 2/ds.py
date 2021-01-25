class element:
    def __init__(self,colorDomain,numberDomain,color = None,number = None):
        #from 0 to m for color, 0 to n for number
        self.color = color
        self.number = number
        self.blockNums = False
        self.blockColors = False
        self.colorDomain = colorDomain
        self.numberDomain = numberDomain

    def blockNumber(self):
        self.blockNums = True
        
    def blockColor(self):
        self.blockColors = True

    def setColorDomain(self,newDomain):
        self.colorDomain = newDomain

    def setNumberDomain(self,newDomain):
        self.numberDomain = newDomain
    
    def setColorConstraint(self,constraint):
        self.colorDomain = self.colorDomain.replace(constraint,"")
        return len(self.colorDomain) is not 0

    def setNumberConstraint(self,constraint):
        self.numberDomain = self.numberDomain.replace(constraint,"")
        return len(self.numberDomain) is not 0
            