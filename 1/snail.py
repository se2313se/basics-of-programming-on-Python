H = int(input())
A = int(input())
B = int(input())
print((H-A)//(A-B) + ((H-A) % (A-B)+(-H+A) % (A-B))//(A-B) + 1)
