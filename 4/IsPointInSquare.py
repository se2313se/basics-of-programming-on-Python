def IsPointInSquare(x, y):
    return (abs(x) <= 1.0) & (abs(y) <= 1.0)


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
