i = 0
j = 0
a = int(input())
i = a
if a != 0:
    a = int(input())
    if a > i:
        j = i
        i = a
    else:
        j = a
while a != 0:
    a = int(input())
    if a >= i:
        j = i
        i = a
    elif a > j:
        j = a
print(j)
