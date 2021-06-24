class Contestant:
    SecondName = ''
    Score = 0


def contestantKey(contestant):
    return -contestant.Score


N = int(input())
contestantList = []
for line in range(N):
    tempContestantData = input().split()
    contestant = Contestant()
    contestant.SecondName = tempContestantData[0]
    contestant.Score = int(tempContestantData[1])
    contestantList.append(contestant)
contestantList.sort(key=contestantKey)
for line in contestantList:
    print(line.SecondName)
