#https://codeforces.com/problemset/problem/1400/A

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
    n = ini()
    s = ins()
    ans.append(n * s[(2*n-1) // 2])
out(ans)
