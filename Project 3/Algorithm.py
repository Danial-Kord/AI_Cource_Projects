import codecs

def getDictionary(path):
    myDict = {}
    myBiDict = {}
    with codecs.open(path, 'r', encoding='utf8') as f:
        Lines = f.readlines()
        for i in Lines:
            words = i.split(" ")
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


def calculatePropability(dict):
    total = 0
    for x in dict:
        total += dict[x]
    uniGramDict = {}
    for i in dict:
        uniGramDict[i] = dict[i] / total 
    return uniGramDict


def getPoemPropability(poem,unigram,bigram,l3,l2,l1,e):
    words = poem.split(" ")
    p = 0.0
    for i in range(1,len(words)):
        u = 0.0
        if unigram.__contains__(words[i]):
            u = unigram[words[i]]
        b = 0.0
        if bigram.__contains__(words[i-1] + " " + words[i]):
            b = bigram[words[i-1] + " " + words[i]]
        p += l3 * b + l2 * u + l1*e
    return p


def printItems(dict):
    for x, y in dict.items():
        print(x, y) 


ferdowsiPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\train_set\\ferdowsi_train.txt"
hafezPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\train_set\\hafez_train.txt"
molaviPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\train_set\\molavi_train.txt"


ferdowsiDict = getDictionary(ferdowsiPath)

cleanDict(ferdowsiDict[0],2)
cleanDict(ferdowsiDict[1],2)

hafezDict = getDictionary(hafezPath)
cleanDict(hafezDict[0],2)
cleanDict(hafezDict[1],2)

molaviiDict = getDictionary(molaviPath)
cleanDict(molaviiDict[0],2)
cleanDict(molaviiDict[1],2)

l3 = 0.8
l2 = 0.15
l1 = 0.05

e = 0.1


ferdowsiUniGram = calculatePropability(ferdowsiDict[0])
ferdowsiBiGram = calculatePropability(ferdowsiDict[1])

hafezUniGram = calculatePropability(hafezDict[0])
hafezBiGram = calculatePropability(hafezDict[1])

molaviUniGram = calculatePropability(molaviiDict[0])
molaviBiGram = calculatePropability(molaviiDict[1])

trainSet = []
trainSet.append((ferdowsiUniGram,ferdowsiBiGram))
trainSet.append((hafezUniGram,hafezBiGram))
trainSet.append((molaviUniGram,molaviBiGram))




testSetPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\test_set\\test_file.txt"


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
        poem = text[1]
        for j in trainSet:
            p.append(getPoemPropability(poem,j[0],j[1],l3,l2,l1,e))
        
        maximum = 0
        index = 0
        for j in range(len(p)):
            if p[j] > maximum:
                maximum = p[j]
                index = j
        if answer == index+1:
            print("nice job!")
            trueAnswers+=1
        else:
            print("wrong!")

successRate = trueAnswers / allAnswwers
print(successRate)





