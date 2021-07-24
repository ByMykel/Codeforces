#https://codeforces.com/problemset/problem/1551/A

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
    x = n // 3
    if n % 3:
        if x + x * 2 + 1 == n:
            print(x + 1, x)
        else:
            print(x, x + 1)
    else:
        print(x, x)
