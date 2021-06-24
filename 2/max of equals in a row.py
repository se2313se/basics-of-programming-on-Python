i = 0
j = 0
s = 0
a = int(input())
if a != 0:
    i = a
    j = 1
    s = 1
while a != 0:
    a = int(input())
    if a == i:
        j = j+1
        if s < j:
            s = j
    elif a != i:
        i = a
        j = 1
print(s)
