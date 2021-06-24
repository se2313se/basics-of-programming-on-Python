n = int(input())
l = list(map(int, input().split()))
x = int(input())
d = (l[0] - x) ** 2
c = l[0]
i = 1
while i < n:
    d1 = (l[i] - x) ** 2
    if d1 < d:
        d = d1
        c = l[i]
    i += 1
print(c)
