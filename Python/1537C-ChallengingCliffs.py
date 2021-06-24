#https://codeforces.com/problemset/problem/1537/C

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
    a = sorted(inl())
    closest = 1e9 + 7
    closest_index = [-1, -1]
    for i in range(1, n):
        if a[i] - a[i - 1] < closest:
            closest = a[i] - a[i - 1]
            closest_index = i - 1
    if n == 2:
        print(*a)
    else:
        print(*a[closest_index + 1:], *a[:closest_index + 1])
