synonyms = dict()
n = int(input())
for i in range(n):
    tempWord, tempSynonyms = input().split()
    synonyms[tempWord] = tempSynonyms
    synonyms[tempSynonyms] = tempWord
print(synonyms[input()])
