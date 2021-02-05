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

l3 = 0.6
l2 = 0.3
l1 = 0.1

e = 0.07


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



printItems(ferdowsiBiGram)









