y0, x0, y, x = int(input()), int(input()), int(input()), int(input())
dx, dy = x - x0, y - y0
r = (8 > dx >= 0)*(dx % 2 == dy % 2)*(dy**2 <= dx**2)
print('YES'*r + 'NO'*(not r))
