def sum(a, b):
    if b > 0:
        a += 1
        b -= 1
        return sum(a, b)
    else:
        return a


a = int(input())
b = int(input())
print(sum(a, b))
