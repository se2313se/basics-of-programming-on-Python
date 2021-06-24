def gcd(a, b):
    if not a % b:
        return b
    else:
        return gcd(b, a % b)


a, b = int(input()), int(input())
if a >= b:
    print(gcd(a, b))
else:
    print(gcd(b, a))
