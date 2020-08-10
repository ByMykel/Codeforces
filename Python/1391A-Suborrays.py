#https://codeforces.com/problemset/problem/1391/A

import sys
input = sys.stdin.readline
ins = lambda: input()
ini = lambda: int(input())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

t = ini()
for _ in range(t):
    n = ini()
    print(*[i for i in range(n, 0, -1)])
