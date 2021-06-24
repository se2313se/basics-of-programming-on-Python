inFile = open('input.txt', 'r', encoding='utf8')
inFileLines = inFile.readlines()
d = dict()
s = []
for line in inFileLines:
    tempLineList = list(line.split())
    for word in tempLineList:
        if word not in d:
            d[word] = 0
        s.append(d[word])
        d[word] += 1
print(*s)
