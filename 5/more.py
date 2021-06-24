list = list(map(int, input().split()))
j = 0
m = list[0]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        print(list[i], end=' ')
