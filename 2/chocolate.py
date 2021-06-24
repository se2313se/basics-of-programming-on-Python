A = int(input())
B = int(input())
C = int(input())
if (C % A == 0 or C % B == 0) and A*B >= C:
    print('YES')
else:
    print('NO')
