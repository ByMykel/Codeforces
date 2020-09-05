#https://codeforces.com/contest/1409/problem/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    a, b, x, y, n = inm()
    tmpa = min(b-y, n)
    tmpb = min(a-x, n)
    print(min((b-tmpa) * (a - min(a-x, n-tmpa)), (a-tmpb) * (b - min(b-y, n-tmpb))))
