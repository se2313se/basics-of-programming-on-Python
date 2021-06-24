def revseq():
    n = int(input())
    if n == 0:
        print(n)
        return 0
    revseq()
    print(n)
    return 0


revseq()
