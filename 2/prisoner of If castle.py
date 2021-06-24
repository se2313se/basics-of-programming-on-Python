a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if a <= d and (b <= e or c <= e):
    print('yes')
else:
    if a <= e and (b <= d or c <= d):
        print('yes')
    else:
        if b <= d and c <= e or b <= e and c <= d:
            print('yes')
        else:
            print('no')
