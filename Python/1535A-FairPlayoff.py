#https://codeforces.com/problemset/problem/1535/A

import sys

input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s="\n": print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    s = inl()
    x = sorted(s)
    if max(s[0:2]) in x[2:] and max(s[2:]) in x[2:]:
        print("YES")
    else:
        print("NO")
