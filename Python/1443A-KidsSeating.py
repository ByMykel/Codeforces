#https://codeforces.com/problemset/problem/1443/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for i in range(t):
    n = ini()
    print(*[i for i in range(4*n, n*2, -2)])
