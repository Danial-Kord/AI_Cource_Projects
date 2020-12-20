import ds

frontier = []
explored = []

input1 = input("enter: stations(K) Colors(m) number od every card(n) : ")
input1 = input1.split(" ")
k = int(input1[0]) #k places
m = int(input1[1]) #color types
n = int(input1[2]) #number of every color

places = []
for i in range(k):
    t = input("enter values with space blank between them : ")
    if(t != "#"):
        data = t.replace(" ","")
        placementI = ds.Placement(data)
        places.append(placementI)
    else:
        placementI = ds.Placement("")
        places.append(placementI)     

    



root = ds.Node(k,places)
root.currentNodeState()


# root.changeCardPlace(0,2)

# root.currentNodeState()

print("  ")


# root2.currentNodeState()


# will use the "before node sxpandation condition" for optimization purposes

notFinished = True
frontier.append(root)

newNode = None
print("start")
while notFinished:

    if len(frontier) == 0:
        break
    expandNode = frontier.pop(0)
    newNode = ds.Node(k,expandNode.placements)
    explored.append(expandNode)
    lastNodeStatus = []
    for i in expandNode.placements:
        if i.isNotEmpty():
            lastNodeStatus.append(i.seeLastCard())
        else:
            lastNodeStatus.append("9")
    print("")
    print("new node")
    newNode.currentNodeState()

    for i in range(k):
        for j in range(k):
            if j == i or lastNodeStatus[i] >= lastNodeStatus[j]:
                continue
            # print(i)
            # print(j)
            # print(" ")
            if newNode.changeCardPlace(i, j, explored, frontier):
                # print("append")
                frontier.append(newNode)
                if newNode.checkFinalState(2*n):
                    print("")
                    print("final result")
                    newNode.currentNodeState()
                    notFinished = False
                    break
                newNode = ds.Node(k,expandNode.placements)

