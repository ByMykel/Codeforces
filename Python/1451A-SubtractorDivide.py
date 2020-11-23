#https://codeforces.com/problemset/problem/1451/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n = ini()
    if n in [1, 2, 3]:
        print(n - 1)
    else:
        if n % 2:
            print(3)
        else:
            print(2)
