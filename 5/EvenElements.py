list = list(map(int, input().split()))
for i in range(0, len(list)):
    if list[i] % 2 == 0:
        print(list[i], end=' ')
