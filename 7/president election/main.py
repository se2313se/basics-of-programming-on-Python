inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
inFileLines = inFile.readlines()
words = dict()
k = 0
for line in inFileLines:
    line = line.strip()
    if line not in words:
        words[line] = 0
    words[line] += 1
    k += 1
s = []
for word in words:
    s.append([-words[word], word])
s.sort()
if k > 1:
    if (-s[0][0]) / k > 0.5:
        print(s[0][1], file=outFile)
    else:
        print(s[0][1], file=outFile)
        print(s[1][1], file=outFile)
else:
    print(s[0][1], file=outFile)
