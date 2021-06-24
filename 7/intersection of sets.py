aSet = set(map(int, input().split()))
bSet = set(map(int, input().split()))
print(*sorted(aSet & bSet))
