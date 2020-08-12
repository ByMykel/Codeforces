#https://codeforces.com/problemset/problem/1395/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

n, m, x, y = inm()
xs = x
ys = y
up = False
right = False
for i in range(m):
    for i in range(n):
        print(x, y)
        if x > 1 and up == False:
            x -= 1
        elif x == 1:
            if i != 0:
                x = 0
            up = True
            if y == ys:
                x += xs
        if x < n and up == True:
            x += 1
        elif x == n:
            if i != 0:
                x = n
            up = False
    if y > 1 and right == False:
        y -= 1
    elif y == 1 and right == False:
        right = True
        y += ys
    else:
        y += 1
