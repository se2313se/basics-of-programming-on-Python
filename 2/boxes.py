a, b, c = int(input()), int(input()), int(input())
d, e, f = int(input()), int(input()), int(input())
if a <= b:
    if a <= c:
        if b <= c:
            a1, b1, c1 = (a, b, c)
        else:
            a1, b1, c1 = (a, c, b)
    else:
        a1, b1, c1 = (c, a, b)
elif b <= c:
    if a <= c:
        a1, b1, c1 = (b, a, c)
    else:
        a1, b1, c1 = (b, c, a)
else:
    a1, b1, c1 = (c, b, a)
if d <= e:
    if d <= f:
        if e <= f:
            d1, e1, f1 = (d, e, f)
        else:
            d1, e1, f1 = (d, f, e)
    else:
        d1, e1, f1 = (f, d, e)
elif e <= f:
    if d <= f:
        d1, e1, f1 = (e, d, f)
    else:
        d1, e1, f1 = (e, f, d)
else:
    d1, e1, f1 = (f, e, d)
if a1 <= d1 and b1 <= e1 and c1 <= f1 and (a1 != d1 or b1 != e1 or c1 != f1):
    print('The first box is smaller than the second one')
elif a1 == d1 and b1 == e1 and c1 == f1:
    print('Boxes are equal')
elif a1 >= d1 and b1 >= e1 and c1 >= f1 and (a1 != d1 or b1 != e1 or c1 != f1):
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
