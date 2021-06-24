from math import ceil
X = float(input())
print(int(X), int(ceil(2*(int(1000*X)/10 - 100*int(X)))/2))
