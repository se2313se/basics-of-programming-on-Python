n = int(input())
aSet = set(range(1, n+1))
line = input()
while line != 'HELP':
    aLineSet = set(map(int, line.split()))
    answer = input()
    if answer == 'NO':
        tempSet = set(aLineSet)
        aSet -= tempSet
    elif answer == 'YES':
        tempSet = set(aLineSet)
        aSet &= tempSet
    line = input()
print(*sorted(list(aSet)))
