#https://codeforces.com/problemset/problem/1366/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

ans = []
t = ini()
for _ in range(t):
    n, x, m = inm()
    c, d = x, x
    for _ in range(m):
        l, r = inm()
        if c >= l and c <= r:
            c = min(c, l)
        if l >= c and l <= d:
            d = max(d, r)
    ans.append(d - c + 1)
out(ans)
