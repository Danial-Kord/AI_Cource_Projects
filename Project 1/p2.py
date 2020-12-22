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

print("start")
while notFinished:

    if len(frontier) == 0:
        graphDepth+=1
        print("changing max depth to " + str(graphDepth))
        frontier = []
        explored = []
        frontier.append(root)
    expandNode = frontier.pop(len(frontier)-1)
    newNode = ds.Node(k,expandNode.placements,expandNode.depth)

    explored.append(expandNode)

    print("")
    print("new node")
    newNode.currentNodeState()

    for i in reversed(range(k)):
        for j in range(k):
            if j == i:
                continue
            # print(i)
            # print(j)
            # print(" ")
            if newNode.changeCardPlace(i, j, explored, frontier):
                # print("append")
                if newNode.depth != graphDepth:
                    frontier.append(newNode)
                if newNode.checkFinalState(n):
                    print("")
                    print("final result")
                    newNode.currentNodeState()
                    notFinished = False
                    break
                newNode = ds.Node(k,expandNode.placements,expandNode.depth)

