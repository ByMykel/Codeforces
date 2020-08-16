#https://codeforces.com/problemset/problem/1392/C

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
    prev = 0
    count = 0
    for i in range(n):
        count += max(0, prev - a[i])
        prev = a[i]
    ans.append(count)
print('\n'.join(map(str, ans)))
