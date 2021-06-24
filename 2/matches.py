l, m, a = [], [], []
for i in range(3):
    l.append([int(input()), int(input())])
    m.append([l[i][0], l[i][1], i+1])

m.sort(key=lambda match: match[0:1])
if (m[0][1] >= m[1][0]) and (m[1][1] >= m[2][0]) or (m[0][1] >= m[2][0]):
    print(0)
else:
    if (m[0][1] >= m[1][0]) and (m[1][1] < m[2][0]):
        a.append(m[2][2])
    if (m[0][1] < m[1][0]) and (m[1][1] >= m[2][0]):
        a.append(m[0][2])
    if m[0][1] - m[0][0] >= m[2][0] - m[1][1]:
        a.append(m[0][2])
    if m[2][1] - m[2][0] >= m[1][0] - m[0][1]:
        a.append(m[2][2])
    try:
        print(min(a))
    except:
        print(-1)
