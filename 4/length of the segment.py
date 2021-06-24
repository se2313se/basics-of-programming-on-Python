def distance(x1, y1, x2, y2):
    s = (((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** (1/2)
    return s


t = [0, 0, 0, 0]
for i in range(4):
    t[i] = float(input())
print(distance(t[0], t[1], t[2], t[3]))
