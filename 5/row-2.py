a = int(input())
b = int(input())
if a < b:
    for j in range(a, b + 1):
        print(j, end=' ')
else:
    for j in range(a, b - 1, -1):
        print(j, end=' ')
