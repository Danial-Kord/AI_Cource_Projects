class Card:
    def __init__(self):
        self.color = "" #R,G or B
        self.number = 1
    def setValues(self,color,number):
        self.color = color
        self.number = number

class Node:
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

    def seeLastCard(self):
        return self.contain[self.length-1]

    def popLastCard(self):
        self.length-=1
        return self.contain.pop(self.length)