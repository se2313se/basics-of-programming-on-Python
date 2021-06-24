from itertools import accumulate


def ssum(a, b):
    return a+b


print(*accumulate(map(int, input().split()), ssum))
