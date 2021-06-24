list = list(map(int, input().split()))
j = 0
for i in range(0, len(list)):
    if list[i] > 0:
        j += 1
print(j)
