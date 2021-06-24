P = int(input())
X = int(input())
Y = int(input())
X1 = X*(1+P/100)
Y1 = Y*(1+P/100)
p = X1*100+Y1
X = int(p//100)
Y = int(p % 100)
print(X, Y)
