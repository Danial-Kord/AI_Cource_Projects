import copy

class Card:
    def __init__(self,color,number):
         #R,G or B
        self.color = color
        self.number = number

    def getCardData(self):
        return ""+self.color+ str(self.number)

class Placement:
    def __init__(self):
        self.contain = []
        self.length = 0

    def addCard(self,input,noCondition = False):
        self.contain.append(input)
        self.length += 1


    def canAddCard(self,input,noCondition = False):
        if noCondition or self.length == 0:
            return True  
        else:    
            if self.contain[self.length-1].number > input.number:
                return True
            else:
                return False
    def isNotEmpty(self):
        return self.length > 0

    def seeLastCard(self):
        return self.contain[self.length-1]

    def popLastCard(self):
        self.length-=1
        return self.contain.pop(self.length)
    
    def PlacementfinalState(self,maxLength):
        if(self.length == 0):
            return True
        if(self.length == maxLength):
            for i in range(1,maxLength):
                if self.contain[i-1].color != self.contain[i].color:
                    return False
            return True
        else:
            return False

    def placementData(self):
        if(self.length == 0):
            return "#"
        
        t = ""
        for i in self.contain:
            t += i.getCardData() + " "
        return t

class Node:
    def __init__(self,length,lastNodePlacement):
        # self.placements = []
        # for i in range(length):
        #     elemnt = array[i]
        #     for
        #     p = Placement()
        #     p.addCard(.contain[i])
        #     self.placements.append(p)
        self.placements = copy.deepcopy(lastNodePlacement)
        self.length = length

    def changeCardPlace(self,i,j,explored = None,frontier = None):
        # print("change status from :")
        # self.currentNodeState()
        if self.placements[i].isNotEmpty():
            if self.placements[j].canAddCard(self.placements[i].seeLastCard()):
                self.placements[j].addCard(self.placements[i].seeLastCard())
                self.placements[i].popLastCard()
                # print("to : ")
                # self.currentNodeState()
                # print()
                if explored is not None:
                    for b in explored:
                        if self.compareWith(b):
                            self.placements[i].addCard(self.placements[j].seeLastCard())
                            self.placements[j].popLastCard()
                            return False
                if frontier is not None:
                    for b in frontier:
                        if self.compareWith(b):
                            self.placements[i].addCard(self.placements[j].seeLastCard())
                            self.placements[j].popLastCard()
                            return False
                return True
        else:
            return False

    def compareWith(self,otherNode):
        check = False
        for j in range(self.length):
            check = False
            for i in range(self.length):
                if self.PlaceIndexTextData(i) == otherNode.PlaceIndexTextData(j):
                    check = True
            if check == False:
                return False
        return True

    def PlaceIndexTextData(self,index):
        t = self.placements[index].placementData()
        return t

    def currentNodeState(self):
        for i in range(self.length):
            print("K"+ str(i+1) + ": " +self.placements[i].placementData())


    def checkFinalState(self,maxLength):
        for i in self.placements:
            if(i.PlacementfinalState(maxLength) == False):
                return False
        return True
