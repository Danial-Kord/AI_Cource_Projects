import copy

def getLastCard(input):
    return int(input[-2])

def checkFinalState(data):
    t = data[1]
    for i in range(1,len(data),2):
        if(t != data[i]):
            return False
    return True

frontier = []
explored = []

input1 = input("enter: stations(K) Colors(m) number od every card(n) : ")
input1 = input1.split(" ")
k = int(input1[0]) 
m = int(input1[1]) 
n = int(input1[2]) 

places = []
for i in range(k):
    t = input("enter values with space blank between them : ")
    if(t != "#"):
        data = t.replace(" ","")
        places.append(data)
    else:
        data = t.replace("#","")
        places.append(data)

    



notFinished = True
frontier.append(places)

newNode = None
while notFinished:

    if len(frontier) == 0:
        break
    expandNode = frontier.pop(0)
    newNode = expandNode.copy()
    explored.append(expandNode)
    lastNodeStatus = []
    for i in expandNode:
        if i != "":
            lastNodeStatus.append(getLastCard(i))
        else:
            lastNodeStatus.append(9)
    print("")
    print("new node")
    for i in newNode:
        print(i)

    for i in range(k):
        for j in range(k):
            if j == i or lastNodeStatus[i] >= lastNodeStatus[j]:
                continue
            
            temp = False

            new = newNode[i][-2:]
            newNode[i] = newNode[i][0:-2]
            newNode[j] += new
            for v in frontier:
                if(v == newNode):
                    temp = True
                    break
            if(temp):
                continue
            for v in explored:
                if(v == newNode):
                    temp = True
                    break
            if(temp):
                continue

            # print("append")
            frontier.append(newNode)
            if(len(newNode) == 2*n):
                if checkFinalState(newNode):
                    print("")
                    print("final result")
                    newNode.currentNodeState()
                    notFinished = False
                    break
            newNode = expandNode.copy()

