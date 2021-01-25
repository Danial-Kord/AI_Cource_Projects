class element:
    def __init__(self,colorDomain,numberDomain,color = None,number = None):
        #from 0 to m for color, 0 to n for number
        self.color = color
        self.number = number
        self.blockNums = False
        self.blockColors = False
        self.colorDomain = colorDomain
        self.numberDomain = numberDomain
        self.colorDomainLen = 0
        self.numberDomainLen = 0

    def blockNumber(self):
        self.blockNums = True
        
    def blockColor(self):
        self.blockColors = True

    def setColorDomain(self,newDomain):
        self.colorDomain = newDomain
        self.colorDomainLen = len(newDomain)/2

    def setNumberDomain(self,newDomain):
        self.numberDomain = newDomain
        self.numberDomainLen = len(newDomain)/2
    
    def setColorConstraint(self,constraint):
        self.colorDomain = self.colorDomain.replace(constraint,"")
        self.colorDomainLen = len(self.colorDomain)/2
        return len(self.colorDomain) is not 0

    def setNumberConstraint(self,constraint):
        self.numberDomain = self.numberDomain.replace(constraint,"")
        self.numberDomainLen = len(self.numberDomain)/2
        return len(self.numberDomain) is not 0
            