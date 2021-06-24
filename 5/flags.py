n = int(input())
s = ('|1 /', '|2 /', '|3 /', '|4 /', '|5 /', '|6 /', '|7 /', '|8 /', '|9 /')
flag = ('+___ ', s, '|__\ ', '|    ')
for j in range(0, 4):
    if j == 1:
        for i in range(0, n):
            print(flag[j][i], end=' ')
        print()
    else:
        for i in range(0, n):
            print(flag[j], end='')
        print()
