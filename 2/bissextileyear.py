A = int(input())
if A % 400 == 0 or (A % 4 == 0 and A % 100 != 0):
    print('YES')
else:
    print('NO')
