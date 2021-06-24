n = int(input())
S = list(map(int, input().split()))
for i in range(0, n):
    S[i] = (S[i], i+1)
S.sort()
m = int(input())
B = list(map(int, input().split()))
for i in range(0, m):
    B[i] = (B[i], i+1)
B.sort()
k = 0
R = list(range(0, n))
j = 1
if m == 1:
    for i in range(0, n):
        R[i] = 1
else:
    for i in range(0, n):
        while (j < m) and ((S[i][0]-B[j-1][0])**2 > (S[i][0]-B[j][0])**2):
            j += 1
        R[S[i][1]-1] = B[j-1][1]
print(*R)
