s = input()
t = s[::-1]
pos1 = s.find('f')
if pos1 != -1:
    pos2 = s[pos1+1::].find('f')
    if pos2 != -1:
        print(pos1 + pos2 + 1)
    else:
        print('-1')
else:
    print('-2')
