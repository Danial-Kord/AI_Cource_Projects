import ds
table = []


input1 = input("input n m: ")
input1 = input1.split(" ")
m = int(input1[0])
n = int(input1[1])

input1 = input("input colors : ")
colors = input1.split(" ")

initialColorConstraint = ""
initialNumberConstraint = ""

for i in range(n):
    initialNumberConstraint += str(i) +","

for i in range(m):
    initialColorConstraint += str(i) +","

for i in range(n):
    input2 = input()
    input2 = input2.split(" ")
    row = []
    for j in input2:
        num = None
        color = None
        if j[0] != "*":
            num = int(j[0])
        if j[1] != "#":
            color = colors.index(j[1]) #get priority of input color
        newElement = ds.element(m,n,color,num)
        if num is not None:
            newElement.blockNumber()
        if color is not None:
            newElement.blockColor()
        row.append(newElement)
    table.append(row)


# set initial constraints
for i in table:
    for j in i:
        if j.blockColors is not True:
            j.setColorDomain(initialColorConstraint)
        if j.blockNums is not True:
            j.setNumberDomain(initialNumberConstraint)

# set number constraints
for i in range(n):
    for j in range(n):
        if table[i][j].blockNums is True:
            number = table[i][j].number
            for k in range(n):
                if k != j:
                    table[i][k].setNumberConstraint(str(k) + ",")
            for k in range(n):
                if k != i:
                    table[k][j].setNumberConstraint(str(k) + ",")
        
        if table[i][j].blockColors is True:
            color = table[i][j].color
            for k in range(n):
                if k != j:
                    table[i][k].setColorConstraint(str(k) + ",")
            for k in range(n):
                if k != i:
                    table[k][j].setColorConstraint(str(k) + ",")





        

        


