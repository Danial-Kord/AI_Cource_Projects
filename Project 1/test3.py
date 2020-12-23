import ds

frontier = []
explored = []
k = 3 #k places

place1 = ds.Placement()
card1 = ds.Card("R",1)
card2 = ds.Card("G",2)
place1.addCard(card1,True)
place1.addCard(card2,True)

print(place1.placementData())

place2 = ds.Placement()
card12 = ds.Card("G",3)
card22 = ds.Card("R",4)
place2.addCard(card12,True)
place2.addCard(card22,True)

place3 = ds.Placement()


print(place2.placementData())

places = [place1,place2,place3]

root = ds.Node(3,places)
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
        print("no answer!")
        break
    
    expandNode = frontier[0]
    l = len(frontier)
    index = 0
    for i in range(1,l):
        if(frontier[i].H < expandNode.H):
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

                        frontier.append(newNode)
                        if newNode.checkFinalState(2):
                            print("")
                            print("final result")
                            newNode.currentNodeState()
                            notFinished = False
                            break
                        newNode.calculateH()
                        newNode = ds.Node(k,expandNode.placements,expandNode.depth)

