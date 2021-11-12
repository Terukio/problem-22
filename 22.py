names = open("p022_names.txt", "r")
data = names.read()
names.close()

dataList = []

currentName = ''

for char in data:
    if char == '"':
        continue
    elif char != ',':
        currentName = currentName + char
    elif char == ',':
        dataList.append(currentName)
        currentName = ''

dataList.sort()

print(dataList)

pprint.pprint(dataList)

dataDictionary = {}

def score(name):
    scoreKey = {' ' : 0}
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = 0
    i = 1
    for char in alpha:
        scoreKey[char] = i
        i += 1
    for char in name:
        score += scoreKey[char]
    return score

print('COLIN has a score of',score('COLIN'))


for i in dataList:
    if i in dataDictionary.keys():
        sys.exit()
    dataDictionary[i] = score(i)

pprint.pprint(dataDictionary)

i = 0

totalScore = 0

print(dataList[0])

for k, v in dataDictionary.items():
    i += 1
    score2 = i * v
    print(k,v,i*v,totalScore)
    totalScore += score2
