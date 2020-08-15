#https://codeforces.com/problemset/problem/1398/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

ans = []
t = ini()
for _ in range(t):
    n = ini()
    a = inl()
    if a[0] + a[1] <= a[n-1]:
        ans.append(f"{1} {2} {n}")
    else:
        ans.append("-1")
print('\n'.join(ans))
