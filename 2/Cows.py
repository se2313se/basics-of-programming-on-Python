A = int(input())
if A > 10 and A < 20:
    print(A, 'korov')
elif A % 10 == 0:
    print(A, 'korov')
elif A % 10 == 1:
    print(A, 'korova')
elif A % 10 < 5:
    print(A, 'korovy')
else:
    print(A, 'korov')
