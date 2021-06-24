n = int(input())
studentsList = list()
for i in range(n):
    m = int(input())
    studentsList.append(set())
    for j in range(m):
        studentsList[i].add(input())

dis = studentsList[0]
con = studentsList[0]
for a in studentsList:
    dis = dis | a
    con = con & a

print(len(con))
for a in con:
    print(a)
print(len(dis))
for a in dis:
    print(a)
