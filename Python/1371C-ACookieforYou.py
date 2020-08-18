#https://codeforces.com/problemset/problem/1371/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(x))

t = ini()
ans = []
for _ in range(t):
    a, b, n, m = inm()
    ans.append("Yes" if m <= min(a, b) and n+m <= a+b else "No")
out(ans)
