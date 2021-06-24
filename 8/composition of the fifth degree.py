import itertools as ft
print(list(ft.accumulate(('1 ' + input()).split(), lambda x, y: int(x) * (int(y)) ** 5))[-1])
