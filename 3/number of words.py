s = input()
if len(s) == 0:
    print('0')
else:
    if s.count(' ') == 0:
        print('1')
    else:
        print(s.count(' ') + 1)
