def distance(x1, y1, x2, y2):
    s = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)
    return s


x = [0, 0, 0]
y = [0, 0, 0]
p = 0
for i in range(3):
    x[i] = float(input())
    y[i] = float(input())
for i in range(3):
    p += distance(x[i], y[i], x[(i+1) % 3], y[(i+1) % 3])
print(p)
