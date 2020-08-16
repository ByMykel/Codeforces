#https://codeforces.com/problemset/problem/1392/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

ans = []
t = ini()
for _ in range(t):
    n, k = inm()
    a = inl()
    k = 1 if k % 2 else 2
    for i in range(k):
        d = max(a)
        for i in range(n):
            a[i] = d - a[i]
    ans.append(a)
for i in ans:
    print(*i)
