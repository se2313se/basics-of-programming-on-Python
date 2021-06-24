def C(n, k):
    if not k:
        return 1
    if k == 1:
        return n
    elif k == n:
        return 1
    return C(n-1, k-1) + C(n-1, k)


n, k = int(input()), int(input())
print(C(n, k))
