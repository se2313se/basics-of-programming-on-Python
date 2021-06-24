l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())

if h1+h2 <= hc and \
        (max(l1, l2) <= lc and max(w1, w2) <= wc or
         max(l1, w2) <= lc and max(w1, l2) <= wc or
         max(w1, l2) <= lc and max(l1, w2) <= wc or
         max(w1, w2) <= lc and max(l1, l2) <= wc):
    print('YES')
elif h1 > hc or h2 > hc:
    print('NO')
else:
    if (l1+l2 <= lc and max(w1, w2) <= wc) \
            or (l1+l2 <= wc and max(w1, w2) <= lc):
        print('YES')
    elif (l1 + w2 <= lc and max(w1, l2) <= wc) \
            or (l1 + w2 <= wc and max(w1, l2) <= lc):
        print('YES')
    elif (max(l1, l2) <= lc and w1+w2 <= wc) \
            or (max(l1, l2) <= wc and w1+w2 <= lc):
        print('YES')
    elif (max(l1, w2) <= lc and w1+l2 <= wc) \
            or (max(l1, w2) <= wc and w1+l2 <= lc):
        print('YES')
    else:
        print('NO')
