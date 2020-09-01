#https://codeforces.com/problemset/problem/1401/B

import sys
import bisect
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

ans = []
t = ini()
for _ in range(t):
    a = inl()
    b = inl()
    x = min(a[2], b[1])
    tmp = x * 2
    a[2] -= x
    b[1] -= x
    x = min(b[2], a[2] + a[0])
    b[2] = max(0, b[2] - x)
    a[2] = max(0, a[2] - x)
    tmp -= min(b[2], a[1]) * 2
    ans.append(tmp)
out(ans)
