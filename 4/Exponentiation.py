def power(a, n):
    s = 1
    if n == 1:
        return a
    elif n == 0:
        return 1
    n -= 1
    return power(a, n) * a


a = float(input())
n = int(input())
print(power(a, n))
