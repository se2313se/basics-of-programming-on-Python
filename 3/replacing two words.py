s = input()
sep = s.find(' ')
s1 = s[:sep:]
s2 = s[sep+1::]
s = s2 + ' ' + s1
print(s)
