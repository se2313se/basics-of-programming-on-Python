list = list(map(int, input().split()))
j = 0
m = list[0]
for i in range(0, len(list)):
    if list[i] >= m:
        j = i
        m = list[i]
print(m, j)
