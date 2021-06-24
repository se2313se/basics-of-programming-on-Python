list = list(map(int, input().split()))
j = 1000
for i in range(0, len(list)):
    if j > list[i] > 0:
        j = list[i]
print(j)
