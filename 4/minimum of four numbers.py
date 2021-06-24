def min4(a, b, c, d):
    t = [a, b, c, d]
    s = t[0]
    for i in range(4):
        s = min(s, t[i])
    return s


t = [0, 0, 0, 0]
for i in range(4):
    t[i] = input()
print(min4(t[0], t[1], t[2], t[3]))
