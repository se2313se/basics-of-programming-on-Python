A, B, C = int(input()), int(input()), int(input())
s = A+B+C
r = (s % 2 != A % 2) or (s % 2 != C % 2) or (s % 2 != B % 2)
print('YES'*r + 'NO'*(not r))
