#https://codeforces.com/contest/1375/problem/C

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
    a = inl()
    ans.append("YES" if a[0] < a[n-1] else "NO")
out(ans)
