A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A >= C or (A - C)**2 < (B - D)**2 or (B - D) % 2 != (A-C) % 2:
    print('NO')
else:
    print('YES')
