#https://codeforces.com/problemset/problem/1538/A

import sys

input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s="\n": print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n = ini()
    a = inl()
    low = [101, -1]
    great = [0, -1]
    for i in range(n):
        if a[i] < low[0]:
            low[0] = a[i]
            low[1] = i
        if a[i] > great[0]:
            great[0] = a[i]
            great[1] = i
    print(
        min(
            max(low[1], great[1]) + 1,
            n - min(low[1], great[1]),
            min(low[1], great[1]) + n - max(low[1], great[1]) + 1,
        )
    )
