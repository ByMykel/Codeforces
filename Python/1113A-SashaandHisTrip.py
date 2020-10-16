#https://codeforces.com/problemset/problem/1113/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n, v = inm()
if n < v:
    print(n - 1)
else:
    x = n - v
    print((x*(x+1) // 2) + v - 1)
