import ds

frontier = []
explored = []

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

print(place2.placementData())

places = [place1,place2]


root2 = ds.Node(2,places)

root = ds.Node(2,places)
root.currentNodeState()

root.changeCardPlace(0,1)

root.currentNodeState()

print("  ")


root2.currentNodeState()


# will use the "befire node sxpandation condition" for optimization purposes

