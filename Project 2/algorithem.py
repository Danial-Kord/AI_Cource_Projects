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
                if table[i][jIndex].setNumberConstraint(number):
                    return False
            if table[iIndex][i].number is None:
                if table[iIndex][i].setNumberConstraint(number):
                    return False

    if color is not None:
        if iIndex-1 >=0:
            checkNode = table[iIndex-1][jIndex]
            if checkNode.color is None:
                checkNode.setColorConstraint(color)
        if iIndex+1 < n:
            checkNode = table[iIndex+1][jIndex]
            if checkNode.color is None:
                checkNode.setColorConstraint(color)
        if jIndex-1 >=0:
            checkNode = table[iIndex][jIndex-1]
            if checkNode.color is None:
                checkNode.setColorConstraint(color)

        if jIndex+1 < n:
            checkNode = table[iIndex][jIndex+1]
            if checkNode.color is None:
                checkNode.setColorConstraint(color)

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
            n1 = j.number
            c = j.color
            if c is None:
                c = "#"
            else:
                c = colors[m - j.color]
            if n1 is None:
                n1 = "*"
            text += str(n1) + str(c) +" "
        print(text)

def printconstraints(table):   
    print("table : \n")
    for i in table:
        text = ""
        for j in i:
            text += str(j.index)+" " + str(j.numberDomain) + "N " + str(j.colorDomain) + "C " +"--"
        print(text)


            



table = []


input1 = input("input n m: ")
input1 = input1.split(" ")
m = int(input1[0])
n = int(input1[1])

input1 = input("input colors : ")
colors = input1.split(" ")


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
input("wait1...in")




printconstraints(table)
input("wait2...in")





for i in table:
    for j in i:
        if forwardChecking(table,j) is False:
            print("impossible soulotion input!")
            exit()

printconstraints(table)
input("wait4...in")




actions = []

initialTable = copy.deepcopy(table)

newTable = copy.deepcopy(table)

numberMrv = []
minNumberDomainLen = -1

colorMrv = []
minColorDomainLen = -1

currentActionSecuence = ""
forbiddenActions = []


establishedActions = {}





while(True):
    colorMrv.clear()
    numberMrv.clear()
    minNumberDomainLen = -1
    minColorDomainLen = -1
    for i in range(n):
        for j in range(n):
            # finding mrv of color and number atributes
            if table[i][j].number == None:
                if table[i][j].numberDomainLen < minNumberDomainLen or minNumberDomainLen == -1:
                    numberMrv.clear()
                    numberMrv.append(table[i][j])
                    minNumberDomainLen = table[i][j].numberDomainLen
                elif table[i][j].numberDomainLen == minNumberDomainLen:
                    numberMrv.append(table[i][j])
            if table[i][j].color == None:
                if table[i][j].colorDomainLen < minColorDomainLen or minColorDomainLen == -1:
                    colorMrv.clear()
                    colorMrv.append(table[i][j])
                    minColorDomainLen = table[i][j].colorDomainLen
                elif table[i][j].colorDomainLen == minColorDomainLen:
                    colorMrv.append(table[i][j])

    currentActionSecuenceTemp = copy.deepcopy(currentActionSecuence)

    searchNumber = True
    if len(numberMrv) == 0 and len(colorMrv) == 0:
        print("this is the end!")
        break
    elif len(numberMrv) > len(colorMrv) or len(numberMrv) == 0:
        searchNumber = False


    if searchNumber:
        selectedNum = None
        for j in numberMrv[0].numberDomain:
            currentActionSecuenceTemp = currentActionSecuence + str(numberMrv[0].index) + str(j)+ "N"
            check = True
            for i in forbiddenActions:
                if i.startswith(currentActionSecuenceTemp):
                    check = False
                    break
            if check:
                newTable[numberMrv[0].i][numberMrv[0].j].number = j
                if forwardChecking(newTable,newTable[numberMrv[0].i][numberMrv[0].j]):
                    table = copy.deepcopy(newTable)
                    selectedNum = j
                    break
                else:
                    newTable = copy.deepcopy(table)
                    forbiddenActions.append(currentActionSecuenceTemp)
        if selectedNum is not None:
            establishedActions[("N",numberMrv[0].i,numberMrv[0].j)] = selectedNum
            currentActionSecuence = currentActionSecuenceTemp
        else:
            table = copy.deepcopy(initialTable)
            establishedActions.popitem()
            if len(establishedActions) == 0:
                print("No possible answer for this CSP!")
                break
            forbiddenActions.append(currentActionSecuence)
            for i in establishedActions:
                node = table[i[1],i[2]]
                if i[0] == "N":
                    node.number = establishedActions[i]
                    forwardChecking(table,node)
                elif i[0] == "C":
                    node.color = establishedActions[i]
                    forwardChecking(table,node)

    else:
        selectedColor = None
        for j in colorMrv[0].colorDomain:
            print("<<" + str(j) + ">>" + str(colorMrv[0].colorDomain))
            currentActionSecuenceTemp = currentActionSecuence + str(colorMrv[0].index) + str(j)+ "C"
            check = True
            for i in forbiddenActions:
                if i.startswith(currentActionSecuenceTemp):
                    check = False
                    break
            if check:
                newTable[colorMrv[0].i][colorMrv[0].j].color = j
                if forwardChecking(newTable,newTable[colorMrv[0].i][colorMrv[0].j]):
                    table = copy.deepcopy(newTable)
                    selectedColor = j
                    print("selec :/ " + "--"+str(colorMrv[0].i) +"   " + str(colorMrv[0].j) + "--" + str(j))
                    break
                else:
                    newTable = copy.deepcopy(table)
                    print("--"+str(colorMrv[0].i) +"   " + str(colorMrv[0].j) + "--" + str(j))
                    forbiddenActions.append(currentActionSecuenceTemp)
        if selectedColor is not None:
            establishedActions[("C",colorMrv[0].i,colorMrv[0].j)] = selectedColor
            currentActionSecuence = currentActionSecuenceTemp
        else:
            printData(table)
            printconstraints(table)
            table = copy.deepcopy(initialTable)
            
            establishedActions.popitem()
            if len(establishedActions) == 0:
                print("No possible answer for this CSP!")
                break
            forbiddenActions.append(currentActionSecuence)
            for i in establishedActions:
                node = table[i[1],i[2]]
                if i[0] == "N":
                    node.number = establishedActions[i]
                    forwardChecking(table,node)
                elif i[0] == "C":
                    node.color = establishedActions[i]
                    forwardChecking(table,node)
    
printData(table)



                
                
            


            
            



        
    
    
    
    






        

        


