l = list(map(int, input().split()))
i = 0
while 2 * i < len(l) - 1:
    c = l[2*i]
    l[2*i] = l[2*i + 1]
    l[2 * i + 1] = c
    i += 1
print(*l)
