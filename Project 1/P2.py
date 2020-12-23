import copy

def getLastCard(input):
    return int(input[-2])

def checkFinalState(data,n):
    for i in data:
        if len(i) == 0:
            continue
        if(len(i) < n):
            return False
        t = i[1]
        for j in range(1,len(i),2):
            if(t != i[j]):
                return False
    return True

frontier = []
explored = []

input1 = input("enter k m n: ")
input1 = input1.split(" ")
k = int(input1[0]) 
m = int(input1[1]) 
n = int(input1[2]) 

stations = []
for i in range(k):
    t = input()
    if(t != "#"):
        data = t.replace(" ","")
        stations.append(data)
    else:
        data = t.replace("#","")
        stations.append(data)

    


depth = 1
frontierDepth = []
cond = True
frontier.append(stations)
frontierDepth.append(0)
newStation = None
while cond:

    if len(frontier) == 0:
        frontierDepth = []
        frontier = []
        explored = []
        depth+=1
        frontier.append(stations)
        frontierDepth.append(0)
    expandNode = frontier.pop()
    newStation = copy.deepcopy(expandNode)
    lastNodeStatus = []
    for z in range(k):
        if expandNode[z] != "":
            lastNodeStatus.append(getLastCard(expandNode[z]))
        else:
            lastNodeStatus.append(99999)
    print("\nnode")
    for z in newStation:
        print(z)

    newDepth = frontierDepth.pop()


    for i in range(k):
        for j in range(k):
            if j == i or lastNodeStatus[i] >= lastNodeStatus[j]:
                continue
            
            temp = False

            new = newStation[i][-2:]
            newStation[i] = newStation[i][0:-2]
            newStation[j] += new
            for v in frontier:
                if(v == newStation):
                    temp = True
            if(temp):
                newStation = copy.deepcopy(expandNode)
                continue
            for h in explored:
                if(h == newStation):
                    temp = True
            if(temp):
                newStation = copy.deepcopy(expandNode)
                continue
            if(newDepth+1 != depth):
                frontierDepth.append(newDepth+1)
                frontier.append(newStation)
            if checkFinalState(newStation, 2 * n):
                print("")
                print("final result")
                print("\nnode")
                for z in newStation:
                    print(z)
                cond = False
                break
            newStation = copy.deepcopy(expandNode)
        explored.append(expandNode)
