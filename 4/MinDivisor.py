def MinDivisor(n):
    i = 2
    while i <= n ** (1/2):
        if n % i == 0:
            return i
        i += 1
    return 1


n = int(input())
s = MinDivisor(n)
if s == 1:
    print(n)
else:
    print(s)
