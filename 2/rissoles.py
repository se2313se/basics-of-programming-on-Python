def ifzero(a):
    return 2*a//(a+1)


k, m, n = int(input()), int(input()), int(input())
if k >= n:
    print(2 * m)
elif n == 0:
    print(0)
else:
    print(((2*n-(2*n % k)) // k + ifzero(2*n % k)) * m)
