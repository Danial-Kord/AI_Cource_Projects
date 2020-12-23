import ds



def finalResult(resultNode):
    print("")
    print("final result")
    resultNode.currentNodeState()
    print("")
    print("result depth:")
    print(resultNode.depth)
    print("")
    print("in memory nodes")
    print("explored nodes : " + str(len(explored)))
    print("all nodes nodes : " + str(len(frontier) + len(explored)))



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
    placementI = ds.Placement()
    if(t != "#"):
        data = t.split(" ")
        for j in data:
            placementI.addCard(ds.Card(j[1],int(j[0])))
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

graphDepth=1
# root.calculateH()
# print(root.H)

# input()


print("start")
while notFinished:

    if len(frontier) == 0:
        print("no answer!")
        break
    
    expandNode = frontier[0]
    l = len(frontier)
    index = 0
    for i in range(1,l):
        print(frontier[i].H)
        if(frontier[i].H < expandNode.H):
            expandNode = frontier[i]
            index = i
    expandNode = frontier.pop(index)

    newNode = ds.Node(k,expandNode.placements,expandNode.depth)

    explored.append(expandNode)
    condidates = []
    for i in expandNode.placements:
        if(i.isNotEmpty()):
            condidates.append(i.seeLastCard().number)
        else:
            condidates.append(-1)

    print("")
    print("new node")
    newNode.currentNodeState()

    for i in range(k):
        for j in range(k):
            if j == i:
                continue
            # print(i)
            # print(j)
            # print(" ")
            if condidates[i] != -1:
                if condidates[j] > condidates[i] or condidates[j] == -1:
                    if newNode.changeCardPlace(i, j, explored, frontier):
                        # print("append")
                        newNode.calculateH()
                        frontier.append(newNode)
                        if newNode.checkFinalState(n):
                            finalResult(newNode)
                            notFinished = False
                            break
                        newNode = ds.Node(k,expandNode.placements,expandNode.depth)

