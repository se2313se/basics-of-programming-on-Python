a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == 0:
    print('INF')
elif c != 0:
    if -b/a == -d/c or b % a != 0:
        print('NO')
    else:
        print(-b//a)
else:
    if b % a != 0:
        print('NO')
    else:
        print(-b//a)
