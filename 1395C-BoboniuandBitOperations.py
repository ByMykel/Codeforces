#https://codeforces.com/contest/1395/problem/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

n, m = inm()
a = inl()
b = inl()
for x in range(512):
    outt = True
    for i in a:
        out = False
        for j in set(b):
            if (i & j) | x == x:
                out = True
                break
        if out == False:
            outt = False
    if outt:
        print(x)
        break
