a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if d != 0:
    x = (e-f*b/d)/(a-c*b/d)
    y = (f-c*x)/d
    print(x, y)
else:
    if b != 0:
        x = (f - e * d / b) / (c - a * d / b)
        y = (e - a * x) / b
        print(x, y)
