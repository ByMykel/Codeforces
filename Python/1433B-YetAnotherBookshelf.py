#https://codeforces.com/contest/1433/problem/B

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
    a = inl()
    if len(set(a)) != 1:
        print(a.count(0) - a.index(1) - a[::-1].index(1))
    else:
        print(0)
