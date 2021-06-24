class Contestant:
    SecondName = ''
    FirstName = ''
    SchoolNum = 0
    Score = 0


def contestantKey(contestant):
    return contestant.SecondName


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
contestantList = []
for line in inFile:
    tempContestantData = line.split()
    contestant = Contestant()
    contestant.SecondName = tempContestantData[0]
    contestant.FirstName = tempContestantData[1]
    contestant.SchoolNum = int(tempContestantData[2])
    contestant.Score = int(tempContestantData[3])
    contestantList.append(contestant)
contestantList.sort(key=contestantKey)
for line in contestantList:
    print(line.SecondName, line.FirstName, line.Score, file=outFile)
inFile.close()
outFile.close()
