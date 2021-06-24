def distance(x1, y1, x2, y2):
    s = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)
    return s


def IsPointInCircle(x, y, xc, yc, r):
    return distance(x, y, xc, yc) <= r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
