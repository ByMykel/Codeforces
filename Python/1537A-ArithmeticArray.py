#https://codeforces.com/problemset/problem/1537/A

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
    x = sum(a)
    print(x - n if x - n >= 0 else 1)
