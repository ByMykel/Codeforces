#https://codeforces.com/problemset/problem/401/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n, x = inm()
a = inl()
total = sum(a)
if total == 0:
    print(0)
elif abs(total) < x:
    print(1)
else:
    print((abs(total) + x - 1) // x)
