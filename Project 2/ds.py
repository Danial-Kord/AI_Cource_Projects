class element:
    def __init__(self,i,j,colorDomain,numberDomain,color = None,number = None):
        #from 0 to m for color, 0 to n for number
        self.color = color
        self.number = number
        self.blockNums = False
        self.blockColors = False
        self.colorDomain = set()
        self.numberDomain = set()
        self.colorDomainLen = 0
        self.numberDomainLen = 0
        self.n = numberDomain
        self.m = colorDomain
        self.i = i
        self.j = j
        self.index = i*self.n + j
        self.setNumberDomain()
        self.setColorDomain()

    def blockNumber(self):
        self.blockNums = True
        
    def blockColor(self):
        self.blockColors = True

    def setColorDomain(self):
        for i in range(1,self.m+1):
            self.colorDomain.add(i)
        self.colorDomainLen = len(self.colorDomain)

    def setNumberDomain(self):
        for i in range(1,self.n+1):
            self.numberDomain.add(i)
        self.numberDomainLen = len(self.numberDomain)

    
    def addNumberDomain(self,newDomain):
        self.numberDomain.add(newDomain)
        self.numberDomainLen = len(self.numberDomain)

    
    def setColorConstraint(self,constraint):
        try:
            self.colorDomain.remove(constraint)
            self.colorDomainLen = len(self.colorDomain)
            return self.colorDomainLen is 0
        except KeyError:
            self.colorDomainLen = len(self.colorDomain)
            return self.colorDomainLen is 0



    def setNumberConstraint(self,constraint):
        try:
            self.numberDomain.remove(constraint)
            self.numberDomainLen = len(self.numberDomain)
            return self.numberDomainLen is 0
        except KeyError:
            self.numberDomainLen = len(self.numberDomain)
            return self.numberDomainLen is 0
    
    # def setNumberConstraintGroup(self,compareNum,beGreater):
    #     if beGreater:
    #         for i in range(compareNum,self.n+1):
    #             self.setNumberConstraint(str(i)+",")
    #     else:
    #         for i in range(1,compareNum+1):
    #             self.setNumberConstraint(str(i)+",")

    def setNumberConstraintGroup(self,compareNode):
        color = compareNode.color
        number = compareNode.number
        if color < self.color:
            for i in range(1,number+1):
                if self.setNumberConstraint(i):
                    return True
        elif color > self.color:
            for i in range(number,self.n+1):
                if self.setNumberConstraint(i):
                    return True
        else:
            return True
        return False

    def setColorConstraintGroup(self,compareNode):
        color = compareNode.color
        number = compareNode.number
        if number < self.number:
            for i in range(1,color+1):
                if self.setColorConstraint(i):
                    return True
        elif number > self.number:
            for i in range(color,self.m+1):
                if self.setColorConstraint(i):
                    return True
        else:
            return True
        return False



            