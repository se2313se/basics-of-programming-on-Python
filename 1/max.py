def dvs(A):
    return (2*A)//(A+1)


A = int(input())
B = int(input())
x = A+B-1
y = A-B

print(dvs(x//A-1)*B+dvs(x//B-1)*A+(1-dvs(y*y))*A)
