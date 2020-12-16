import ds

frontier = []
explored = []

c = ds.Node()
card = ds.Card()
card.setValues("R",1)

c.addCard(card,True)

print(c.seeLastCard().number)

