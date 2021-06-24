A = int(input())
B = int(input())
C = int(input())
if A+B <= C or B+C <= A or C+A <= B:
    print('impossible')
else:
    if A**2 < B**2 + C**2 and A**2 + B**2 > C**2 and A**2 + C**2 > B**2:
        print('acute')
    elif A**2 == B**2 + C**2 or A**2 + B**2 == C**2 or A**2 + C**2 == B**2:
        print('rectangular')
    elif A**2 > B**2 + C**2 or A**2 + B**2 < C**2 or A**2 + C**2 < B**2:
        print('obtuse')
