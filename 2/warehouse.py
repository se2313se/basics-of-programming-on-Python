A, B, C = int(input()), int(input()), int(input())
a, b, c = int(input()), int(input()), int(input())
print(max((A//a)*(B//b)*(C//c), (A//b)*(B//a)*(C//c), (A//a)*(B//c)*(C//b),
          (A//b)*(B//c)*(C//a), (A//a)*(B//b)*(C//c), (A//c)*(B//b)*(C//a)))
