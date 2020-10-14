#https://codeforces.com/problemset/problem/1093/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    s = ins()
    if len(set(s)) == 1:
        print(-1)
    else:
        out(sorted(s), "")
