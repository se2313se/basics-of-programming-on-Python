s = input()
t = s[::-1]
pos1 = s.find('h')
posL = len(s)-t.find('h')-1
p = s[:pos1:] + s[posL+1::]
print(p)
