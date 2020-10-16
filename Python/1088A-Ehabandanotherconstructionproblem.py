#https://codeforces.com/problemset/problem/1088/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

x = ini()
if x == 1:
    print(-1)
else:
    print(x, x)
