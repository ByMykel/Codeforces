#https://codeforces.com/problemset/problem/1512/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))
 
t = ini()
for _ in range(t):
    n = ini()
    b = []
    a = [list(ins()) for i in range(n)]
    for y in range(n):
        for x in range(n):
            if a[y][x] == "*":
                b.append([y, x])
    if b[0][0] == b[1][0]:
        if b[0][0] == 0:
            b[0][0] += 1
            b[1][0] += 1
        else:
            b[0][0] -= 1
            b[1][0] -= 1
    elif b[0][1] == b[1][1]:
        if b[0][1] == 0:
            b[0][1] += 1
            b[1][1] += 1
        else:
            b[0][1] -= 1
            b[1][1] -= 1
    else:
        b[0][0], b[0][1], b[1][0], b[1][1] = b[0][0], b[1][1], b[1][0], b[0][1]
    a[b[0][0]][b[0][1]] = "*"
    a[b[1][0]][b[1][1]] = "*"
    out(["".join(i) for i in a])
