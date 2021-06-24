def ReduceFraction(n, m):
    s = gcd(n, m)
    n = int(n/s)
    m = int(m/s)
    return n, m


def gcd(n, m):
    if n == m:
        return n
    elif m > n:
        if m % n == 0:
            return n
        m = m % n
    else:
        if n % m == 0:
            return m
        n = n % m
    return gcd(n, m)


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
