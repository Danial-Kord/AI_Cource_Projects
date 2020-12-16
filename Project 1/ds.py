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
        if noCondition:
            self.contain.append(input)
            self.length += 1
            return True  
        else:    
            if self.contain.__len__ == 0:
                self.contain.append(input)
                self.length += 1
                return True
            elif self.contain[self.length-1].number > input.number:
                self.contain.append(input)
                self.length += 1
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
    
    def finalState(self,maxLength):
        if(self.length == maxLength):
            for i in range(1,maxLength):
                if self.contain[i-1].color != self.contain[i].color:
                    return False
            return True
        else:
            return False

    def placementData(self):
        t = ""
        for i in self.contain:
            t += i.getCardData() + " "
        return t

class Node:
    def __init__(self,length,array):
        # self.placements = []
        # for i in range(length):
        #     elemnt = array[i]
        #     for
        #     p = Placement()
        #     p.addCard(.contain[i])
        #     self.placements.append(p)
        self.placements = copy.deepcopy(array)
        self.length = length

    def changeCardPlace(self,i,j):
        if self.placements[i].isNotEmpty():
            if self.placements[j].addCard(self.placements[i].seeLastCard()):
                self.placements[i].popLastCard()
                return True
        else:
            return False

    def currentNodeState(self):
        for i in range(self.length):
            print("K"+ str(i+1) + ":")
            print(self.placements[i].placementData())
