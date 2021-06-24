def CountSort(A):
    B = [0] * 101
    for i in A:
        B[i] += 1
    newA = []
    for i in range(len(B)):
        for j in range(B[i]):
            newA.append(i)
    return newA


numList = list(map(int, input().split()))
numList = CountSort(numList)
print(*numList)
