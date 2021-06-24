def power(a, n):
    s = 1
    if n == 1:
        return a
    elif n == 0:
        return 1
    if n % 2 == 0:
        return power(a, n/2) ** 2
    else:
        return power(a, (n-1)/2) ** 2 * a


a = float(input())
n = int(input())
print(power(a, n))
