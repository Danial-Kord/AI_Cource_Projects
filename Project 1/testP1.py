import ds

frontier = []
explored = []
k = 3 #k places

place1 = ds.Placement("3R3G4R")


print(place1.placementData())

place2 = ds.Placement("7G1G2R")


place3 = ds.Placement("")


places = [place1,place2,place3]

root = ds.Node(3,places)
root.currentNodeState()

places = [place2,place1,place3]

root2 = ds.Node(3,places)


# root2.changeCardPlace(0,2)

print(root2.compareWith(root))

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
            lastNodeStatus.append(i.seeLastCard()[0])
        else:
            lastNodeStatus.append("9")
    print(lastNodeStatus)
    print("")
    print("new node")
    newNode.currentNodeState()

    for i in range(k):
        if(notFinished):
            for j in range(k):
                if j == i or lastNodeStatus[i] >= lastNodeStatus[j]:
                    continue
                # print(i)
                # print(j)
                # print(" ")
                if newNode.changeCardPlace(i, j,frontier,explored):
                    # print("append")
                    frontier.append(newNode)
                    if newNode.checkFinalState(6):
                        print("")
                        print("final result")
                        newNode.currentNodeState()
                        notFinished = False
                        break
                    newNode = ds.Node(k,expandNode.placements)

