def IsPrime(n):
    i = 2
    while i <= n ** (1/2):
        if n % i == 0:
            return 1
        i += 1
    return 0


n = int(input())
if IsPrime(n) == 0:
    print('YES')
else:
    print('NO')
