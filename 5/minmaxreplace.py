l = list(map(int, input().split()))
min = [l[0], 0]
max = [l[0], 0]
i = 0
while i < len(l):
    if l[i] < min[0]:
        min[0] = l[i]
        min[1] = i
    elif l[i] > max[0]:
        max[0] = l[i]
        max[1] = i
    i += 1
l[max[1]] = min[0]
l[min[1]] = max[0]
print(*l)
