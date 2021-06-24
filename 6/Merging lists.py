
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(range(0, len(A) + len(B)))
i = 0
j = 0
k = 0
while i < len(A) + len(B):
    if (j < len(A)) & (k < len(B)):
        if A[j] < B[k]:
            C[i] = A[j]
            i += 1
            j += 1
        else:
            C[i] = B[k]
            i += 1
            k += 1
    elif j == len(A):
        while k < len(B):
            C[i] = B[k]
            i += 1
            k += 1
    elif k == len(B):
        while j < len(A):
            C[i] = A[j]
            i += 1
            j += 1
print(*C)
