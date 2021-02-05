import codecs

def getDictionary(path):
    myDict = {}
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
    return myDict






ferdowsiPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\train_set\\ferdowsi_train.txt"
hafezPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\train_set\\hafez_train.txt"
molaviPath = "C:\\Danial\\Projects\\python\\AI_Cource_Projects\\Project 3\\train_set\\molavi_train.txt"


ferdowsiDict = getDictionary(ferdowsiPath)
hafezDict = getDictionary(hafezPath)
molaviiDict = getDictionary(molaviPath)



# for x, y in ferdowsiDict.items():
#   print(x, y) 

# print("-------")
# for x, y in hafezDict.items():
#   print(x, y) 

# print("-------")
# for x, y in molaviiDict.items():
#   print(x, y) 




