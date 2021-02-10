import codecs

def getDictionary(path):
    myDict = {}
    myBiDict = {}
    with codecs.open(path, 'r', encoding='utf8') as f:
        Lines = f.readlines()
        for i in Lines:
            statement = "S " +i

            words = statement.split(" ")


            for j in words:
                encoded = j#.encode()
                if myDict.keys().__contains__(encoded) is False:
                    myDict[encoded] = 1
                else:
                    myDict[encoded] = myDict[encoded] + 1

            for j in range(1,len(words)):
                encoded = words[j-1] +" " +words[j] #.encode()
                if myBiDict.keys().__contains__(encoded) is False:
                    myBiDict[encoded] = 1
                else:
                    myBiDict[encoded] = myBiDict[encoded] + 1
            
    return myDict,myBiDict




def cleanDict(dict,limit):
    removeKeys = []
    for x, y in dict.items():
        if y < limit:
            removeKeys.append(x)
    for i in removeKeys:
        del dict[i]

def calculateBigram(biDict,uniDict):
    bigram = {}
    for i in biDict:
        if uniDict.keys().__contains__(i.split(" ")[0]):
            bigram[i] = biDict[i] / uniDict[i.split(" ")[0]] 
    return bigram



def calculateUnigram(dict):
    total = 0
    for x in dict:
        total += dict[x]
    uniGramDict = {}
    for i in dict:
        uniGramDict[i] = dict[i] / total 
    return uniGramDict


def getPoemPropability(poem,unigram,bigram,l3,l2,l1,e):
    words = poem.split(" ")
    p = 1
    for i in range(1,len(words)):
        u = 0.0
        if unigram.keys().__contains__(words[i]):
            u = unigram[words[i]]
        b = 0.0
        if bigram.keys().__contains__(words[i-1] + " " + words[i]):
            b = bigram[words[i-1] + " " + words[i]]
        p *= (l3 * b + l2 * u + l1*e)
    return p


def printItems(dict):
    for x, y in dict.items():
        print(x, y) 


ferdowsiPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\train_set\\ferdowsi_train.txt"
hafezPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\train_set\\hafez_train.txt"
molaviPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\train_set\\molavi_train.txt"


ferdowsiDict = getDictionary(ferdowsiPath)

cleanDict(ferdowsiDict[0],5)


hafezDict = getDictionary(hafezPath)
cleanDict(hafezDict[0],5)


molaviiDict = getDictionary(molaviPath)
cleanDict(molaviiDict[0],5)


l3 = 0.1
l2 = 0.85
l1 = 0.05

e = 0.05


ferdowsiUniGram = calculateUnigram(ferdowsiDict[0])
ferdowsiBiGram = calculateBigram(ferdowsiDict[1],ferdowsiDict[0])

hafezUniGram = calculateUnigram(hafezDict[0])
hafezBiGram = calculateBigram(hafezDict[1],hafezDict[0])

molaviUniGram = calculateUnigram(molaviiDict[0])
molaviBiGram = calculateBigram(molaviiDict[1],molaviiDict[0])

trainSet = []
trainSet.append((ferdowsiUniGram,ferdowsiBiGram))
trainSet.append((hafezUniGram,hafezBiGram))
trainSet.append((molaviUniGram,molaviBiGram))




testSetPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\test_set\\test case.txt"


# testcase = [
#     [0.2,0.2,0.6],
#     [0.4,0.2,0.5],
#     [0.4,0.1,0.6],
#     [0.3,0.3,0.4],
#     [0.33,0.33,0.33],
#     [0.4,0.5,0.1],
#     [0.6,0.3,0.1],
#     [0.9,0.05,0.05],
#     [0.99,0.008,0.002],
#     [0.008,0.99,0.002],
#     [0.05,0.15,0.8],
#     [0.75,0.20,0.05],
#     [0.2,0.75,0.05],
# ]

testcase = [

    [0.8,0.1,0.1],
    [0.7,0.2,0.1],
    [0.6,0.3,0.1],
    [0.5,0.4,0.1],
    [0.4,0.5,0.1],
    [0.3,0.6,0.1],
    [0.2,0.7,0.1],
    [0.1,0.8,0.1],
    [0.2,0.1,0.7],
    [0.1,0.3,0.6],
    [0.3,0.1,0.6],
    [0,0.9,0.01],
    [0.9,0,0.1],
    

]
es = [0,0.05,0.005]
file1 = open("C:\Danial\Projects\python\AI_Cource_Projects\Project 3\myfile.csv", "w")
t = "l3,;2,l1,e,success rate\n"
file1.write(t)
for e in es:
    for w in testcase:
        v = w[0]
        h = w[1]
        s = w[2]
        successRate = 0
        allAnswwers = 0
        trueAnswers = 0
        with codecs.open(testSetPath, 'r', encoding='utf8') as f:
            Lines = f.readlines()
            allAnswwers = len(Lines)
            for i in Lines:
                text = i.split("\t")
                answer = int(text[0])
                p = []
                poem = "S " + text[1]
                for j in trainSet:
                    p.append(getPoemPropability(poem,j[0],j[1],v,h,s,e))
                
                maximum = 0
                index = 0
                for j in range(len(p)):
                    if p[j] > maximum:
                        maximum = p[j]
                        index = j
                if answer == index+1:
                    # print("nice job!")
                    trueAnswers+=1
                # else:
                #     print("wrong!")

        successRate = trueAnswers / allAnswwers
        print("---")
        t = str(v)+","+str(h)+","+str(s)+","+str(e)+","+str(successRate)+"\n"
        print(t.split(","))
        file1.write(t)
        print("---")

file1.close()




