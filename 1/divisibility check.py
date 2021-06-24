def dvs(A):
    return (2 * A*A) // (A*A + 1)


A, B = int(input()), int(input())
print('YES'*(1-dvs(A % B))*(dvs(A//B))+'NO'*dvs(dvs((B-1)//A)+dvs(A % B)))
