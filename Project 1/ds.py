import copy

class Placement:
    def __init__(self,data):
        self.contain = data
        self.length = len(data)
        print("data : "+data +" len :" + str(self.length))
    def addCard(self,input,noCondition = False):
        self.length+=2
        self.contain += input

    def canAddCard(self,input,noCondition = False):
        if noCondition or self.length == 0:
            return True  
        else:   
            if self.contain[-2] > input[0]:
                return True
            else:
                return False


    def isNotEmpty(self):
        return self.length > 0

    def seeLastCard(self):
        return self.contain[-2:]

    def popLastCard(self):
        out = self.contain[-2:]
        self.length-=2
        self.contain = self.contain[0:-2]
        return out
    
    def PlacementfinalState(self,maxLength):
        if(self.length == 0):
            return True
        if(self.length == maxLength):
            last = self.contain[1]
            for i in range(1,maxLength,2):
                if self.contain[i] != last:
                    return False
            return True
        else:
            return False

    def placementData(self):
        return self.contain

class Node:
    def __init__(self,length,lastNodePlacement):
        self.placements = copy.deepcopy(lastNodePlacement)
        self.length = length

    def changeCardPlace(self,i,j,explored = None,frontier = None):
        # print("change status from :")
        # self.currentNodeState()
        self.placements[j].addCard(self.placements[i].popLastCard())

        # print("to : ")
        # self.currentNodeState()
        # print()
        if explored is not None:
            for b in explored:
                if self.compareWith(b):
                    self.placements[i].addCard(self.placements[j].popLastCard())
                    return False
        if frontier is not None:
            for b in frontier:
                if self.compareWith(b):
                    self.placements[i].addCard(self.placements[j].popLastCard())
                    return False
        return True

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
        return self.placements[index].placementData()

    def currentNodeState(self):
        for i in range(self.length):
            print("K"+ str(i+1) + ": " +self.placements[i].placementData())


    def checkFinalState(self,maxLength):
        for i in self.placements:
            if(i.PlacementfinalState(maxLength) == False):
                return False
        return True
