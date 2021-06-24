from math import sqrt
A = float(input())
B = float(input())
C = float(input())
if B**2 > 4*A*C:
    if (-B-sqrt(B**2-4*A*C))/(2*A) < (-B+sqrt(B**2-4*A*C))/(2*A):
        print((-B-sqrt(B**2-4*A*C))/(2*A), (-B+sqrt(B**2-4*A*C))/(2*A))
    else:
        print((-B+sqrt(B**2-4*A*C))/(2*A), (-B-sqrt(B**2-4*A*C))/(2*A))
elif B**2 == 4*A*C:
    print(-B/(2*A))
