#https://codeforces.com/problemset/problem/1420/A

import sys
import bisect
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n = ini()
    a = inl()
    if len(set(a)) == n and a == sorted(a, reverse=True):
        print("NO")
    else:
        print("YES")
