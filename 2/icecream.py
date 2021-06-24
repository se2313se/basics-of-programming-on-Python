k = int(input())
r = ((k-5) % 3 == 0)*((k-5) >= 0) or \
    ((k-10) % 3 == 0)*((k-10) >= 0) or ((k % 3) == 0) or ((k % 5) == 0)
print('YES'*r + 'NO'*(not r))
