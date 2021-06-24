class Applicant:
    name = ''
    score1 = 0
    score2 = 0
    score3 = 0
    score = 0


def CountSort(A):
    B = [0] * 301
    for applicant in A:
        B[applicant.score] += 1
    newA = []
    for i in range(len(B)):
        if B[i] > 0:
            newA.append((i, B[i]))
    return newA


def PassingScore(A, K):
    if len(A) <= K:
        return 0
    newA = CountSort(A)
    if newA[-1][1] > K:
        return 1
    j = -1
    i = newA[j][1]
    PS = newA[j][0]
    while i <= K:
        j -= 1
        i += newA[j][1]
    return newA[j+1][0]


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
inFileLines = inFile.readlines()
K = int(inFileLines[0])
appList = []
for line in inFileLines[1:len(inFileLines)]:
    tempApplicantData = line.split()
    applicant = Applicant()
    applicant.score1 = int(tempApplicantData[-3])
    applicant.score2 = int(tempApplicantData[-2])
    applicant.score3 = int(tempApplicantData[-1])
    if (applicant.score1 >= 40) and \
            (applicant.score2 >= 40) and (applicant.score3 >= 40):
        applicant.name = tempApplicantData[:-3]
        applicant.score = applicant.score1 +\
            applicant.score2 + applicant.score3
        appList.append(applicant)
appList.sort(key=lambda a: -a.score)
print(PassingScore(appList, K))
