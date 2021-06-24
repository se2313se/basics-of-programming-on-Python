s = input()
t = s[::-1]
pos1 = s.find('f')
posL = len(s)-t.find('f')-1
if pos1 != -1:
    if pos1 != posL:
        print(pos1, posL)
    else:
        print(pos1)
