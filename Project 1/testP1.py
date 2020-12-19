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

    print("")
    print("new node")
    newNode.currentNodeState()

    for i in range(k):
        if(notFinished):
            for j in range(k):
                if j == i:
                    continue
                # print(i)
                # print(j)
                # print(" ")
                if newNode.changeCardPlace(i, j, explored, frontier):
                    # print("append")
                    frontier.append(newNode)
                    if newNode.checkFinalState(2):
                        print("")
                        print("final result")
                        newNode.currentNodeState()
                        notFinished = False
                        break
                    newNode = ds.Node(k,expandNode.placements)

