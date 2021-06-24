def phib(k):
    if k <= 2:
        return 1
    if k < 1:
        return 0
    else:
        return phib(k-1)+phib(k-2)


print(phib(int(input())))
