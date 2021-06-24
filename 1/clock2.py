N = int(input())
print(((N//3600) % 24), sep='', end=':')
print(((N//60) % 60)//10, ((N//60) % 60) % 10, sep='', end=':')
print((N//10) % 6, (N % 10), sep='')
