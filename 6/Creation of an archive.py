def depth(S, N):
    if S < 0:
        return N + 1
    elif (S == 0) or (N == 0):
        return N
    else:
        S -= L[-N]
        N -= 1
        return depth(S, N)


S, N = map(int, input().split())
L = []
for i in range(0, N):
    L.append(int(input()))
L.sort()
print(N - depth(S, N))
