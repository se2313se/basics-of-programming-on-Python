with open('input.txt', 'r', encoding='utf8') as f:
    Lines = [line.strip() for line in f.readlines()]
k = int(Lines[0].split()[0])
A, B = set(Lines[1:k+1]), set(Lines[k+1:])
for c in [A & B, A-B, B-A]:
    print(f'{len(c)}\n{" ".join(sorted(list(c)))}')
