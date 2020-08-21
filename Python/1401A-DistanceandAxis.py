#https://codeforces.com/problemset/problem/1401/A

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
    n, k = inm()
    if n < k:
        ans.append(k - n)
    else:
        ans.append((n - k) % 2)
out(ans)
