aList = list(map(int, input().split()))
aSet = set()
for a in aList:
    if a in aSet:
        print('YES')
    else:
        print('NO')
    aSet.add(a)
