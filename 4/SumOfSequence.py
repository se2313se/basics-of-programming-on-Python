def SumOfSequence():
    n = int(input())
    if n == 0:
        return 0
    return n + SumOfSequence()


print(SumOfSequence())
