i = 0
j = 0
a = int(input())
if a != 0:
    i = a
    j = 1
while a != 0:
    a = int(input())
    if a == i:
        j = j+1
    elif a > i:
        i = a
        j = 1
print(j)
