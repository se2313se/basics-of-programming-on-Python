import sys

aText = sys.stdin.readlines()
aSet = set()
for line in aText:
    line = line.strip()
    for w in list(line.split()):
        if w.strip() not in aSet:
            aSet.add(w.strip())

print(len(aSet))
