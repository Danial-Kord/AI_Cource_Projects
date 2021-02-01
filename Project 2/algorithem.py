import ds
import copy


def forwardChecking(table,node):
    number = node.number
    color = node.color
    iIndex = node.i
    jIndex = node.j
    if number != None:
        for i in range(n):
            if table[i][jIndex].number is None:
                if table[i][jIndex].setNumberConstraint(str(number) +","):
                    return False
            if table[iIndex][i].number is None:
                if table[iIndex][i].setNumberConstraint(str(number) +","):
                    return False

    if color is not None:
        if iIndex-1 >=0:
            checkNode = table[iIndex-1][jIndex]
            if checkNode.color is None:
                checkNode.setColorConstraint(str(color)+",")
        if iIndex+1 < n:
            checkNode = table[iIndex+1][jIndex]
            if checkNode.color is None:
                checkNode.setColorConstraint(str(color)+",")
        if jIndex-1 >=0:
            checkNode = table[iIndex][jIndex-1]
            if checkNode.color is None:
                checkNode.setColorConstraint(str(color)+",")

        if jIndex+1 < n:
            checkNode = table[iIndex][jIndex+1]
            if checkNode.color is None:
                checkNode.setColorConstraint(str(color)+",")

    if color is not None and number is not None:
        if iIndex-1 >=0:
            checkNode = table[iIndex-1][jIndex]
            if checkNode.number is None and checkNode.color is not None:
                if checkNode.setNumberConstraintGroup(node):
                    return False
            elif checkNode.number is not None and checkNode.color is None:
                if checkNode.setColorConstraintGroup(node):
                    return False
            
            
        if iIndex+1 < n:
            checkNode = table[iIndex+1][jIndex]
            if checkNode.number is None and checkNode.color is not None:
                if checkNode.setNumberConstraintGroup(node):
                    return False
            elif checkNode.number is not None and checkNode.color is None:
                if checkNode.setColorConstraintGroup(node):
                    return False
        if jIndex-1 >=0:
            checkNode = table[iIndex][jIndex-1]
            if checkNode.number is None and checkNode.color is not None:
                if checkNode.setNumberConstraintGroup(node):
                    return False
            elif checkNode.number is not None and checkNode.color is None:
                if checkNode.setColorConstraintGroup(node):
                    return False
        if jIndex+1 < n:
            checkNode = table[iIndex][jIndex+1]
            if checkNode.number is None and checkNode.color is not None:
                if checkNode.setNumberConstraintGroup(node):
                    return False
            elif checkNode.number is not None and checkNode.color is None:
                if checkNode.setColorConstraintGroup(node):
                    return False
    return True
        
    
def printData(table):   
    print("table : \n")
    for i in table:
        text = ""
        for j in i:
            c = j.color
            n1 = j.number
            if c is None:
                c = "#"
            if n1 is None:
                n1 = "*"
            text += str(n1) + str(c) +" "
        print(text)

def printconstraints(table):   
    print("table : \n")
    for i in table:
        text = ""
        for j in i:
            text += str(j.index)+" " + j.numberDomain + "N " + j.colorDomain + "C " +"--"
        print(text)

            



table = []


input1 = input("input n m: ")
input1 = input1.split(" ")
m = int(input1[0])
n = int(input1[1])

input1 = input("input colors : ")
colors = input1.split(" ")

initialColorConstraint = ""
initialNumberConstraint = ""

for i in range(n):
    initialNumberConstraint += str(i+1) +","

for i in range(m):
    initialColorConstraint += str(i+1) +","

for i in range(n):
    input2 = input()
    input2 = input2.split(" ")
    row = []
    Jindex=0
    for j in input2:
        num = None
        color = None
        if j[0] != "*":
            num = int(j[0])
        if j[1] != "#":
            color = m - (colors.index(j[1])) #get priority of input color
        newElement = ds.element(i,Jindex,m,n,color,num)
        if num is not None:
            newElement.blockNumber()
        if color is not None:
            newElement.blockColor()
        row.append(newElement)
        Jindex+=1
    table.append(row)

printData(table)
input("wait...in")


# set initial constraints
for i in table:
    for j in i:
        j.setColorDomain(initialColorConstraint)
        j.setNumberDomain(initialNumberConstraint)


printconstraints(table)
input("wait...in")

for i in table:
    for j in i:
        forwardChecking(table,j)

printconstraints(table)
input("wait...in")

# set number constraints
for i in range(n):
    for j in range(n):
        if table[i][j].number is not None:
            number = table[i][j].number
            for k in range(n):
                if k != j:
                    table[i][k].setNumberConstraint(str(number) + ",")
            for k in range(n):
                if k != i:
                    table[k][j].setNumberConstraint(str(number) + ",")
        
        if table[i][j].color is not None:
            color = table[i][j].color
            if i-1 >=0:
                table[i-1][j].setColorConstraint(str(color) + ",")
            if i+1 < n:
                table[i+1][j].setColorConstraint(str(color) + ",")
            if j-1 >=0:
                table[i][j-1].setColorConstraint(str(color) + ",")
            if j+1 < n:
                table[i][j+1].setColorConstraint(str(color) + ",")
actions = []

newTable = copy.deepcopy(table)

numberMrv = []
minNumberDomain = newTable[0][0].numberDomainLen

colorMrv = []
minColorDomain = newTable[0][0].colorDomainLen

currentActionSecuence = ""
forbiddenActions = []

while(True):
    for i in range(n):
        for j in range(m):
            # finding mrv of color and number atributes
            if table[i][j].number == None:
                if table[i][j].numberDomainLen < minNumberDomain:
                    numberMrv.clear()
                    numberMrv.append(table[i][j])
                elif table[i][j].numberDomainLen == minNumberDomain:
                    numberMrv.append(table[i][j])
            if table[i][j].color == None:
                if table[i][j].colorDomainLen < minColorDomain:
                    colorMrv.clear()
                    colorMrv.append(table[i][j])
                elif table[i][j].colorDomainLen == minColorDomain:
                    colorMrv.append(table[i][j])
    if len(numberMrv) == 1:
        currentActionSecuence+= str(numberMrv[0].index)+ "N"

        
    
    
    
    






        

        


