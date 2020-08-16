#https://codeforces.com/problemset/problem/1392/A

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
    ans.append(n if len(set(a)) == 1 else 1)
print('\n'.join(map(str, ans)))
